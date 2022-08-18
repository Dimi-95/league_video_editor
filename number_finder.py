# string = "0/10/0"
# string_2 = "1/10/1"
# string_size = len(string_2)
# iterator = string_size
# index_counter = 0
# positive_index_number = []


# while(iterator != 0):
#     if(string_2[index_counter].isnumeric()):
#         positive_index_number.append(index_counter)
#         index_counter = index_counter + 1
#         iterator = iterator - 1
#     else:
#         index_counter = index_counter + 1
#         iterator = iterator - 1

# print(f"Numbers got located at index: ", positive_index_number)
# print(len(positive_index_number))

# length = len(positive_index_number)
# the_length = length


# #kills can only have index 0 1
# #deaths can only have index 3 4
# #assists can only have index 6 7

# #patern detection
# # if number is true or false

# #Variations of 4
# # 10/0/0, 0/10/0, 0/0/10

# #Variations of 5
# # 10/10/0, 0/10/10, 10/0/10

# #Variations of 6
# #01 34 67
# # 10/10/10

# #check array in variation of 4 to determine what the patter is
# # pattern of 4
# # if numbers: 0135 -> Kills double digit
# # if numbers: 0235 -> Deaths double digit
# # if numbers: 0245 -> Assists double digit

# #pattern of 5
# # if numbers: 01346 -> Kills and Deaths double digit 14
# # if numbers: 02356 -> Deaths and Assists double digit 16
# # if numbers: 01356 -> Kills and Assists double digit 15

# #pattern of 6
# # All are double digits

# print(sum(positive_index_number))



#---------------------------------




string = "0/0/0"

x = string.split("/")

print(x)