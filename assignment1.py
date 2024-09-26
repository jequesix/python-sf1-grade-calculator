def calculate_weighted_average(grades: list[float], weights: list[float]) -> int:
  avg = 0

  # apply each weight to its corresponding grade 
  avg += grades[0] * weights[0]
  avg += grades[1] * weights[1]
  avg += grades[2] * weights[2]
  avg += grades[3] * weights[3]
  avg += grades[4] * weights[4]
  avg += grades[5] * weights[5]

  return round(avg)


# grade assignments based on their completion state
def grade_quantitative_assignment(num_completed: int) -> float:
  if num_completed > 6:
    grade = 100
  else:
    grade = (num_completed / 6) * 100

  return grade


# retrieve grades from user and output them in a list
def grades_input() -> list[float]:
  # list of grades (in percentage)
  grades = []

  # quantitative assignments (labs and quizzes)
  grades.append(grade_quantitative_assignment(int(input("Enter the number of labs completed: "))))
  grades.append(grade_quantitative_assignment(int(input("Enter the number of quizzes completed: "))))

  # numbered assignments
  assignment_1_grade = int(input("Enter grade for Assignment 1: "))
  assignment_2_grade = int(input("Enter grade for Assignment 2: "))
  assignment_3_grade = int(input("Enter grade for Assignment 3: "))
  assignment_4_grade = int(input("Enter grade for Assignment 4: "))

  # sum is used to emulate multiple list elements into 1 element, making is shorter
  # does not alter the final result
  grades.append(assignment_1_grade + assignment_2_grade + assignment_3_grade + assignment_4_grade)

  # midterm assignments
  midterm_1_grade = int(input("Enter grade for Midterm 1: "))
  midterm_2_grade = int(input("Enter grade for Midterm 2: "))

  # sum is used to combine multiple list elements into 1 element, making is shorter
  # does not alter the final result
  grades.append(midterm_1_grade + midterm_2_grade)

  # final exam
  grades.append(int(input("Enter grade for Final Exam: ")))

  # preparation
  grades.append(int(input("Enter grade for Midterms and Final Preparation: ")))

  return grades


grades = grades_input()

# weights are separated from the inputs for modularity's sake
avg = calculate_weighted_average(grades, [0.2, 0.15, 0.04, 0.125, 0.18, 0.06])

# display weighted average on the screen
print("Your grade is:", avg)
