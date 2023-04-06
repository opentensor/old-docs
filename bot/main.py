import os
import openai
import langchain
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = input("Enter your OpenAI API key: ")

# Load documents from src/
loader = DirectoryLoader('src/', glob="**/*.md")
documents = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=0
)
documents_as_texts = text_splitter.split_documents( documents )

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents( documents_as_texts, embeddings )
retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(
    llm = OpenAI(), 
    chain_type = "stuff", 
    retriever = retriever
)

while True:
    query = input("Whats your bittensor question? ")
    print(  qa.run(query) , '\n')