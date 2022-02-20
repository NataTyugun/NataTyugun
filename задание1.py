answer1 = input("Is it rainy?").lower()
if answer1 == "yes":
    answer2 = input("Is it windy?").lower()
    if answer2 == "yes":
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy yor day")
