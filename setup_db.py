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
#print(documents[0].page_content) teste

# "picotar" o documento:
print("picotando os docs em chunks")
text_splitter = RecursiveCharacterTextSplitter(
    # esses parametros estão em analise, não cheguei na conclusão se são os melhores
    chunk_size=1000,
    chunk_overlap=100
)

# criar os chunks de texto pro modelo processar maneiro

chunks = text_splitter.split_documents(documents)


print("adicionando chunks no banco de dados vetorial....")
#add esses chunks no db vetorial
vectorstore = Chroma.from_documents(
    collection_name="collectionlegal",
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_PATH,

)

