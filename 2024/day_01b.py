def similarity_score(data1, data2):
    score = 0
    for entry in data1:
        occurrance = data2.count(entry)
        score = score + occurrance * entry
    return score

# Test Data
t1 = [3, 4, 2, 1, 3, 3]
t2 = [4, 3, 5, 3, 9, 3]

similarity = similarity_score(t1, t2)
print(similarity)