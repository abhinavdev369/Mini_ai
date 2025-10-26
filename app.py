from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

print("Loading Sentiment AI model...")
sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
print("Sentiment model loaded.")

print("Loading Zero-Shot AI model...")
zero_shot_pipeline = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)
print("Zero-Shot model loaded.")


print("Loading NER AI model...")
ner_pipeline = pipeline(
    "ner", 
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    grouped_entities=True # This makes the output cleaner
)
print("NER model loaded. API is ready!")

@app.route("/")
def home():
    """A homepage to show the API is working."""
    return (
        "Welcome! Your Advanced AI API is running.<br>"
        "Use <b>/analyze?text=...</b> for sentiment.<br>"
        "Use <b>/classify?text=...&labels=...</b> for custom classification.<br>"
        "Use <b>/extract?text=...</b> for entity extraction."
    )


@app.route('/analyze', methods=['GET'])
def analyze_sentiment():
    text_to_analyze = request.args.get('text')
    if not text_to_analyze:
        return jsonify({"error": "Missing 'text' parameter"}), 400
    
    result = sentiment_pipeline(text_to_analyze)
    return jsonify(result[0])

@app.route('/classify', methods=['GET'])
def classify_text():
    text_to_classify = request.args.get('text')
    labels_str = request.args.get('labels')

    if not text_to_classify or not labels_str:
        return jsonify({"error": "Missing 'text' or 'labels' parameters"}), 400
    
    labels_to_use = labels_str.split(',')
    result = zero_shot_pipeline(text_to_classify, labels_to_use)
    return jsonify(result)

@app.route('/extract', methods=['GET'])
def extract_entities():
    """Finds people, places, and organizations in text."""
    text_to_extract = request.args.get('text')
    if not text_to_extract:
        return jsonify({"error": "Missing 'text' parameter"}), 400

    # Run the NER model
    entities = ner_pipeline(text_to_extract)
    return jsonify(entities)

if __name__ == '__main__':
    app.run(debug=True, port=5000)