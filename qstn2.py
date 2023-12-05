# list_1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# list_1.insert(2, [9,0,1,2])
# list_1.insert(3, [3,4,5,6])
# list_1.pop(4)
# list_1.pop(-1)
# print(list_1)

# for i in range(len(list_1)):
#     print(list_1[i])


original_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
result_strings = []
result_strings = ["even" if sum(sublist) % 2 == 0 else "odd" for sublist in original_list]

for sublist in original_list:
    sublist_result = "odd" if any(num % 2 != 0 for num in sublist) else "even"
    result_strings.append(sublist_result)

result_string = " ".join(result_strings)
print(result_string)






# even_numbers_list = []
# odd_numbers_list = []

# for list in list_1:
#     even_numbers = [num for num in list if num % 2 == 0]
#     odd_numbers = [num for num in list if num % 2 != 0]
    
#     even_numbers_list.append(even_numbers)
#     odd_numbers_list.append(odd_numbers)

# print("even Numberslist:",even_numbers_list)
# print("Odd Numbers List:", odd_numbers_list)


# sums_list = [sum(list) for list in list_1]

# print(sums_list)


# result_strings = []

# for list in list_1:
#     sums_list = sum(list)
    
#     if sums_list % 2 == 0:
#         result_strings.append("even")
#     else:
#         result_strings.append("odd")

# result_string = " ".join(result_strings)
# print(result_string)
