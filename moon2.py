def moon_weight(weight, increase, year):
    year = year + 1
    for x in range(1,year):
        weight = weight + increase
        moon = weight * 0.165
        moon = float(moon)
        print("Your weight on the moon in year %s is %s " % (x, moon))
