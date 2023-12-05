

print("")
print("result1")
print("")
   
sample = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] 
result1 = []    
for i in sample[:2]:
    result1.append(i)

result1.insert(2,[9,0,1,2])
result1.insert(3,[3,4,5,6])

for j in result1:
    print(j)

odd_and_even = []
for k in sample:
    for l in k:
        if(l%2)==0:
            odd_and_even.append("even")
        else:
            odd_and_even.append("odd")

print("")
print("result 2")
print("")

odd_and_even1 = []
odd_and_even1.append(odd_and_even[:4])
odd_and_even1.append(odd_and_even[4:8])
odd_and_even1.append(odd_and_even[8:12])
odd_and_even1.append(odd_and_even[12:17])

for lists in odd_and_even1:
    print(lists)

print("")
print("result 3")
print("")

result3 = [sample[1][0]*2,sample[3][0]*2,sample[1][1]*2,sample[2][0]*2]

print(result3)

print("")
print("result 4")
print("")

even = []
for even1 in result3:
    if(even1 % 2)==0:
        even.append("even")
    else:
        even.append("odd")
print(even)



