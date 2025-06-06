# Docu LLM (LangChain and LLM-based QA Bot from Loaded Documents)

## 👤 Author

| Name            | Role              | LinkedIn                                      |
|-----------------|-------------------|-----------------------------------------------|
| Jason Emmanuel  | AI Engineer | [linkedin.com/in/jasoneml](https://www.linkedin.com/in/jasoneml/) |

📄 **Docu LLM** is an AI-powered document question-answering application that enables users to upload a PDF file and ask natural language questions about its content. Instead of manually scanning through long and complex documents, users can simply interact with the system to get contextually accurate answers drawn directly from the uploaded file. This makes it especially useful for tasks like reviewing academic papers, analyzing business reports, or understanding legal documents.

At the core of the application is IBM Watsonx’s suite of foundation models. The language generation is powered by the Mixtral model hosted on Watsonx, which can generate high-quality responses based on retrieved context. For understanding and organizing the document, the system uses Watsonx’s embedding model to convert text chunks into numerical representations (embeddings), which are stored in a vector database for efficient semantic search. This allows the system to find and prioritize the most relevant portions of the document when answering a question.

The document is first processed using LangChain’s document loaders and split into smaller, overlapping text chunks for improved context retention. These chunks are embedded and indexed using the Chroma vector store. When a question is asked, the system uses a Retrieval-Augmented Generation (RAG) approach—retrieving relevant chunks and feeding them to the language model for answer generation. This architecture ensures that answers remain grounded in the actual document content while maintaining conversational fluency.

The user interface is built with Gradio, offering a clean and accessible web interface where users can upload a PDF, type in their questions, and receive answers in seconds. The application also includes custom styling for a modern, professional look. Docu LLM demonstrates how large language models, when combined with retrieval systems and user-friendly interfaces, can create powerful tools for information extraction, learning, and productivity.

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
