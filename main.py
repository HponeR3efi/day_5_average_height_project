# Day 5 Average Height Project

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights = 0
for heights in student_heights:
  total_heights += heights

students_ammount = 0
for students in student_heights:
  students_ammount += 1

calc_average_height = total_heights / students_ammount

print(int(calc_average_height))




