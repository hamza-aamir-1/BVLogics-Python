# implement logical AND, OR, NOT operators


# determine if a given year is a leap year
year = input("Enter year: ")
if(int(year) % 4 == 0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")