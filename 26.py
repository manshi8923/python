try:
    age=int(input('age: '))
    income=200
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:
    print("Invalid Error")

