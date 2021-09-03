# Problem Statement :  https://www.hackerrank.com/challenges/nested-list/forum

data = []
for _ in range(0, int(input())):
    data.append([input(), float(input())])
second_highest = sorted(list(set([score for name, score in data])))[1]
print('\n'.join([a for a,b in sorted(data) if b == second_highest]))
