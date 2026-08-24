test_score = {"Jess" : 56, "Amy" : 89 , "Tom" :26, "Ben" : 87, "Lia" : 98 }

total = 0

for score in test_score.values():
    total = total + score

average = total / len(test_score)

print("Class Average: ",average)

top_student = max(test_score,key=test_score.get)
bottom_student = min(test_score,key=test_score.get)

print("Top student: ", top_student , "-" , test_score[top_student])
print("Bottom student: ", bottom_student , "-" , test_score[bottom_student])

name = input("Enter student name:  ")
score = test_score.get(name)

if score is not None:
    print(name, "'s score is ", score)
else:
    print("student not found.")    