# ITZY RAG 프로젝트

이 프로젝트는 Langchain을 사용하여 ITZY 가수의 정보를 수집하고 일본어로 번역한 후, RAG(Retrieval-Augmented Generation)를 통해 질의응답을 수행하는 시스템입니다.

## 기능

- 위키피디아에서 ITZY 정보 수집
- 수집된 정보를 일본어로 번역
- FAISS를 사용한 벡터 데이터베이스 구축
- RAG를 통한 질의응답 시스템 구현
- 한국어 및 일본어 질의응답 지원

## 설치 방법

1. 저장소 클론:
```bash
git clone https://github.com/your-username/RAG_itzy.git
cd RAG_itzy
```

2. 가상환경 생성 및 활성화:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux의 경우
# Windows의 경우: .venv\Scripts\activate
```

3. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

4. 환경 변수 설정:
- `.env` 파일을 생성하고 OpenAI API 키를 설정합니다:
```
OPENAI_API_KEY=your_api_key_here
```

## 실행 방법

```bash
python rag_itzy.py
```

## 프로젝트 구조

- `rag_itzy.py`: 메인 실행 파일
- `requirements.txt`: 필요한 패키지 목록
- `.env`: API 키 등 환경 변수 설정 파일
- `itzy_vector_store/`: 벡터 데이터베이스 저장 디렉토리

## 사용된 기술

- Langchain
- OpenAI API
- FAISS
- Wikipedia API
- Google Translator

## 라이선스

MIT License