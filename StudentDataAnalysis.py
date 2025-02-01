def calcualte_highest_in_maths(Student_list):
    highest_marks_in_Maths = 0
    highest_marks_name = ''
    for student in student_list:
        if (student.get('Maths') > highest_marks_in_Maths):
            highest_marks_in_Maths = student.get('Maths')
            highest_marks_name = student.get('Name')
    print(f'The Highest scorer in maths is {highest_marks_in_Maths} by {highest_marks_name}')

def calcualte_highest_in_science(Student_list):
    highest_marks_in_Science = 0
    highest_marks_name = ''
    for student in student_list:
        if (student.get('Science') > highest_marks_in_Science):
            highest_marks_in_Science = student.get('Science')
            highest_marks_name = student.get('Name')
    print(f'The Highest scorer in Science is {highest_marks_in_Science} by {highest_marks_name}')

def calcualte_highest_in_social(Student_list):
    highest_marks_in_Social = 0
    highest_marks_name = ''
    for student in student_list:
        if (student.get('Social') > highest_marks_in_Social):
            highest_marks_in_Social = student.get('Social')
            highest_marks_name = student.get('Name')
    print(f'The Highest scorer in Social is {highest_marks_in_Social} by {highest_marks_name}')


student_1 = {'Name':'Tanmay', 'Maths': 50, "Science": 60, 'Social': 66}
student_2 = {'Name':'Dheeraj', 'Maths': 47, "Science": 87, 'Social': 58}
student_3 = {'Name':'Sooraj', 'Maths': 56, "Science": 45, 'Social': 67}
student_list = [student_1, student_2 , student_3]

calcualte_highest_in_maths(student_list)
calcualte_highest_in_science(student_list)



