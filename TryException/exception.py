
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't have 0 as denominator")
except ValueError as e:
    print(e)
    print("You need to use only numbers in this operation")
except Exception as e:
    print(e)
    print("something went wrong")
else: #If none of the exception been called, the else statment will be execute
    print(result)
finally:
    print("This will always execute")