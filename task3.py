my_list = [19,15,20,9]

choice = input(f"Do you want to remove by index or value? {my_list}  :").lower()

if choice == "index":
    index = int(input("enter number to remove:"))
    my_list.pop(index)

elif choice == "value":
    value = int(input("Enter value to remove:"))
    my_list.remove(value)

else:
    print("Invalid choice") 

print(my_list)
