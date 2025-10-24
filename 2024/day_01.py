def similarity_score(data1, data2):
    data1.sort()
    data2.sort()
    score = 0
    i = 0
    for entry in data1:
        distance = abs(data1[i] - data2[i])
        score = score + distance
        i += 1
    return score

# Test Data
t1 = [3, 4, 2, 1, 3, 3]
t2 = [4, 3, 5, 3, 9, 3]

# Real Data
# with open("input01.txt") as f:
#     data = f.read().strip().splitlines()

# l1 = []
# l2 = []

# for line in data:
#     a, b = map(int, line.split())
#     l1.append(a)
#     l2.append(b)

sim = similarity_score(t1,t2)
print(sim)