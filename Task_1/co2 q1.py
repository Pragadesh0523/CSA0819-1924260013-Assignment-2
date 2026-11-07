units = int(input())
ration = input()
age = int(input())

if units <= 100:
    print("Full Subsidy")
elif 101 <= units <= 200 and ration == "yes":
    print("Partial Subsidy")
elif 101 <= units <= 200 and ration == "no":
    print("No Subsidy")
elif units > 200 and age > 80:
    print("Senior Citizen Subsidy")
else:
    print("No Subsidy")
