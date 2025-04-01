#lets say welcome 
print("Welcome to the bill calculator")

cost = float(input(("What is the total cost? $")))

percentage = float(input("What is the percentage of tip? %"))

people = int(input("How many people the price divide between? "))

tip = round(((percentage/100)*cost), 2)

total =(cost + tip)

per_person = float(total)/float(people)

final = (round(per_person, 2))
print(f"the total cost is ${cost} without tip")
print(f"the tip is ${tip}" )
print(f"total cost is ${total}")
print(f"{people} is the number of people who share the cost.")
print(f"each person have to pay {final} $")



#Today, I added a new feature to the my Day #2 project it calculates bill with persentage.


#I implemented the round() function to round numbers to a specific decimal place.





