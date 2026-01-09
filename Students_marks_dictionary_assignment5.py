marks = {"Suraj":85,"Venkat":77,"Manikanta":91,"Mukesh":88}

list1 = marks.keys()

name = input ("Enter student's name:")
if name in list1:
    print(f"{name}'s marks:{marks[name]}")

else:
    print("Student not found")