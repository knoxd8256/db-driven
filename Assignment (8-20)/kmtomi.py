def unitChoice():
    unit1 = input("Enter your starting unit, mi or km. \n")
    if unit1 == "mi":
        distConv("mi")
    elif unit1 == "km":
        distConv("km")
    else:
        print("ERROR: Please enter mi or km.")
        unitChoice()
def distConv(unit):
    distance = float(input("Enter distance. \n"))
    if unit == "mi":
        finalDist = distance * 1.60934
        print("You entered", distance, "miles. That is equivalent to", round(finalDist, 2), "kilometers.")
    elif unit == "km":
        finalDist = distance * 0.621371
        print("You entered", distance, "kilometers. That is equivalent to", round(finalDist, 2), "miles.")
    else:
        return
unitChoice()
