import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()
GOOGLE_FACT_CHECK_API_KEY = os.getenv("GOOGLE_FACT_CHECK_API_KEY")

def get_evidence_for_claim(claim):
    """
    Google Fact Check API to get evidence for a given claim.
    Returns a list of highly relevant evidence strings.
    Filters out irrelevant snippets based on keywords from the claim.
    Improves ranking by keyword match count.
    """

    url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={claim}&key={GOOGLE_FACT_CHECK_API_KEY}"
    response = requests.get(url)
    data = response.json()

    evidence_list = []
    keywords = [word.lower() for word in claim.split() if len(word) > 3]

    scored_snippets = []

    for item in data.get("claims", []):
        text = item.get("text", "")
        reviews = item.get("claimReview", [])
        if reviews:
            publisher = reviews[0].get("publisher", {}).get("name", "")
            snippet = f"{text} (Source: {publisher})"

            # count matching keywords
            match_count = sum(1 for k in keywords if k in snippet.lower())
            if match_count > 0:
                scored_snippets.append((match_count, snippet))

    # sort snippets by highest match count first
    scored_snippets.sort(reverse=True, key=lambda x: x[0])

    # remove duplicates and keep only snippets
    seen = set()
    for _, snippet in scored_snippets:
        if snippet not in seen:
            evidence_list.append(snippet)
            seen.add(snippet)

    # fallback if no relevant evidence found
    if not evidence_list:
        evidence_list.append("No relevant evidence found.")

    return evidence_list
