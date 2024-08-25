



![Untitled Diagram](https://github.com/user-attachments/assets/4dd77063-451d-48cd-abdc-b4ce481169b0)



# PDF Question Answering with RAG

This project provides a tool to answer questions from a PDF document using a Retrieval-Augmented Generation (RAG) approach. If the answer isn't found in the PDF, it retrieves information from external sources like Arxiv and Wikipedia.

## Features

- **PDF Upload:** Upload any PDF file for analysis.
- **Question Answering:** Ask questions about the content of the PDF.
- **External Retrieval:** If the answer isn't in the PDF, the tool searches for it in Arxiv and Wikipedia.

## Setup

Follow these steps to get the project running on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/massudmiyanji/Streamlit-pdf-processor.git
cd your_repository_name


### Install Dependencies
Make sure you have Python installed. Then, install the required Python packages:

pip install -r requirements.txt
### set  up your API Jey in .env file
OPENAI_API_KEY=your_openai_api_key_here

### run streamlit 
streamlit run pdf_qa.py

