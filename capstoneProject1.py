'''
Name    : REMIR JOSEPH EKLOU
Project : Capstone Module 1
Course  : Data Science & Machine Learning
Title   : Penjualan Barang Toko
Client  : D'VERSE BOUTIQUE 
'''

import operator  

items = [
    {
        'ID':     1,
        'Name':  'Batik',
        'Stock':  45,
        'Cost':   175000,
        'Source': 'Local'
    },
    {
        'ID':     2,
        'Name':  'T-Shirt',
        'Stock':  55,
        'Cost':   105000,
        'Source': 'Import'
    },
    {
        'ID':     3,
        'Name':  'Jacket',
        'Stock':  85,
        'Cost':   115000,
        'Source': 'Local'
    },
    {
        'ID':     4,
        'Name':  'Jeans',
        'Stock':  35,
        'Cost':   195000,
        'Source': 'Import'
    },
    {
        'ID':     5,
        'Name':  'Chinos',
        'Stock':  95,
        'Cost':   180000,
        'Source': 'Local'
    }
]

# Fuction to show all available items 
def show_items() :
    if len(items) == 0 :
        print("All items data are not available")
    else :
        print("List of available items\n")
        print("|ID \t| Name \t\t| Stock | Cost(Rp) \t| Source")
        for i in range(len(items)) :
            print("|{} \t| {} \t| {} \t| {} \t| {}".format(items[i]['ID'], items[i]['Name'], items[i]['Stock'], items[i]['Cost'],items[i]['Source']))

# Fuction to search items 
def read_item() :
    while len(items) == 0 :
        print("All items data are not available")
        break

    else:
        while True:
            view_option = int(input('''
            =======================
            ======READ MENU========  

            1. Show all items data 
            2. Search item with ID 
            3. Back to main menu 
            ========================
            Choose one of the read menu for items search (1-3): '''))

            if view_option == 1 :
                show_items()

            elif view_option == 2 :
                item_search = int(input("Enter the ID of item: "))
                print("|ID \t| Name \t\t| Stock | Cost(Rp) \t| Source")
                for i in range(len(items)):
                        if items[i]["ID"] == item_search :
                            print("|{} \t| {} \t| {} \t| {} \t| {}".format(items[i]['ID'], items[i]['Name'], items[i]['Stock'], items[i]['Cost'],items[i]['Source']))
                            if items[i]["ID"] != item_search :
                                print("Item ID not available")
                        else:
                            continue

            elif view_option == 3 :
                break
        
            else:
                print("Invalid read menu option. Please try again")

# Function to add data to items based on user input 
def create_item() :
    
    get_values = operator.itemgetter("ID") # Method from operator module to get values based on key input
    list_values = list(map(get_values, items))
    
    while True: 

        input_ID = int(input("Enter the ID of item you wish to add : "))
        new_item = input_ID
            
        if new_item not in list_values :

            input_name =  input("Enter name of new item : ")
            input_stock=  int(input("Enter number of new item : "))
            input_cost=   int(input("Enter cost of new item : "))
            input_source= input("Enter source of new item : ")
            
            item_checker = input(f"Do you wish to continue adding the item ? (Yes/No): ")
                
            if item_checker != "Yes".lower():
                    break
            else:
                items.append({
                    "ID":     input_ID,
                    "Name":   input_name.capitalize(),
                    "Stock":  input_stock,
                    "Cost":   input_cost,
                    "Source": input_source.capitalize()})
                        
                show_items()
                break      
        
        else:
            print("This item is already available. It cannot be added again. Try another item ID")
            break

# Function to update values in list of items 
def update_item() :
    
    get_values = operator.itemgetter("ID") # Method from operator module to get values based on key input 
    list_values = list(map(get_values, items))
    
    update_stock = int(input('''
    =====================
    =====UPDATE MENU===== 

    1. Update item  
    2. Back to main menu 
    =====================
    Choose one of the update menu options (1-2): '''))

    if update_stock == 1 :
        show_items()
        
        update_item = int(input("Enter the ID of item you wish to update : "))

        while update_item in list_values :

            update_type = int(input('''
            ==================
            ===UPDATE FIELD=== 
            
            1. Name
            2. Stock 
            3. Cost 
            4. Source 
            ===================
            Enter field you wish to update (1-4) : '''))

            if update_type == 1 :
                new_name = input("Enter the new name : ")
                newName_checker = input(f"Do you wish to continue updating the item {update_item} name  >> {new_name} ? (Yes/No): ")

                if newName_checker != "Yes".lower():
                    break
                else:
                    items[update_item - 1]["Name"] = new_name.capitalize()
                    show_items()
                    break
            
            elif update_type == 2 :
                new_stock = input("Enter the new number of stock : ")
                newStock_checker = input(f"Do you wish to continue updating item {update_item} number of stock  >> {new_stock} ? (Yes/No): ")

                if newStock_checker != "Yes".lower():
                    break
                else:
                    items[update_item - 1]["Stock"] = new_stock.capitalize()
                    show_items()
                    break
            
            elif update_type == 3 :
                new_cost = input("Enter the new cost : ")
                newCost_checker = input(f"Do you wish to continue updating item {update_item} cost  >> {new_cost} ? (Yes/No): ")

                if newCost_checker != "Yes".lower():
                    break
                else:
                    items[update_item - 1]["Cost"] = new_cost
                    show_items()
                    break
            
            elif update_type == 4 :
                new_source = input("Enter the new source : ")
                newSource_checker = input(f"Do you wish to continue updating item {update_item} source  >> {new_source} ? (Yes/No): ")

                if newSource_checker != "Yes".lower():
                    break
                else:
                    items[update_item - 1]["Source"] = new_source
                    show_items()
                    break
            else:
                break

        else:
            print("The item ID you entered is not available.")
    
    while update_stock == 2:
        break

