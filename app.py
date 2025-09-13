import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Fake News Detector", layout="wide")
st.title("Fake News Detector")

st.markdown(
    "Enter a news article below, and the model will predict whether it is real or fake."
    "This is just a demo and may not be accurate."
)

user_input = st.text_area("Enter news article here:", height=200)

#Load zer-shot classification model
def load_model():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)

classifier = load_model()

if st.button("Predict"):
    if not user_input.strip():
        st.warning("Please enter text.")
    else:
        labels = ["Real", "Fake"]
        result = classifier(user_input, candidate_labels=labels)

        label = result['labels'][0]
        score = result['scores'][0] * 100

        st.subheader(f"Prediction: {label}")
        st.write(f"Confidence: {score:.2f}%")
        
        with st.expander("Show detailed model output"):
            st.json(result)