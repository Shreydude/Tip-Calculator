print("Welcome to tip calculator!")
bill=float(input("What was the total bill?$"))
tip=float(input("How much tip would you like to give?10,12 or 15?"))
people=int(input("How many people to split the bill?"))
tipindecimal=(tip/100)+1 #to convert tip percentage to decimal
split=(bill/people)*tipindecimal
finalamt=round(split, 2)

print(f"Each person has to pay ${finalamt}")
