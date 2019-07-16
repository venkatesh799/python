a=10
b=10
try:
    print(a/b)
    k=int(input("Enter a Integer"))
    print(k)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("Invalid Number")
finally:
    print("I'm here")
