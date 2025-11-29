#!/usr/bin/env python3
import sys
import json
import boto3
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def improve_transcript(input_file):
    transcript = Path(input_file).read_text()
    
    region = os.getenv('AWS_REGION', 'us-east-1')
    model_id = os.getenv('BEDROCK_MODEL_ID', 'us.anthropic.claude-sonnet-4-20250514-v1:0')
    
    bedrock = boto3.client('bedrock-runtime', region_name=region)
    
    prompt = f"""Rewrite this transcript following these guidelines:
- Do not add or remove content
- Fix broken sentences
- Use proper words to express the idea
- Fix grammar
- Break long sentences into shorter ones for better readability

Transcript:
{transcript}"""
    
    response = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 10000,
            "messages": [{"role": "user", "content": prompt}]
        })
    )
    
    result = json.loads(response['body'].read())
    improved_text = result['content'][0]['text']
    
    output_file = Path(input_file).with_stem(Path(input_file).stem + '_improved')
    output_file.write_text(improved_text)
    
    print(f"Improved transcript saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python improve_transcript.py <transcript_file>")
        sys.exit(1)
    
    improve_transcript(sys.argv[1])
