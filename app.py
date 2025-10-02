import streamlit as st
from transformers import pipeline
import torch
from verify import verify_claim
from checker import get_evidence_for_claim

st.set_page_config(page_title="Fake News Detector", layout="wide")
st.title("Fake News Detector")

st.markdown(
    "Enter a news article below, and the model will predict whether it is real or fake."
)

#text area for user input
user_input = st.text_area("Enter news article text here:", height=300)

#button to trigger verification
if st.button("Verify"):
    if not user_input.strip():
        st.warning("Please enter text.")
    else:
        #split input text into sentences to treat each as a claim
        claims = [sentence.strip() for sentence in user_input.split('. ') if sentence.strip()]

        aggregated_results = {"ENTAILMENT": [], "CONTRADICTION": [], "NEUTRAL": []}
        for claim in claims:
            #get evidence for each claim
            evidence_list = get_evidence_for_claim(claim)

            st.write(f"### Claim: {claim}")

            for evidence in evidence_list:
                st.write(f"- Evidence: {evidence}")
                #verify claim against evidence
                results = verify_claim(claim, evidence)
                st.write(f"**Verification Scores: {results}**")

                #aggregate results for overall assessment
                for label, score in results.items():
                    aggregated_results[label].append(score)

            st.markdown("---")
        
        #average aggregated results across all claims and evidence
        average = {label: sum(scores)/len(scores) if scores else 0.0 for label, scores in aggregated_results.items()}
        st.write("### Aggregated Verification Scores: ", average)

        if average["ENTAILMENT"] > 0.35:
            st.success("Overall, the claims in the article are likely TRUE based on the evidence.")
        elif average["CONTRADICTION"] > 0.6:
            st.error("Overall, the claims in the article are likely FALSE based on the evidence.")
        else:
            st.info("Overall, the claims in the article are UNCERTAIN based on the evidence.")