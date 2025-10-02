from checker import get_evidence_for_claim
from verify import verify_claim

claim = "Donald Trump won the 2016 US presidential election"

evidence_list = get_evidence_for_claim(claim)
print("Evidence found:")
for e in evidence_list:
    print("-", e)

for evidence in evidence_list:
    results = verify_claim(claim, evidence)
    print("\nClaim:", claim)
    print("Evidence:", evidence)
    print("Verification Scores:", results)
