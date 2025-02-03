# list is mutable

tea_varities=["Black","Green","Oolang"]
print(tea_varities[1:3])

# being treated as an array
tea_varities[1:2]="Lemon"
print(tea_varities)

tea_varities=["Black","Green","Masala","White"]
tea_varities[1:2]=["Lemon"]
print(tea_varities)


# methods
tea_varities.append("Oolong")
print(tea_varities)

tea_varities.pop()
print(tea_varities)

tea_varities.remove("White")
print(tea_varities)

tea_varities.insert(1,"green")
print(tea_varities)

tea_varities_copy=tea_varities.copy()

#list compreshesion
squared_nums=[x**2 for x in range(10)]
print(squared_nums)