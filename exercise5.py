scores = [85,92,78,90,65]
print(len(scores))
print(scores[0])
print(scores[4])
scores.append(88)
for score in scores:
    print("score:",{score})
for score in scores:
    if score>=70:
        print(score,"- pass")
    else:
        print(score, "-fail")
