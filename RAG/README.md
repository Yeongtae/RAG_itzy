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

## 실행 결과
```
RAG 테스트 결과:
(한국어)
질문: ITZY는 언제 데뷔했나요?
답변: Itzyは2019年2月12日にデビューしました。

질문: ITZY의 멤버는 누구인가요?
답변: ITZY의 멤버는 Yeji, Lia, Ryujin, Chaeryeong, Yuna로 구성되어 있습니다.

질문: ITZY의 대표곡은 무엇인가요?
답변: ITZY의 대표곡은 "달라달라 (Dalla Dalla)"입니다.

(일본어)
질문: ITZYはいつデビューしましたか?
답변: Itzyは2019年2月12日にデビューしました。

질문: ITZYのメンバーは誰ですか?
답변: ITZYのメンバーはYeji、Lia、Ryujin、Chaeryeong、Yunaの5人です。

질문: ITZYの代表曲は何ですか?
답변: 代表曲は「Dalla Dalla」です
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