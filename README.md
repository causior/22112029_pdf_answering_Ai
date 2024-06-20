# 22112029_pdf_answering_Ai

# Overview
This project is a PDF question answering (QA) system that leverages natural language processing (NLP) techniques to extract relevant sections from PDF documents in response to user queries. The system uses GloVe embeddings converted to a Word2Vec-compatible format for sentence similarity calculations and provides an interactive web interface built with Streamlit.

To Run the Pogramme in your system you need to: 
- clone the repo 
```bash
git clone https://github.com/yonkosan/PDF-ANSWERING-AI.git
cd PDF-ANSWERING-AI
```
- install the required packages
```bash
pip intall -r requirments.txt
```
# Usage
- Run the application
```bash
streamlit run app.py
```
- upload the pdf file 
- ask the question
- enter to get the answer

# Project Structure
- logic.py: Contains the core logic for processing PDFs, extracting text, converting embeddings, and calculating sentence similarity.
- app.py: Contains the Streamlit code to create the web interface for the application.
  
    
# Dependencies
* Python 3.7+
* Gensim
* PyMuPDF
* Scikit-learn
* Streamlit
