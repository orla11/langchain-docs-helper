import os
import config
import pinecone

from typing import Any

from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT"],
)


def run_llm(query: str) -> Any:
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(config.INDEX_NAME, embedding=embeddings)
    chat = ChatOpenAI(verbose=True, temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True
    )
    return qa({"query": query})


if __name__ == "__main__":
    run_llm(query="What is RetrievalQA chain?")
