import os
from dotenv import load_dotenv
import requests

#Load environment variables from .env file
load_dotenv()
GOOGLE_FACT_CHECK_API_KEY = os.getenv("GOOGLE_FACT_CHECK_API_KEY")

def get_evidence_for_claim(claim):
    """
    Google Fact Check API to get evidence for a given claim.
    Returns a list of evidence strings.
    Filters out irrelevant snippets based on keywords from the claim.
    """

    #construct API request URL
    url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={claim}&key={GOOGLE_FACT_CHECK_API_KEY}"

    response = requests.get(url)

    #parse JSON response
    data = response.json()

    evidence_list = []

    #extract relevant evidence from response
    for item in data.get("claims", []):
        text = item.get("text", "")
        reviews = item.get("claimReview", [])
        if reviews:
            publisher = reviews[0].get("publisher", {}).get("name", "")
            snippet = f"{text} (Source: {publisher})"

            keywords = [word for word in claim.split() if len(word) > 3]
            if any(keyword.lower() in snippet.lower() for keyword in keywords):
                evidence_list.append(snippet)
    
    #if no evidence found, return a default message
    if not evidence_list:
        evidence_list.append("No relevant evidence found.")

    return evidence_list