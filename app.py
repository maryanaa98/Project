import csv
from typing import OrderedDict
courier_list=[{"name": "Maryan","phone":71111111},{"name": "Beyonce","phone":7222222},{"name": "Patrick","phone":7333333},{"name": "Megha","phone":74444444}]
product_list = [{"id":1,"item":"Coffee","price":3.00}, {"id":2,"item":"Tea","price":2.50},{"id":3,"item":"Banana Smoothie","price":4.50},{"id":4,"item":"Fanta","price":2.50},{"id":5,"item":"Orange Juice","price":1.50}]
live_orders=[{"Customer Name":"John","Customer Address":'Unit 2,12 Main Street, LONDON, WH1 2ER',"Customer Phone":7123456789,"Courier":2,"Order Status":'preparing',"Order items":'1,2,3'}]
order_keys = ["Customer Name","Customer Address", "Customer Phone","Courier","Order Status","Order items"]
order_status = ["preparing","out for delivery","delivered"]
order_dict = {"Customer_name":None,"Customer_address":None,"Customer_phone":None,"courier":None,"order_status":None}
counter = 0 

def save_menu():
    try:
            with open('product.csv', 'a', newline='')  as output_file:
                keys = product_list[0].keys()
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(product_list)
            with open('courier.csv', 'a', newline='')  as f:
                keys = courier_list[0].keys()
                dict_writer = csv.DictWriter(f, keys)
                dict_writer.writeheader()
                dict_writer.writerows(courier_list)
            with open('orders.csv', 'a', newline='')  as f:
                keys = live_orders[0].keys()
                print(live_orders)
                dict_writer = csv.DictWriter(f, keys)
                dict_writer.writeheader()
                dict_writer.writerows(live_orders)
                
            print("Added and saved to the list")
    except FileNotFoundError:
        print('Doesnt exist')
        print("Exiting, Goodbye!") 

def product_menu():  
      while True: 
        product_menu_option = int(input('Product Menu\n 0:Exit \n 1: To view all product \n 2: Create a new product \n 3: To update an existing product \n 4: Delete a product '))

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
            
def courier_menu():
     
    while True:           
        courier_menu_option = int(input('Courier Menu\n 0: Back to Main menu \n 1: To view couriers available \n 2: To add a new courier \n 3: To update a courier \n 4: To delete a courier'))
         
        if courier_menu_option == 1:
          print(courier_list)

        elif courier_menu_option == 1:
          for i in courier_list:
            print(i)
              
        elif courier_menu_option== 2:
          new_courier = input("What would you like to add?\n")
          new_item_value = input("what is the number")
          d = {"name":new_courier,"phone":new_item_value}
          courier_list.append(d)
          print(courier_list)
          
        elif courier_menu_option == 3:
          update_courier = int(input(' Please enter the number of the courier you wish to update: '))
          print(f' You have chosen {courier_list[update_courier]}: ')
          new_replacement_item =input("What would you like it to be\n") 
          courier_list[update_courier] = {new_replacement_item}
          print(courier_list)
                   
        elif courier_menu_option == 4:
          delete = int(input("what is the index?\n"))
          del courier_list[delete]
          print(courier_list)

        elif courier_menu_option == 0:
          break

        else:
            print("incorrect Choice!")

def live_order_menu():
     while True:
        order_menu_option = int(input('Order Menu\n 0: Back to Main menu \n 1: To view live order \n 2: To add orders \n 3: To update order status \n 4: To update order \n 5: To delete order'))

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
          for (i, item) in enumerate(courier_list, start=0):
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

        elif order_menu_option == 0:
          break

        else:
            print("incorrect Choice!")
