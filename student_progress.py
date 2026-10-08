name = input("Enter Student name : ")
subjects = ['Maths', 'English', 'Science', 'Computer', 'History']

marks = []

for subject in subjects:
  mark = int(input(f"Enter {subject} marks: "))
  marks.append(mark)


total = sum(marks)
average = total / len(marks)

if average >= 90:
  grade = "A"

elif average >= 80:
  grade = "B"

elif average >= 70:
  grade = "C"

elif average >= 60:
  grade = "D"

else:
  grade = "F"

if average >= 40:
  result = "PASS"
else:
  result = "FAIL"


print("------ STUDENT RESULT -----")
print("Name : ", name)
print("Total : ", total)
print("Average : ", average)
print("Grade : ", grade)
print("Result : ", result)

