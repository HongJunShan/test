import csv

student_name = input("请输入学生的姓名：")
subjects = input("请输入科目，用逗号分割：").split(',')

grades = input("请输入成绩：")
grades_list = list(eval(grades))

avg_grade = sum(grades_list) / len(grades_list)
print("平均成绩为:"+str(avg_grade))

with open('score.csv', 'w') as file:
    writer = csv.writer(file)
    row = [student_name] + subjects + [avg_grade]
    writer.writerow(row)
