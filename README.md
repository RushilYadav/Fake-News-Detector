# Fake-News-Detector (Prototype)

This is a **demo AI-based Fake News Detector** built with Python, Streamlit, and Hugging Face Transformers.
It now uses **claim verification** with the Google Fact Check Tools API and a **Natural Language Inference** model to conclude whether the claims are likely true, false, or uncertain.

**Note:** This project is a prototype and is not 100% accurate.

---

## Features

- Paste a news headline or article and the app extracts claims.
- Fetches real evidence from Google Fact Check Tools API.
- Uses roberta-large-mnli to verify claims against evidence found.
- Displays **Verification Scores**.
- Aggregates results to give an overall conclusion: TRUE, FALSE, or UNCERTAIN.
- Interactive Streamlit web interface for easy use.

---

## Tech Stack

- Python
- Streamlit - for web interface
- Transformers - Natural Language Inference model for verifying claims.
- PyTorch - backend for model
- Google Fact Check Tools API - retrieving evidence
- Requests - API calls

---

## Installation

1. Clone the repository:

> `git clone https://github.com/RushilYadav/Fake-News-Detector.git`

2. Create a virtual environment:

> `python -m venv .venv`

3. Activate the virtual environment (cmd):

> `.venv\Scripts\activate.bat`

4. Install dependencies:

> `pip install -r requirements.txt`

5. Add Google Fact Check Tools API:

Create a .env file in the root of the project.
Add the line:
> `GOOGLE_FACT_CHECK_API_KEY=Your_Key`

## How to use the app

1. Run the app:

> `streamlit run app.py`

2. Open the window and paste a news headline or article in the text area.

3. Click **Verify** to see the prediction.

## Future Improvements

- Improve evidence retrieval for better claim checks.
- Fine-tune the model for better accuracy.