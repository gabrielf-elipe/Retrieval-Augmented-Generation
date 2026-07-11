from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
import gradio as gr


DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"


# to usando ollama pq é gratuito e roda local, tentei usar claude e openai, mas tem que pagar pra usar
# embedding
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)
# define a llm q vai ser usada
llm = ChatOllama(model="llama3.2:3b", temperature=0.6) 
# ja testei o phi,llama3.2:3b, stablelm2 e qwen3.5, o qwen3.5 foi o que funcionou melhor mas ele demora muito pra rodar no meu pc
#então segui com o llama3.2:3b, que foi o segundo melhor
load_db=Chroma(collection_name="collectionlegal", persist_directory=CHROMA_PATH,embedding_function=embeddings)
retriever=load_db.as_retriever(search_kwargs={"k":10}) #especificando que vai retornar os 4 (default) docs mais relevantes para a query
def format_docs(docs):
    contexto = "\n\n".join(doc.page_content for doc in docs)

    """
    print("===== CONTEXTO =====")
    print(contexto)
    print("====================")
    """
   
    # ^^^^ descomentar isso aqui se quiser ver oq a ia ta recebendo como contexto
    

    return contexto
template = """ Use the following context as your only knowledge \n
Context:{context}
\n
When answering the user:
- If you don't know the answer, simply and always state that you don't know.
- Avoid mentioning that the information was sourced from the context.
- Respond in brazilian portuguese.

- Strictly adhere to the user's question and provide relevant information. 
- Answer succintly and straight to the point
Given the context information, address the query.\n
Query: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()

setup_and_retrieval = RunnableParallel(
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
)
chain = setup_and_retrieval | prompt | llm | output_parser

def answer(message, history):
    response = chain.invoke(message)
    return response

interface = gr.ChatInterface(
    answer,
    examples=["Analisando os documentos, o que pode ser apontado como tema principal?"],
    title="Retrieval-Augmented Generation",
    description="Faça perguntas sobre seus documentos PDF",
    textbox=gr.Textbox(
        placeholder="Digite sua pergunta aqui...",
        container=False,
        scale=7
    ),
)

interface.launch()
#tenho que testar com diferentes tamanhos de doc.

