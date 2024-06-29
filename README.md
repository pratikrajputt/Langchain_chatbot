# Langchain_chatbot

This project is a simple chatbot interface built using Flask, Sentence Transformers, and a pre-trained embedding model.

## Requirements

- Python 3.7 or higher
- Flask
- Sentence Transformers
- NumPy

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd Langchain_chatbot
## 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Prepare Embeddings

Ensure that you have your embeddings.json file prepared. This file should contain the precomputed embeddings and corresponding documents. You can generate this file using the embeddings_store.py script.

## 5. Run the Flask Application
python app.py

The server should start, and you can access the chatbot interface at http://127.0.0.1:5000/.

Usage

Using Postman

You can interact with the chatbot by sending POST requests to the /chat endpoint using Postman or a similar tool.

	1.	Set the URL: http://127.0.0.1:5000/chat
	2.	Set the HTTP method: POST
	3.	Set the headers:
	•	Content-Type: application/json
	4.	Set the body:
{
    "input": "Your question here"
}

Example Response
{
    "response": "Chatbot's response here"
}
