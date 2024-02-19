"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names 
alphabetically and print each name on a new line.
Example
The ordered list of scores is , so the second lowest score is . There are two students
 with that score: . Ordered alphabetically, the names are printed as:
"""
if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print(
    '\n'.join(sorted([name for name, score in alist if score == second_highest])))

# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name, score])
#     print(students)

#
