from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA

import gradio as gr
import warnings
warnings.filterwarnings("ignore")

def get_llm():
    model_id = 'mistralai/mixtral-8x7b-instruct-v01'
    parameters = {
        GenParams.MAX_NEW_TOKENS: 256,
        GenParams.TEMPERATURE: 0.5,
    }
    project_id = "skills-network"
    watsonx_llm = WatsonxLLM(
        model_id=model_id,
        url="https://us-south.ml.cloud.ibm.com",
        project_id=project_id,
        params=parameters,
    )
    return watsonx_llm

def watsonx_embedding():
    embed_params = {
        EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
        EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True},
    }
    embedding = WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr",
        url="https://us-south.ml.cloud.ibm.com",
        project_id="skills-network",
        params=embed_params,
    )
    return embedding

def document_loader(file):
    loader = PyPDFLoader(file.name)
    return loader.load()

def text_splitter(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len,
    )
    return splitter.split_documents(documents)

def vector_database(chunks):
    embedding_model = watsonx_embedding()
    vectordb = Chroma.from_documents(chunks, embedding_model)
    return vectordb

def retriever(file):
    documents = document_loader(file)
    chunks = text_splitter(documents)
    vectordb = vector_database(chunks)
    return vectordb.as_retriever()

def retriever_qa(file, query):
    llm = get_llm()
    retriever_obj = retriever(file)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever_obj,
        return_source_documents=False
    )
    result = qa_chain.invoke(query)
    return result["result"]

with gr.Blocks(css="""
    .gradio-container {
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #e0f7fa, #e1bee7);
        padding: 2em;
        min-height: 100vh;
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.3em;
    }
    .description {
        font-size: 1.1em;
        color: #34495e;
        text-align: center;
        margin-bottom: 2em;
    }
    .footer {
        font-size: 0.85em;
        color: #95a5a6;
        text-align: center;
        margin-top: 3em;
    }
""") as rag_application:

    gr.HTML("<div class='title'>📄 Docu LLM</div>")
    gr.HTML("<div class='description'>Upload a PDF and ask a question. Docu LLM will answer based on the content of the uploaded document.</div>")

    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(
                label="📂 Upload PDF File", 
                file_types=[".pdf"], 
                file_count="single", 
                type="filepath"
            )
        with gr.Column(scale=2):
            question_input = gr.Textbox(
                label="❓ Ask a Question",
                placeholder="What do you want to know from the document?",
                lines=3
            )

    with gr.Row():
        submit_btn = gr.Button("🚀 Get Answer", variant="primary")

    with gr.Row():
        answer_output = gr.Textbox(label="🧠 Answer", lines=6)

    submit_btn.click(
        fn=retriever_qa,
        inputs=[pdf_input, question_input],
        outputs=answer_output
    )

    gr.HTML("<div class='footer'>© 2025 Docu LLM | Powered by IBM Watsonx and LangChain</div>")

rag_application.launch(server_name="0.0.0.0", server_port=7862)