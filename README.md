# Docu LLM (LangChain and LLM-based QA Bot from Loaded Documents)

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

<img width="959" alt="image" src="https://github.com/user-attachments/assets/d07f0403-78f7-4283-9d64-2485dad43e45" />

The web front end of Docu LLM features a clean and user-friendly interface designed for interacting with the content of uploaded PDF documents. On the left side, users can upload a PDF file by either dragging and dropping it or clicking the designated upload area. To the right, there is a text box labeled "Ask a Question," where users can type any question they want to ask based on the uploaded document. Once both the PDF and the question are provided, clicking the orange "Get Answer" button will trigger the system to analyze the content and display the answer in the "Answer" section below. This setup enables users to easily explore and extract information from research papers or other complex documents.

<img width="959" alt="Screenshot 2025-06-06 134317" src="https://github.com/user-attachments/assets/c1f52faa-ecba-4bd4-aa2b-e5defe5f713a" />

In this step, a user is selecting and uploading a scientific research paper titled "Fine-tuning Pretrained Multilingual BERT Model for Indonesian Aspect-based Sentiment Analysis" to the Docu LLM web application. The upload is done by navigating through the file explorer window and choosing the appropriate PDF file, shown here as 2103.03732v1.

<img width="959" alt="image" src="https://github.com/user-attachments/assets/efbb2a70-64f4-4e18-bbaf-9a929867f8d1" />

After uploading the scientific research paper file in .pdf extension, a sample question is entered, such as: "Explain how the sentence-pair classification approach using auxiliary pseudo-sentences improves the performance of the ABSA task compared to single-sentence classification, and why this approach is more compatible with BERT’s pretraining architecture." The app then processes the PDF and provides an answer based on the content of the uploaded document.

---

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
```
