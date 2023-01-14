print("                   ***Grade Calculator***")
print("< Input your test scores (numerical form) to see your lowest, highest and average grades.")
print(" ")

def grade_calculator():
  name = input("Enter your name: ")
  grades = []
  for i in range(5):
    grade = int(input("Enter 5 test scores (one at a time): "))
    grades.append(grade)
  grades.sort()
  print("Grades: ", grades)
  print("")
  print("Lowest Grade: ", min(grades))
  print("Highest Grade: ", max(grades))
  average = sum(grades)/len(grades)
  print(name, "'s test average is: ", average)

grade_calculator()
