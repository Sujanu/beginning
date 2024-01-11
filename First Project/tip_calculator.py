# creating tip calculator

# bill 
tb = input("What was the total bill ? ")

# tip percentage
tipp = input("What percentage tip would you like to give ? ")

# numbers of people
pn = input("How many person to spill the bill ?")

# tip calculation
tp = (float(tb) * float (tipp)) / 100

#total bill
total_bill = float(tb) + float (tp)

# each person contribution
db = round(float(total_bill) / float(pn),2)
print("Calculated")

print(f" your  bill is {tb} \n your tip with {tipp} percentage is {tp} \n your final bill is {total_bill} \n each person contribution is {db}")
