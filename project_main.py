from test import save_menu, product_menu, courier_menu, live_order_menu

print('Welcome to Maryans Cafe')
while True:
    menu = int(input("What menu would you like to access?\n Press 0 EXIT\n Press 1 To enter the product menu\n Press 2 To enter courier menu\n Press 3 to create, check orders and change status\n"))
    print(menu)
    if menu == 0:
        save_menu
    elif menu == 1:
        product_menu()
    elif menu == 2:
        courier_menu()
    elif menu == 3:
        live_order_menu()