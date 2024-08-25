from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain_community.retrievers import ArxivRetriever
from langchain_community.retrievers import WikipediaRetriever
from langchain.tools.retriever import create_retriever_tool
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import streamlit as st
import PyPDF2
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()
import os

# Step 1: Set up the Streamlit interface for PDF upload
st.title("PDF Question Answering with RAG")

uploaded_pdf=st.file_uploader("Upload A PDF" ,type='pdf'
)

if uploaded_pdf:

    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_pdf.getbuffer())
    pdf_loader=PyPDFLoader("temp_uploaded.pdf")
    documents=pdf_loader.load()

    # Step 2: Embed PDF content and store in vector store
    embedings=OpenAIEmbeddings()
    vector_store=FAISS.from_documents(documents,embedings)

    retriever = vector_store.as_retriever()

    # Step 3: Integrate LangChain for PDF-based QA with vector store
    pdf_qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)

    question = st.text_input("Ask a question about the PDF")

    if question:
            # will Retrieve answer from PDF content using the vector store
            answer = pdf_qa_chain.invoke(question)


            answer_text = answer['result'] if 'result' in answer else answer
            # Step 4: RAG System
            if "I'm not sure" in answer_text or len(answer_text.strip()) == 0:
                    st.write("The PDF content didn't have the answer. Retrieving from external sources...")
                    arxiv_retriever = ArxivRetriever()
                    wikipedia_retriever = WikipediaRetriever()

                    tools = [
                            Tool(name="Arxiv", retriever=arxiv_retriever),
                            Tool(name="Wikipedia", retriever=wikipedia_retriever)]
                    rag_agent=create_retriever_tool(tools,llm=OpenAI())
                    answer=rag_agent.invoke(question)
            st.write(f"Answer: {answer}")

        
