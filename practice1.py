# list and tuple
user_info = ("person1", 100)
shopping_list = [
    ("milk", 30),
    ("meat", 250),
    ("braed", 15),
    ("cheese", 120),
    ("apple", 45)
]

expensive_items = []
for name, price in shopping_list:
    if price > user_info[1]:
        expensive_items.append(name)
    else:
        print("it is not more than 100")
print(expensive_items)
