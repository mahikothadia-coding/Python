test_dict = {"Codingal": 2, "is":2, "best": 2, "for": 2, "coding": 1}

print("The original dictionary:"+ str(test_dict))

M = 2

count = 0
for key in test_dict:
    if test_dict[key] == M:
        count = count + 1

print("Frequency of M is : " + str(count))