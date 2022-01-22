"""   Assignment 2.2 - 3 """

# To add elements to a tuple

#t = (1,2,3,4,5)
print(t)
l = list(t)
p = int(input("Enter a position to insert the element :"))
ele = input("Enter a element :")
l.insert(p,int(ele))
t = tuple(l)
# After adding 
print(t)
