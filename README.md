# DocuLLM (LangChain and LLM-based QA Bot from Loaded Documents)

## 👤 Author

| Name            | Role              | LinkedIn                                      |
|-----------------|-------------------|-----------------------------------------------|
| Jason Emmanuel  | AI Engineer | [linkedin.com/in/jasoneml](https://www.linkedin.com/in/jasoneml/) |

📄 **DocuLLM** is an interactive document question-answering application that allows users to upload a PDF file and ask questions based on the content of the uploaded document. It leverages IBM Watsonx Foundation Models for natural language understanding and embeddings, combined with LangChain for document processing and retrieval, and Gradio for the web-based user interface.

---

## ✨ Features

- Upload any PDF document and extract its text content.
- Split documents into manageable chunks for efficient semantic search.
- Use IBM Watsonx Large Language Models (LLM) for answering user queries based on document content.
- Generate embeddings using IBM Watsonx embedding models for vector-based retrieval.
- Retrieve relevant information from documents using a vector database powered by Chroma.
- User-friendly web interface built with Gradio.
- Styled UI with a clean, modern look and responsive layout.

---

## 📱 Application Overview



## 📜 Code Overview

- `get_llm()`: Initializes IBM Watsonx LLM with a specified model and parameters.

- `watsonx_embedding()`: Sets up IBM Watsonx embedding model for vector representation.

- `document_loader(file)`: Loads the PDF file and extracts documents.

- `text_splitter(documents)`: Splits documents into chunks for retrieval.

- `vector_database(chunks)`: Creates a vector database from document chunks.

- `retriever(file)`: Combines loading, splitting, and embedding to create a retriever.

- `retriever_qa(file, query)`: Uses LangChain RetrievalQA with Watsonx LLM to answer queries.

---

## 🏗️ Architecture & Technologies

| Component          | Technology / Library                 |
|--------------------|-----------------------------------|
| Large Language Model| IBM Watsonx Foundation Models     |
| Embeddings         | IBM Watsonx Embeddings             |
| Document Loader    | LangChain PyPDFLoader              |
| Text Splitter      | LangChain RecursiveCharacterTextSplitter |
| Vector Store       | Chroma (via langchain_community)  |
| Retrieval QA Chain | LangChain RetrievalQA              |
| Front-End Apps      | Gradio                            |
| Programming Language| Python                           |

---

## 🚀 Installation
**Clone the repository:**

```bash
git clone https://github.com/namoklom/docullm-langchain.git
cd docullm-langchain
'''
