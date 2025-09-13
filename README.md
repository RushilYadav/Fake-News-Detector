# Fake-News-Detector (Prototype)

This is a **demo AI-based Fake News Detector** built with Python, Streamlit, and Hugging Face Transformers.

**Note:** This project is a prototype for demonstration purpose. The AI predicts based on **text style**.

---

## Features

- Paste a news headline or article and get an AI prediction.
- Displays **prediction label** and **confidence percentage**.
- Optional **detailed model output** for detailed breakdowns.
- Uses **zero-shot classification** with a pre-trained Hugging Face Model.

---

## Tech Stack

- Python
- Streamlit - for web interface
- Transformers - for zero-shot classification
- PyTorch - backend for model

---

## Installation

1. Clone the repository:

> git clone https://github.com/RushilYadav/Fake-News-Detector.git

2. Create a virtual environment:

> python -m venv .venv

3. Activate the virtual environment (cmd):

> .venv\Scripts\activate.bat

4. Install dependencies:

> pip install -r requirements.txt

## How to use the app

1. Run the app:

> streamlit run app.py

2. Open the window and paste a news headline or article in the text area.

3. Click **Check** to see the prediction.

## Future Improvements

- Add more labels to improve predictions
- Integrate real face-checking APIs to cross-reference news.
- Fine-tune the model for better accuracy