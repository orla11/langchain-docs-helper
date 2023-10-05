
# LangChain Documentation Helper

# Overview

**LangChain Documentation Helper** is a Python project that uses LangChain to gather information out of LangChain official documentation. It uses Pinecone as a vector store for all the langchain documentation embeddings, the ConversationalRetrievalChain to interact with the embeddings via user prompt, a chat history and streamlit as the frontend.

# Getting Started

## Clone the Repository

`git clone https://github.com/orla11/langchain-docs-helper.git`

## Install Dependencies

`pipenv install`

## Set up API Keys

Ensure you set up your API keys in the .env file.

## Ingest the documentation

1. Download the documentation with `make get-docs`.
2. Generate the embeddings and store them to Pinecone vectorstore with `make generate-embeddings`

## Run the project

`make run`