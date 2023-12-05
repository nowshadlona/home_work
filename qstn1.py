sample = [2,4,4,4,5,5,7,9]

sum = 0
for i in sample:
  sum = sum + i

def custom_len(x):
  count = 0
  for j in x:
    count = count + 1
  return count
mean_avr = sum/custom_len(sample)
sum1 = 0
for k in sample:
    sample_sum = (k-mean_avr)**2
    sum1 = sum1+sample_sum

o = (sum1/(custom_len(sample)-1))**(1/2)
print(o)

# or


# sample = [2, 4, 4, 4, 5, 5, 7, 9] 

# import statistics
# print("Standard Deviation of sample is= % s "
#                 % (statistics.stdev(sample)))