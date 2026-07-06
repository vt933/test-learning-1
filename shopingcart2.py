#shopinglist.py

items=[]
features1=("1.Add items",
          "2.Remove items",
          "3.View cart",
          "4.exit",
          "5.clear cart",
          "6.Search item"
)          

while True:
    for featurex in features1:
        print(featurex)
    user_input=int(input("enter the feature you want to perform as (1,2,3,4,5,6)"))
    if user_input==1:
        item_name=input("enter the name of item you like")
        items.append(item_name)
        print()
    if user_input==2:
        remove_item=input("remove the item you would like to remove")
        if remove_item in items:
           print(f"item has been removed{remove_item}")
           items.remove(remove_item)
        else:
         print("item is not in list")
        print()
    elif user_input==3:
     for item in items:
        print(item)
        
    elif user_input==4:
     print("you have exited the loop")
     break
    print()
    
    if user_input==5:
     items.clear()
     print("your cart has been cleared")
    print()

    if user_input==6:
        search_item=input("enter the name of item you like:-")
        if search_item in items:
           print(f"{search_item} is in cart")
        else:
           print("item not found")
        print()
 
              
    