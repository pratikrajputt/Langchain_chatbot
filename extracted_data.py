# data_extraction.py
from langchain_community.document_loaders import WebBaseLoader

url = 'https://brainlox.com/courses/category/technical'
loader = WebBaseLoader([url])  # Pass the URL list directly to the loader
documents = loader.load()

# Save the documents to a file
with open('documents.txt', 'w') as file:
    for doc in documents:
        file.write(doc.page_content + '\n')  # Use page_content to get the text content