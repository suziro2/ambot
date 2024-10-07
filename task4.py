user1 = ["wakosumabot" ,"dinakaya","alala"]

user = input("you want to sort or reverse:").lower()

if user == "sort":
    user1.sort()
    print(user1)


elif user == "reverse":
    user1.reverse()
    print(user1)
    
else:
    print("invalid")



    