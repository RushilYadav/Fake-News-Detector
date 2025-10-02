from transformers import pipeline

#Load NLI model for verification
nli_model = pipeline("text-classification", model="roberta-large-mnli", return_all_scores=True)

def verify_claim(claim, evidence):
    """
    Verify a claim against provided evidence using an NLI model.
    Returns a dictionary with entailment, contradiction, and neutral scores.
    """
    text = evidence + " </s></s> " + claim
    scores = nli_model(text)[0]
    return {score['label']: round(score['score'], 3) for score in scores}