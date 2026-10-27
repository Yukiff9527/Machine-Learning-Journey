
# Lesson 03: Conditional statements

scores = [95, 78, 52]

for score in scores:
    if score >= 90:
        print(score, "Excellent")
    elif score >= 60:
        print(score, "Passed")
    else:
        print(score, "Needs improvement")
