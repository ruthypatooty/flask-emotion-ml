from flask import Flask, request, jsonify
import pickle, json
from sklearn.feature_extraction.text import TfidfVectorizer
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

current_dir = os.getcwd()
model_path = os.path.join(current_dir,'flask-server', 'trained_model.pkl')
vectorizer_path = os.path.join(current_dir,'flask-server', 'vectorizer.pkl')
with open(model_path, 'rb') as f:
    clf = pickle.load(f)
with open(vectorizer_path,'rb') as f:
    tfidf_vec = pickle.load(f)

@app.route("/getText", methods=['POST'])
def getText():
    if request.is_json:
        data = request.get_json()
        user_text = data.get('text')
        text_tfidf = tfidf_vec.transform([user_text])
        emotion = clf.predict(text_tfidf)[0]

        return jsonify({
            'emotion': emotion,
            'success': True
        }), 200
        
    else:
        return jsonify({"invalid"}), 400


if __name__ == "__main__":
    app.run(debug = True)