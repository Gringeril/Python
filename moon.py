weight = input("What is your weight? ")
weight = int(weight)


year = 0
while year < 15:
    weight = weight + 1
    year = year + 1
    moon = weight * 0.165
    moon = float(moon)
    print("Your weight on the moon in year %s is %s " % (year, moon))
