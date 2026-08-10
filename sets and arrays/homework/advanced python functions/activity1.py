items = ["pencil", "earaser", "notebook","sharpener" , "glue"]
stock_counts = [26,0,5,12,0]

inventory = {item: count for item,count in zip (items, stock_counts) }
print("Full inventory:" , inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("Items in stock ; " , in_stock_items)

chosen_item = input("Which school stationary would you like to buy?")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock!!")

    exit()

prices = [2,5,12,6,8]
markup = int(input("Enter thr markup amount to add to every price :  "))


marked_up_prices = list(map(lambda p:p + markup, prices))
print("Marked up prices: " , marked_up_prices)

item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("Price of ", chosen_item,"after markup:" , chosen_price)


inventory[chosen_item] =inventory[chosen_item] -1
print(chosen_item, "PURCHASED! Remaining stock: ", inventory[chosen_item])

print("======School inventory checker======")
print("Item Bought :", chosen_item)
print("Price Paid:  ", chosen_price)
print("updated Inventory: " , inventory)
print("======================================")