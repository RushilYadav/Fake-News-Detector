#manual testing

def get_evidence_for_claim(claim):
    """
    Returns a list of evidence snippets for a claim.
    For now, we can return a hardcoded example.
    """
    sample_evidence = {
        "NASA announced a mission to Europa": 
        "NASA has confirmed plans to send a robotic mission to explore Europa in 2026."
    }
    return [sample_evidence.get(claim, "No evidence available.")]
