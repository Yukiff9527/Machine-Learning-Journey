
# Lesson 05: Return values

def classify_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 60:
        return "Passed"
    else:
        return "Needs improvement"


scores = [95, 78, 52]

for score in scores:
    result = classify_score(score)
    print(score, result)
