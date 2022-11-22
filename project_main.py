import os
import csv
from mini_project_app import product_list,courier_list,live_orders,write_file,read_file, product_menu, courier_menu, live_order_menu

print('Welcome to Maryans Cafe')

while True:
    menu = int(input("What menu would you like to access?\n Press 0: EXIT\n Press 1: To enter the product menu\n Press 2: To enter courier menu\n Press 3: to create, check orders and change status\n"))
    if menu == 0:
       print("Goodbye, see you next time")
       write_file('products.csv', product_list)
       write_file('courier.csv', courier_list)
       write_file('orders.csv', live_orders)
       exit()
    elif menu == 1:
        product_menu()
    elif menu == 2:
        courier_menu()
    elif menu == 3:
        live_order_menu()
    else:
     print('Incorrect choice!')
   