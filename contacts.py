contacts = {
    "number":4,
    "students":
    [
        {"name":"Umi Ikem", "email":"umy.ikem@gmail.com"},
        {"name":"Los Sanchez", "email":"los.sanchez@gmail.com"},
        {"name": "Lebron James", "email":"lebron.james@gmail.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])