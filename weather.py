answer = input("Is the weather good? Type 'Yes' or 'No' ")


step = 0
while step < 100:
    print(step)

    if answer == "Yes":
        step = step + 1
    else:
        break
