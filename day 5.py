ifelse conditions
colour=input("enter the colour (red yellow green):")
if colour=='red':
    print("stop")
elif colour=='yellow':
    print("go")
elif colour=='green':
        print("get ready")
else:
            print("chosee correct colour")
output:enter the colour (red yellow green):blue
chosee correct colour
# Discount Calculator Program

amount = float(input("Enter the purchase amount: ₹ "))

if amount > 1000:
    discount = amount * 0.20   # 20% discount
    final_price = amount - discount
    print("You got 20% discount 🎉")
elif amount >= 500:
    discount = amount * 0.10   # 10% discount
    final_price = amount - discount
    print("You got 10% discount 🎉")
else:
    discount = 0
    final_price = amount
    print("No discount applied ❌")

print("Final Price to Pay: ₹", final_price)

Movie Ticket Pricing
age=int(input("enter the age"))
child_ticket=100
teen_ticket=150
adult_ticket=200
if age<12:
    print("child ticket",child_ticket)
elif age<=18:
    print("teenticket",teen_ticket)
elif age >=18:
    print("adult ticket",adult_ticket)
else:
        print("choose a correct age")
#Password Checker
correct_passward="python123"
entered_passward=(input("enter the passward"))
if entered_passward==correct_passward:
    print("asses granted")
else:
        print("not asses")
Bus Fare Program
# Bus Fare Calculator

distance = float(input("Enter the travel distance in km: "))

if distance < 5:
    fare = 10
    print("Bus Fare: ₹", fare)
elif distance <= 15:
    fare = 20
    print("Bus Fare: ₹", fare)
else:
    fare = 30
    print("Bus Fare: ₹", fare)

    

