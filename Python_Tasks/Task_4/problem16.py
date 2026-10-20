#Nested Lists
#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # Step 1: Extract unique grades and sort them in ascending order
    grades = sorted(list(set([student[1] for student in students])))
    
    # Step 2: Identify the second lowest grade
    second_lowest = grades[1]
    
    # Step 3: Collect the names of all students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest]
    
    # Step 4: Sort names alphabetically and print each on a new line
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)