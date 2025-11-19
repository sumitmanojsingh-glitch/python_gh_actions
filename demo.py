menu_items=["lemon","ginger"]
customer_name=["sumit","sujeet"]

for index,order in enumerate(menu_items,start=1):
    print (f"Chai {index} : {order}")

for menu,customer in zip(menu_items,customer_name):
    print(f"chai {menu}: {customer}")