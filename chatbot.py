from datetime import datetime

# Greet the user based on current time
curr = datetime.now()
name = str(input("Enter Your Name :"))
c = curr.hour

if c < 12:
    print(f"Good Morning {name} !")
elif c >= 12 and c < 18:
    print(f"Good Afternoon {name} !")
else:
    print(f"Good Evening {name} !")

print("Welcome to help centre")
print("1. My Orders \n2. My Account \n3. Return \n4. Payments \n5. Product Question \n6. Something else \n7. Exit")

# Define functions for each menu option
def myorder():
    print("1. Current Products \n2. Previous Order \n3. Canceled Order")
    type_order = int(input("Enter Type of Order :"))
    if type_order == 1:
        print("Current Product: Lenskart Glasses")
    elif type_order == 2:
        print("Previous Order: Samsung Galaxy Z Fold 2")
    elif type_order == 3:
        print("Canceled Order: Bewakoof White Shirt")
    else:
        print("Invalid option in My Orders.")

def myaccount():
    print("Alright! I'd be happy to help. What's going on with your account?")
    print("1. Change the number \n2. Change my email")
    type_order = int(input("Enter your request :"))
    
    if type_order == 1:
        print("Which phone number do you need to change?")
        print("1. Contact number for an order \n2. Register number for my account \n3. Ask another question")
        ph_num = int(input("Enter your request :"))
        if ph_num == 1:
            ph1 = int(input("Enter your new 10-digit number : "))
            print("Successfully changed to", ph1)
        elif ph_num == 2:
            print("1. Go to the Flipkart website or app.\n2. Enter your mobile number on the login page.")
            print("3. Enter the OTP sent to your phone.\n4. Verify your phone number.")
        else:
            print("Please ask another question.")
    
    elif type_order == 2:
        print("Which email do you need to change?")
        print("1. Contact email for an order \n2. Change email for my account \n3. Ask another question")
        email_option = int(input("Enter your request :"))
        if email_option == 1:
            email = str(input("Enter your new email: "))
            print("Successfully changed to", email)
        elif email_option == 2:
            print("1. Go to the Account section.\n2. Select Edit Profile.")
            print("3. Enter your new email address.\n4. Tap Verify.")
        else:
            print("Please ask another question.")
    else:
        print("Invalid option in My Account.")

def ret():
    print("Alright! What kind of issue are you having with return?")
    print("1. Payment and refunds \n2. Issue with order")
    ch = int(input("Enter your request :"))
    
    if ch == 1:
        print("1. Where can I get my refund?")
        a = int(input("Enter your request :"))
        if a == 1:
            print("1. Cash on delivery \n2. Prepaid")
            b = int(input("Enter your request :"))
            if b == 1:
                print("Refund (amount < ₹1000) will be processed to the UPI ID you shared.")
            elif b == 2:
                print("Refund (amount < ₹1000) will be processed to the card you used.")
    elif ch == 2:
        issue = str(input("Enter issue with your order: "))
        print("Your issue has been recorded:", issue)
    else:
        print("Invalid option in Return.")

def payment():
    print("1. Where do I get refund? \n2. Amount debited but order not confirmed")
    ch = int(input("Enter your request :"))
    if ch == 1:
        print("Refunds are processed within 5–7 business days.")
    elif ch == 2:
        print("If the amount was debited but the order isn't confirmed, please wait or contact support.")
    else:
        print("Invalid option in Payments.")

def question():
    print("Sure! Please ask your product-related question below.")
    q = str(input("Your question: "))
    print("Thank you! We'll get back to you shortly regarding:", q)

def somethingelse():
    print("Please describe your issue:")
    msg = str(input("Your message: "))
    print("Thank you for contacting us. Your message has been received.")

# Main choice input
ch = int(input("Enter your choice (1–7): "))

# Call corresponding function
if ch == 1:
    myorder()
elif ch == 2:
    myaccount()
elif ch == 3:
    ret()
elif ch == 4:
    payment()
elif ch == 5:
    question()
elif ch == 6:
    somethingelse()
elif ch == 7:
    print("Thank you for visiting the help centre!")
else:
    print("Invalid option. Please try again.")
