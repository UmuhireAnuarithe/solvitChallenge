def calculate(students, name):
    marks = students[name]
    average = sum(marks) / len(marks)
    return '%.2f' % average

students = {
    'John': [67, 68, 69],
    'Jane': [70, 71, 72],
    'Jim': [73, 74, 75]
}

name = 'Jane'
average_marks = calculate(students, name)
print(f'The average marks for {name} is: {average_marks}')
 
