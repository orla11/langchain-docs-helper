.PHONY: get-docs
get-docs:
	wget -r -A.html -P langchain-docs https://api.python.langchain.com/en/latest/api_reference.html

.PHONY: run
run:
	pipenv run streamlit run main.py

.PHONY: generate-embeddings
generate-embeddings:
	pipenv run python3 ingestion.py