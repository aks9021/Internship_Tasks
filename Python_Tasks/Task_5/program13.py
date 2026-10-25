#Nested Lists

#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Get unique grades and sort them
    grades = sorted(set(student[1] for student in students))

    # Find the second lowest grade
    second_lowest = grades[1]

    # Get names of students having the second lowest grade
    names = sorted(
        student[0] for student in students
        if student[1] == second_lowest
    )

    # Print names alphabetically
    for name in names:
        print(name)