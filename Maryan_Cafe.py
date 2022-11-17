import csv

couriers = [{"name": "Maryan","phone":71111111111},{"name": "Beyonce","phone":72222222222},{"name": "Patrick","phone":73333333333},{"name": "Megha","phone":74444444444}]
product_list = []
# product_list = [{"item":"Coffee","price":3.00}, {"item":"Tea","price":2.50},{"item":"Banana Smoothie","price":4.50},{"item":"Fanta","price":2.50},{"item":"Orange Juice","price":1.50}]
order_keys = ["Customer Name","Customer Address", "Customer Phone","Courier","Order Status","Order items"]
live_orders = []
order_status = ["preparing","out for delivery","delivered"]
order_dict = {"Customer_name":None,"Customer_address":None,"Customer_phone":None,"courier":None,"order_status":None}
counter = 0 
while True:
    print('')
    print('MAIN MENU')
    print('0: EXIT')
    print('1: To enter the products Menu')
    print('2: To enter the couriers Menu')
    print('3: To enter the order Menu')

    print('')
    selection = int(input('What is your selection: '))
    if selection== 0:
        break

    if selection == 1: 
      while True: 
        print('')
        print('') 
        print('MAIN MENU')
        print('0: Return back the MAIN MENU.')
        print('1: To Print all products')
        print('2: To Create a new product')
        print('3: To Update an existing product')
        print('4: To Delete a product')
        print('')

        product_menu_option = int(input(''))

        if product_menu_option == 1:
          print (product_list)
  
         
        elif product_menu_option == 2:
          new_item = input("What would you like to add?\n")
          new_item_value = input("what is the price")
          d = {"item":new_item,"price":new_item_value}
          product_list.append(d)
          print(product_list) 

        elif product_menu_option == 3:
          for (i, item) in enumerate(product_list, start=0):
            print(i, item)
          new_index = int(input("What index\n"))
          new_item = input("What would you like to add?\n")
          new_item_value = input("what is the price\n")
          j = {"item":new_item,"price":new_item_value}
          product_list[new_index] = j
          print(product_list)

        elif product_menu_option == 4:
          delete = int(input("what is the index?\n"))
          del product_list[delete]
          print(product_list)

        elif product_menu_option == 0:
          break

        else:
            print("incorrect Choice!")

    elif selection == 2:
      while True:
        print ("\n0.Back to main menu")
        print ("1. To couriers available")
        print ("2. To add a new courier") 
        print ("3. To update a courier")
        print ("4. To delete a courier")
                      
        courier_menu_option = int(input(''))
         
        if courier_menu_option == 1:
          print(couriers)

        elif courier_menu_option == 1:
          for i in couriers:
            print(i)
              
        elif courier_menu_option== 2:
          new_courier = input("What would you like to add?\n")
          new_item_value = input("what is the number")
          d = {"name":new_courier,"phone":new_item_value}
          couriers.append(d)
          print(couriers)
          
        elif courier_menu_option == 3:
          update_courier = int(input(' Please enter the number of the courier you wish to update: '))
          print(f' You have chosen {couriers[update_courier]}: ')
          new_replacement_item =input("What would you like it to be\n") 
          couriers[update_courier] = {new_replacement_item}
          print(couriers)
          
          
        elif courier_menu_option == 4:
          delete = int(input("what is the index?\n"))
          del couriers[delete]
          print(couriers)

        elif courier_menu_option == 0:
          break

        else:
            print("incorrect Choice!")

    elif selection == 3:
      while True:
        print("\n0. Back to main menu")
        print("1. To view live order")
        print("2. To add orders")
        print("3. To update order status")
        print("4. To update order")
        print('5. To delete order')
        
        order_menu_option = int(input(''))

        if order_menu_option ==1:
          print(live_orders)
        
        
        elif order_menu_option == 2:
          current_order = dict(order_dict)    
          customer_name =input("What is the name?\n")
          customer_address =input("What is the address?\n")
          customer_phone =input("What is the phone number?\n")
          current_order["Customer_name"] = customer_name
          current_order["Customer_address"] = customer_address
          current_order["Customer_phone"] = customer_phone
          print("You've added")
          print(current_order)
          for (i, item) in enumerate(couriers, start=0):
            print(i, item)
            
          current_order["courier"] = input("What courier shall be assigned?\n")
          current_order["order_status"] = "Preparing"
          print("order status set to preparing")
          print(order_dict)
            #Create a list which stores item numbers so a courier can take more than one item
          for (i, item) in enumerate(product_list, start=1):
            print(i, item)
          L = [int(x) for x in input("The Order the courier is taking with a comma then a space please, very important pls pls \n").split(', ')]
          current_order["Order items"] = L
          live_orders.append(current_order)
          print("You've added")
          print(live_orders)
                
        elif order_menu_option == 3: #update existing order status
          for (i, item) in enumerate(live_orders, start=0):
           print(i, item)
          for (i, item) in enumerate(order_status, start=0):
            print(i, item)
          order_index = int(input("What is the order number\n"))
          order_status_index =int(input("what is the updated status\n"))
          live_orders[order_index]["order_status"] = order_status[order_status_index]
          print(live_orders[order_index])
          
        elif order_menu_option == 4: #update whole order
          for (i, item) in enumerate(live_orders, start=0):
             print(i, item)
          dict_index = int(input("what is the index\n"))
          live_orders[dict_index]['Customer_name'] = input('Who is the new customer?') or live_orders[dict_index]['Customer_name']
          live_orders[dict_index]['Customer_address'] = input('address?') or live_orders[dict_index]['Customer_address']
          live_orders[dict_index]['Customer_phone'] = input('What is the new number?') or live_orders[dict_index]['Customer_phone']
          live_orders[dict_index]['courier'] = input('What is the new courier?') or live_orders[dict_index]['courier']
          live_orders[dict_index]['order_status'] = input('What is the order status?') or live_orders[dict_index]['order_status']
            #Add a product
          print(live_orders[dict_index])
          continue
        elif order_menu_option == 5: #delete order
            for (i, item) in enumerate(live_orders, start=0):
                print(i, item)
            delete_input = int(input("What order would you like to delete?\n"))
            del(live_orders[delete_input])
            print(live_orders)
            continue
    