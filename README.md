# Gen_AI_Tax_Attorney

This project contains the code for an end-to-end infrastructure for a Generative AI Tax Law Research model. It is intended to exist in a Google Cloud Platform environment but could likely be reoriented for another cloud environment. The general flow of work is outlined below. Please note that I am not an attorney and no output from this model should be considered legal advice.

## Creating Reference Database

The infrastructure used in this project is Retrieval Augmented Generative AI for legal research. As such, the first step is to create the reference database of legal precedents. This process is done in the notebook pull_irs_legal_determinations, which scrapes the PDFs of written determinations on the official IRS website. Source PDFs can be found here: https://www.irs.gov/downloads/irs-wd. After pulling the PDFs, the notebook stores useable ones in a cloud storage bucket for later reference.

## Creating RAG Model

After storing reference material the model itself is created in the notebook tax_rag. Here, a Matching Engine and Vector Search is initialized using embeddings from the PDFs pulled earlier. The LangChain
library is then used to integrate this semantic search with the Google Bison generative text model. The result of this chaining is an LLM that is fed context from the most relevant documents based on similarity scores from a semantic search of the question it is asked. This RAG architecture is designed to build a legal research model that will not give hallucinatory answers when asked for tax law precedence.

## Using the Model

Finally, the notebook hit_model is used to test the model itself. It has both a basic example of a question related to tax law to ensure that the search portion of the model functions and that the model itself will not hallucinate. There is a further piece of functionality designed to allow a user to upload a PDF of a case and ask for related cases. 
