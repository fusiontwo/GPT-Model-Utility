from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import os
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

loader = PyPDFLoader("./chapter5/ExplorersGuide.pdf")
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(pages, embeddings)

q = "What is Link's traditional outfit color?"
content = db.similarity_search(q)[0]

print("Similarity Search: \n", content)
print("\n")

llm = OpenAI()
chain = RetrievalQA.from_llm(llm=llm, retriever=db.as_retriever())
q = "What is Link's traditional outfit color?"
response = chain.invoke(q, return_only_outputs=True)

print("Answer: \n", response)