def total_calc(bill_amount,tip_percentage):
    total = bill_amount * (1 + 0.01 * tip_percentage)
    total = round(total, 2)
    print(f"Please pay £{total}")

bill = float(input("Enter your total bill amount:  "))

tip = float(input("Enter the percentage amount you want to give us:  "))    
total_calc(bill, tip)