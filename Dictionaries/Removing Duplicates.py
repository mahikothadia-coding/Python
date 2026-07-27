student_data = {
    "id1" : {"name" : "Mahi", "class" : "v", "Subject_integration":"Maths,Music,Science" },
    "id2" : {"name" : "Tom", "class" : "v", "Subject_integration":"Maths,Music,Science" }, 
    "id3" : {"name" : "Mahi", "class" : "v", "Subject_integration":"Maths,Music,Science" }, 
    "id4" : {"name" : "Sofia", "class" : "v", "Subject_integration":"Maths,Music,Science" }, 
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["Subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k,":",v)
