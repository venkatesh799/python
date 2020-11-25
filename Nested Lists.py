# Problem Statement  :  https://www.hackerrank.com/challenges/nested-list/problem

 """
 Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example : records = [ ["chi",20.0], ["beta",50.0] , ["alpha" , 50.0] ]

The ordered list of scores is [20.0,50.0] , so the second lowest score is 50.0. There are two students with that score: ["beta" , "alpha"] . Ordered alphabetically, the names are printed as:

Output :
        alpha
        beta
        
"""

d={}
for _ in range(int(input())):
    name = input()
    grade = float(input())
    d[name] = grade
grades = d.values()
grades2 = sorted(list(set(grades)))[1]
second = []
for key,value in d.items():
    if value == grades2:
        second.append(key)
second.sort()
for x in second:
    print(x)