# Function to delete item
def delete_item() :
    show_items()

    get_values = operator.itemgetter("ID") # Method from operator module to get values based on key input
    list_values = list(map(get_values, items))
    
    input_del = int(input("Enter the item ID you wish to delete : "))
    while input_del in list_values : 
   
        del_checker = input(f"Do you wish to proceed with item {input_del} delete ? (Yes/No): ")
        if del_checker != "Yes".lower():
            break
        else:
            del items[input_del - 1]
            show_items()
            break
    
    else:
            print("The item ID you entered is not available.")


# Function to buy item
cart = []

def buy_item() :
    show_items()

    while True:
        item_ID = int(input("Enter the ID of item you wish to buy : "))
        item_qty = int(input("Enter the quantity you wish to buy : "))
        if(item_qty > items[item_ID - 1]["Stock"]) :
            print(f'Number of item requested not available. \nStock of {items[item_ID - 1]["Name"]} remaining {items[item_ID - 1]["Stock"]}')
        else :
            cart.append({
                "Name": items[item_ID - 1]["Name"], 
                "Qty":  item_qty, 
                "Cost": items[item_ID - 1]["Cost"], 
                "ID":   item_ID,
                "Source": items[item_ID - 1]["Source"]
                })
        
        print('Cart :')
        print("| Name   \t| Qty \t| Cost(Rp) \t| Source")
        for item in cart :
            print(f"| {item['Name']}    \t| {item['Qty']} \t| {item['Cost']} \t| {item['Source']}")
        buy_checker = input("Do you wish to buy something else ? (Yes/No) : ")
        if buy_checker == "No".lower() :
            break
    
    print("***Shopping List***")
    print("| Name   \t| Qty \t| Unit Cost(Rp) | Total Cost(Rp)")
    total_cost = 0
    for item in cart :
        print(f"| {item['Name']}    \t| {item['Qty']} \t| {item['Cost']} \t| {item['Qty'] * item['Cost']}")
        total_cost += item['Qty'] * item['Cost']   
    
    while True :
        print(f"Total amount to be paid = Rp {total_cost}")
        
        cash_paid = int(input('Enter amount of cash paid : '))
        if cash_paid > total_cost :
            print(f"Thank you. Transaction complete. \nYour balance is : Rp {cash_paid - total_cost}")
            for item in cart :
                items[item['ID']]['Stock'] -= item['Qty']
            cart.clear()
            break
        elif cash_paid == total_cost :
            print('Transaction completed. Thank you.')
            for item in cart :
                items[item['ID']]['Stock'] -= item['Qty']
            cart.clear()
            break
        else :
            remaining_cash = total_cost - cash_paid
            print(f"Cash payment remaining : Rp {remaining_cash}")


while True:
    user_input = int(input('''
    ===========================
    WELCOME TO D'VERSE BOUTIQUE
    ===========================
    Select you identity:
    1. Staff
    2. Customer 
    3. Exit Program
    =========================== 
    Enter a login menu (1-3): 
    '''))
    
    while user_input == 1:
        
            staff_menu = int(input('''
            ***You are logged in as boutique staff***
            ======================
            Main Staff Menu :
            1. See available items 
            2. Add data to items
            3. Update items data
            4. Delete items data 
            5. Exit program 
            =======================
            Enter a menu option (1-5) : 
            '''))
            
            if staff_menu == 1 :
                read_item()
            elif staff_menu == 2 :
                create_item()
            elif staff_menu == 3 :
                update_item()
            elif staff_menu == 4 :
                delete_item()
            elif staff_menu == 5 :
                break
            else:
                print("The menu you entered is not available. Try again")

    while user_input == 2 :
        customer_menu = int(input('''
        ======================
        Customer Menu :
        1. See available items  
        2. Buy Items 
        3. Back to home page 
        =======================
        Enter a menu option (1-3): 
        '''))

        if customer_menu == 1 :
            show_items()
        elif customer_menu == 2 :
            buy_item()
        elif customer_menu == 3 :
            break
        else:
            user_input = int(input('''
            =======================
            Customer Menu : 
            1. See available items  
            2. Buy Items 
            3. Back to home page 
            =======================
            Enter a menu option (1-3): 
            '''))    

    else:
        break