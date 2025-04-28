# RAG 테스트 코드

import os
import sys
import time
import json
import requests

# 환경 변수 설정
os.environ["OPENAI_API_KEY"] = "sk-proj-1234567890"

# 테스트 데이터 준비
test_data = [
    {"question": "What is the capital of France?", "answer": "Paris"},
]

# 테스트 실행
for data in test_data:
    print(f"Question: {data['question']}")
    print(f"Answer: {data['answer']}")
    print("-" * 50)

