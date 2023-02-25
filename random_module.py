import random
n=random.randint(2,5)
print(n)

n1=random.randrange(3,9)
print(n1)


l=[10,5,7,9]
n2=random.choice(l)
print(n2)

#random function

r=random.random()
print(r)


#shuffle function
list=[3,5,7,9]
random.shuffle(list)
print(list)

#uniform function
u=random.uniform(3,6)
print(u)