import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(page_title="Fake News Detector", layout="wide")
st.title("Fake News Detector")

st.markdown(
    "Enter a news article below, and the model will predict whether it is real or fake."
    "This is just a demo and may not be accurate."
)

@st.cache_resource #add caching to prevent reloading the model each time
def load_model():
    #Check if GPU is available and set device accordingly
    if torch.cuda.is_available():
        device = 0 #GPU
    else:
        device = -1 #CPU
    return pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-1", device=device)

classifier = load_model()

#function to split long text into smaller chunks so each chunk gets processed separately
def split_text(text, max_length=1000):
    sentences = text.split('. ') #split by sentences
    current_chunk = ""
    #iterate through sentences and create chunks
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + '. '
        else:
            yield current_chunk.strip()
            current_chunk = sentence + '. '
    #yield the last chunk
    if current_chunk:
        yield current_chunk.strip()

#text area for user input
user_input = st.text_area("Enter news article text here:", height=300)

#button to trigger prediction
if st.button("Predict"):
    if not user_input.strip():
        st.warning("Please enter text.")
    else:
        labels = ["Real", "Fake"]

        #split input text into manageable chunks
        chunks = list(split_text(user_input, max_length=1000)) or [user_input]

        #aggregate scores from all chunks (dictionary to hold total scores)
        total_scores = {label: 0.0 for label in labels}
        for chunk in chunks:
            result = classifier(chunk, candidate_labels=labels)
            for label, score in zip(result['labels'], result['scores']):
                total_scores[label] += score

        #average scores across chunks
        average_scores = {label: total_scores[label] / len(chunks) for label in total_scores}
        predicted_label = max(average_scores, key=average_scores.get)
        confidence_score = average_scores[predicted_label]

        #set a confidence threshold to determine if prediction is certain or uncertain
        threshold = 0.60
        if confidence_score < threshold:
            st.subheader("Prediction: Uncertain")
            st.info(f"Top guess: {predicted_label} with confidence {confidence_score*100:.2f}%. The model is not confident enough to make a prediction.")
        else:
            st.subheader(f"Prediction: {predicted_label}")
            st.write(f"Confidence: {confidence_score*100:.2f}%")

        st.markdown("---")

        #show detailed scores in an expandable section
        with st.expander("Show detailed model output"):
            st.json(average_scores)