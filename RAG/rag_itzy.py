import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import WikipediaLoader
from deep_translator import GoogleTranslator

# 환경 변수 로드
load_dotenv()

def get_wikipedia_content(query):
    """위키피디아에서 내용을 가져오는 함수"""
    loader = WikipediaLoader(query=query, load_max_docs=1)
    docs = loader.load()
    return docs[0].page_content if docs else ""

def translate_to_japanese(text):
    """텍스트를 일본어로 번역하는 함수"""
    translator = GoogleTranslator(source='auto', target='ja')
    return translator.translate(text)

def create_vector_store(text):
    """텍스트를 벡터 저장소로 변환하는 함수"""
    # 텍스트 분할
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_text(text)
    
    # 임베딩 생성
    embeddings = OpenAIEmbeddings()
    
    # FAISS 벡터 저장소 생성
    vector_store = FAISS.from_texts(texts, embeddings)
    return vector_store

def main():
    # local 벡터 DB가 이으면 수집 안함
    if os.path.exists("itzy_vector_store"):
        vector_store = FAISS.load_local("itzy_vector_store", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    else:
        # ITZY 정보 수집
        print("ITZY 정보를 위키피디아에서 수집 중...")
        itzy_content = get_wikipedia_content("ITZY")
        
        # 일본어 번역
        print("일본어로 번역 중...")
        japanese_content = translate_to_japanese(itzy_content)
        
        # 벡터 저장소 생성
        print("벡터 저장소 생성 중...")
        vector_store = create_vector_store(japanese_content) 
        # 한국어도 추가
        vector_store.add_texts(itzy_content)

    # 백터 디비 local 저장
    vector_store.save_local("itzy_vector_store")
    
    # RAG 체인 생성
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    
    
    # 테스트 쿼리
    test_queries_korean = [
        "ITZY는 언제 데뷔했나요?",
        "ITZY의 멤버는 누구인가요?",
        "ITZY의 대표곡은 무엇인가요?"
    ]
    test_queries_japanese = [
        "ITZYはいつデビューしましたか?",
        "ITZYのメンバーは誰ですか?",
        "ITZYの代表曲は何ですか?"
    ]
    
    print("\nRAG 테스트 결과:")
    for query in test_queries_korean:
        print(f"\n질문: {query}")
        result = qa_chain.invoke({"query": query})
        print(f"답변: {result['result']}")

    for query in test_queries_japanese:
        print(f"\n질문: {query}")
        result = qa_chain.invoke({"query": query})
        print(f"답변: {result['result']}")

if __name__ == "__main__":
    main() 