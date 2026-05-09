grand_total = 0.0
order_summary = []
running = True

while running:
    print("\n" + "="*30)
    print("      CAMPUS CAFÉ MENU")
    print("="*30)
    print("1. Coffee                       $3.50")
    print("2. Sandwich                     $6.00")
    print("3. Salad                        $5.50")
    print("4. Combo (Sandwich + Coffee)    $8.00")
    print("5. Checkout & Exit")
    print("="*30)
    
    choice = input("Please select an option (1-5): ")

    if choice == "1":
        item_price = 3.50
        size = input("Choose a size small medium or large): ").strip().lower()
        if size == "medium":
            item_price += 1.00
        elif size == "large":
            item_price += 2.00
        elif size == "small":
            pass 
        else:
            print("please pick small medium or large.")
        grand_total += item_price
        order_summary.append(f"${item_price:.2f}")
        
    elif choice == "2":
        item_price = 6.00
        cheese = input("would you like to add cheese? (yes/no): ").strip().lower()
        if cheese == "yes":
            item_price += 0.75
            order_summary.append(f"${item_price:.2f}")
        else:
            order_summary.append(f"${item_price:.2f}")
            grand_total += item_price

    elif choice == "3":
        item_price = 5.50
        valid_dressings = ["ranch", "italian", "vinaigrette", "none"]
        dressing = input("Please select dressing (Ranch, Italian, Vinaigrette, None): ").strip().lower()
        if dressing not in valid_dressings:
            print("Please select a dressing or select none.")
            grand_total += item_price
        order_summary.append(f"${item_price:.2f}")

    elif choice == "4":
        item_price = 8.00 
        size = input("Choose a size small medium or large): ").strip().lower()
        if size == "medium":
            item_price += 1.00
        elif size == "large":
            item_price += 2.00
        else:
            size = "small"
            cheese = input("Would you like to add cheese to sandwich? (yes/no): ").strip().lower()
        if cheese == "yes":
            item_price += 0.75
        grand_total += item_price
        order_summary.append(f"${item_price:.2f}")

    elif choice == "5":
        running = False
        print("\n" + "="*30)
        print("      FINAL ORDER SUMMARY")
        print("="*30)
        if not order_summary:
            print("No items ordered.")
        else:
            for item in order_summary:
                print(f" {item}")
            print("=" * 30)
            print(f"GRAND TOTAL: ${grand_total:.2f}")
        print("="*30)
        print("Thank you for dining with us!")
    else:
        print("Invalid menu choice. Please enter a number between 1 and 5.")
