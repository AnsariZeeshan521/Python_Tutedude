StudentMap ={"John":50,"Max":80,"Elaine":70,"Richard":55}

student = input("Enter the student's name: ")

if student in StudentMap:
    print(f"{student}'s marks: {StudentMap[student]}")
else:
    print("Student not found.")