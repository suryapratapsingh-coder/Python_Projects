menu ={
    'Pizza':50,
    'Pasta':60,
    'Salad':40,
    'Coffee':80,
    'Burger':70
}

#Greet

print("Welcome to Shyam Restaurent")
print("Pizza: Rs50\nPasta: Rs60\nSalad: Rs40\nCoffee:Rs80\nBurger:Rs70")

order_total = 0

item_1 = input("Enter The Name Of Item You Want To Order")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your Item {item_1} Has Been Added To your Order")
else:
    print(f"Ordered Item {item_1} is Not Available Yet !")

another_order = input("Do You Want To Another Item ? (Yes/No)")       

if another_order == "Yes":
    item_2 = input("Enter The  Name Of Another Item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2}Has Been Added To Order")

    else:
        print(f"Ordered Item {item_2} Is Not Available!")

print(f"The Total Amount Of Item Is To Pay {order_total}")

pri
