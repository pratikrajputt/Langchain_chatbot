from sentence_transformers import SentenceTransformer
import numpy as np
import json

# Load pre-trained embedding model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the document texts
with open('documents.txt', 'r') as file:
    documents = file.readlines()

# Create embeddings for each document
embeddings = model.encode(documents, convert_to_tensor=False)

# Store embeddings in a simple dictionary (or use a more sophisticated vector store)
embedding_store = {
    'documents': documents,
    'embeddings': embeddings.tolist()
}

# Save embeddings to a file
with open('embeddings.json', 'w') as f:
    json.dump(embedding_store, f)

print("Embeddings created and stored successfully.")