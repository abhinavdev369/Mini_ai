# Multi-Task AI Microservice 🤖

A lightweight Python & Flask API that serves three different pre-trained AI models from Hugging Face for real-time Natural Language Processing (NLP).

This project demonstrates how to operationalize multiple sophisticated AI models into a simple, easy-to-use web service. It can perform sentiment analysis, flexible zero-shot classification, and named[...]

---

## 🚀 Features

- **Sentiment Analysis:** Classifies text as POSITIVE or NEGATIVE.  
- **Zero-Shot Classification:** Classifies text against a custom list of labels you provide.  
- **Named Entity Recognition (NER):** Extracts and categorizes entities like people (PER), organizations (ORG), and locations (LOC).  
- **Lightweight & Fast:** Uses the Flask web server and optimized models.  
- **Easy to Test:** All endpoints are accessible via simple GET requests in your browser.

---

## 🛠️ Tech Stack

- **Python:** Core programming language.  
- **Flask:** Lightweight web framework for building the API.  
- **Hugging Face transformers:** Library for downloading and running the pre-trained AI models.  
- **PyTorch:** The deep learning backend used by the models.

---

## 🏁 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### 1. Prerequisites

- Python 3.8 or newer  
- git installed on your machine

### 2. Installation & Setup

Clone the repository:

```bash
git clone https://github.com/abhinavdev369/Mini_ai.git
cd Mini_ai
```

Create a Python Virtual Environment:
(Using venv5 as an example name, like in our setup)

```bash
python -m venv v5
```

Activate the Virtual Environment:

On Windows (PowerShell):

```powershell
.\v5\Scripts\Activate.ps1
```

On macOS / Linux:

```bash
source v5/bin/activate
```

Install the required libraries:

```bash
pip install flask transformers torch
```

### 3. Running the Application

Start the Flask server:

```bash
python app.py
```

Wait for the models to load. The first time you run this, it will download several GB of AI models. This is normal. You will see messages like "Loading AI model..."

Once it says * Running on http://127.0.0.1:5000/, your AI API is live!

---

## 📖 API Endpoints & Usage

You can test all endpoints directly in your web browser.

### 1. Homepage

Shows that the API is running.

- URL: http://127.0.0.1:5000/

---

### 2. Sentiment Analysis

Classifies a piece of text as either POSITIVE or NEGATIVE.

- Endpoint: /analyze  
- Model: distilbert-base-uncased-finetuned-sst-2-english  
- URL Parameter: text

Test URL:

http://127.0.0.1:5000/analyze?text=This is a wonderful project and I am very happy

Sample Response:

```json
{
  "label": "POSITIVE",
  "score": 0.9998819828033447
}
```

---

### 3. Zero-Shot Classification

Classifies text against a custom list of labels you provide.

- Endpoint: /classify  
- Model: facebook/bart-large-mnli  
- URL Parameters: text and labels (comma-separated)

Test URL:

http://1.0.0.1:5000/classify?text=Apple just announced the new M5 chip&labels=technology,sports,politics,food

Sample Response:

```json
{
  "labels": [
    "technology",
    "politics",
    "sports",
    "food"
  ],
  "scores": [
    0.9942001104354858,
    0.002824905328452587,
    0.002167098456993699,
    0.0008078970131464303
  ],
  "sequence": "Apple just announced the new M5 chip"
}
```

---

### 4. Named Entity Recognition (NER)

Extracts people, organizations, locations, and other entities from text.

- Endpoint: /extract  
- Model: dbmdz/bert-large-cased-finetuned-conll03-english  
- URL Parameter: text

Test URL:

http://1.0.0.1:5000/extract?text=My name is Rohan and I work at Google in India.

Sample Response:

```json
[
  {
    "entity_group": "PER",
    "score": 0.9996020793914795,
    "word": "Rohan",
    "start": 11,
    "end": 16
  },
  {
    "entity_group": "ORG",
    "score": 0.9986345171928406,
    "word": "Google",
    "start": 31,
    "end": 37
  },
  {
    "entity_group": "LOC",
    "score": 0.9996538162231445,
    "word": "India",
    "start": 41,
    "end": 46
  }
]
```

---

## 📄 Project Report

For a detailed breakdown of the project methodology, model choices, and results, please see the PROJECT_REPORT.md file.

---

## 📜 License

This project is licensed under the MIT License.
