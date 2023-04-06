import os
import openai
import langchain
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = "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"

loader = DirectoryLoader('bittensor/', glob="**/*.md")
documents = loader.load()

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents_as_texts = text_splitter.split_documents( documents )

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(documents_as_texts, embeddings)
retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)


query = "how can I register a delegate?"
print( qa.run(query) )