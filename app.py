from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import numpy as np
import json

app = Flask(__name__)

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the embeddings and documents
with open('embeddings.json', 'r') as f:
    embedding_store = json.load(f)

documents = embedding_store['documents']
embeddings = np.array(embedding_store['embeddings'], dtype=np.float32)  # Ensure embeddings are float32

# Print the first document to verify loading
print("First document loaded: ", documents[0])

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('input')
    if not user_input:
        return jsonify({"error": "Invalid input"}), 400

    # Create embedding for the user input
    input_embedding = model.encode(user_input, convert_to_tensor=False).astype(np.float32)  # Ensure input embedding is float32

    # Find the closest document using cosine similarity
    similarities = util.pytorch_cos_sim(input_embedding, embeddings)[0]
    
    # Print similarities to debug
    print("Similarities: ", similarities)
    
    closest_index = np.argmax(similarities)
    
    # Print closest index to debug
    print("Closest index: ", closest_index)
    
    response_text = documents[closest_index]

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)