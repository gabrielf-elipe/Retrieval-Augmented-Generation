from langchain_community.document_loaders import DirectoryLoader,PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

#algumas configurações:
DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

# embedding
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)   

#carregar o pdf:
print("carregando os pdfs ")
loader = DirectoryLoader(DATA_PATH,loader_cls=PyMuPDFLoader,use_multithreading=True,max_concurrency=128,show_progress=True,silent_errors=True)

documents = loader.load()
print(documents[0].page_content)

# "picotar" o documento:
print("picotando os docs em chunks")
text_splitter = RecursiveCharacterTextSplitter(
    #usando parametros pequenos, pois estou trabalhando com documentos curtos
    chunk_size=1000,
    chunk_overlap=200
)

# criar os chunks de texto pro modelo processar maneiro

chunks = text_splitter.split_documents(documents)


print("adicionando chunks no banco de dados vetorial....")
#add esses chunks com seus respectivos id no db vetorial
vectorstore = Chroma.from_documents(
    collection_name="collectionlegal",
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_PATH,

)

"""
#teste pra ver se deu tudo certo:
query = "Ditadura Militar brasileira"
dbteste = Chroma(collection_name="collectionlegal",persist_directory=CHROMA_PATH, embedding_function=embeddings)
results=dbteste.similarity_search(query)
#print(results)
print(results[0].page_content)
"""