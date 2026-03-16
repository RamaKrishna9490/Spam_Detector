user_name = str(input("Enter the Username: "))

if(len(user_name)<10):
    print("Invalid Username")
    
else:
    print(f"{user_name}")