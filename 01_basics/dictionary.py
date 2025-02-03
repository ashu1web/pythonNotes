# Dicitionary is muttable

chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
print(chai_types)

print(chai_types["Masala"])
print(chai_types.get("Ginger"))


# muttable
chai_types["Green"]="Fresh"
print(chai_types)


# loop-->We are getting keys
for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai,"-",chai_types[chai])

for keys,values in chai_types.items():
    print(keys,"-",values)

# methods
chai_types.pop("Ginger")
print(chai_types)

del chai_types["Green"]
print(chai_types)

# copy
chai_types_copy=chai_types.copy()


# 2d dict
tea_shop={
          "chai":{"Masala":"Spicy","Ginger":"Zesty"},
          "Tea":{"Green":"Mild","Black":"Strong"}
         }

print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

# some more 
squared_num={x:x**2 for x in range(1,6)}
print(squared_num)
print(squared_num.clear())

# default values
keys=["Masala","Ginger","Lemon"]
default_value="Delicious"

new_dict=dict.fromkeys(keys,default_value)
new_dict=dict.fromkeys(keys,keys)
print(new_dict)