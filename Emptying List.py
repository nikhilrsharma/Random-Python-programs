list1=['abc','def','ghi']

print(list1)

#Always create a copy when modifying a list


print(list1[:])

print(list1==list1[:])

print(list1)

for item in list1[:]:
    list1.remove(item)
    print(list1)