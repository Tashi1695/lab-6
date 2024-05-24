num_student = int(input("enter no. students:"))
i = 1
while i <= num_student:
    total_grade = 0
    num_subjects = int(input(f"enter no. of subject for student {i}:"))

    for j in range (1, num_student +1):
        grade = float(input(f"enter subject {j} grade for student {i}:"))
        total_grade += grade

    average_grade = total_grade / num_subjects
    print(f"average grade for student {i} : {average_grade}")
    i += 1