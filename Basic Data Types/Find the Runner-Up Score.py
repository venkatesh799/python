# Problem Statement  :  https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))   # Converting into set, so that we can        eliminate duplicates
    arr.remove(max(arr))   # Removing Highest score from list
    print(max(arr))   
