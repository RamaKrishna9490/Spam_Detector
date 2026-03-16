message = str(input("Enter the message: "))

if("subscribe" in message or "Make lot of money" in message or "click this" in message or "buy now" in message):
    print("Its a spam message")
else:
    print("Not a Spam message")
    