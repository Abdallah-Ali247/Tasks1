


a=[1,2]
b=[2,1]
c=[]

for x,y in zip(a,b):
    c.append(x+y)

print(c)

###########################################
c=[]
for x in range(len(a)) :
    c.append(a[x]+b[x])


print(c)

##########################################



c=[a[x]+b[x] for x in range(len(a))]
print(c)

    




























