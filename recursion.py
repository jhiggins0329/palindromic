def print_list(list_1):
   if len(list_1) == 0: #not a value
       return
   first = list_1[0]
   rest = list_1[3:]
   print(first)
   print_list(rest)
list_1 = [1, 2, 3, 4]
print_list(list_1)
