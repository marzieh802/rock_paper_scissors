students_data = [
    ("ali", 18, "python"),
    ("sara", 11, "git"),
    ("reza", 15, "python"),
    ("neda", 9, "linux"),
    ("mina", 17, "git"),
    ("mahdi", 10, "git"),

]

result = {}
all_skills = {x[2] for x in students_data}
for name, grade, skills in students_data:
    # all_skills.add(skills)
    result.update({name: "pass" if grade >= 10 else "fail"})
    # if grade < 10:
    #     result.update({name: "fail"})
    #     print(f"{name} not accepted")
    # else:
    #     result.update({name: "pass"})
    #     print(f"{name} accepted")
print(all_skills)
print(result)
