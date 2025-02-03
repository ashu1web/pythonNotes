# Tuple  is immutable cannot be changed 
tea_Tuple=(1,2,3)
print(tea_Tuple)

print(tea_Tuple[0])
print(tea_Tuple[-1])
print(tea_Tuple[1:])

# tea_Tuple[0]=4         -->immutable cannot be changed
# print(tea_Tuple[0])  

len(tea_Tuple)
# tea_Tuple=(4,5)            
# print(tea_Tuple)       -->the memory ref has changed

more_tea=(4,5)
all_tea=more_tea+tea_Tuple
print(all_tea)

more_tea=(6,6,7,8)
if 6 in more_tea:
    print("Yes 6 is present")

print(more_tea.count(6))


# A common db operation 
tea_types=("black","green","oolong")
(Black,Green,Oolong)=tea_types
print(Black)



 