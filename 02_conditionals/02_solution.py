age=22
day="Wednesday"

if age>=70:
    print("Enter a valid age")
    exit()

price=12 if age>=18  else 8

if day=="wednesday":
    # price=price-2
    price-=2

print("Ticket price is:",price)