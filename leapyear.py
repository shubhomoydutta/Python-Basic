year=int(input("Give me your year : "))
if year%100==0 and year%400==0:
    print(f"Your given {year} is a leapyear.")
elif year%100!=0 and year%4==0:
    print(f"Your given {year} is a leapyear.")
else:
    print(f"Your given {year} is not a leapyear.")