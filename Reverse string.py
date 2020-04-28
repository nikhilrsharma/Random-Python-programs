# reverse string

s1 = input("Enter a string with multiple words:")

print(f'Original:{s1}')
print(f'Reverse is:{s1[::-1]}')

each_word_new_list = []

s1_split = s1.split()

for i in range(0,len(s1_split)):
    each_word_new_list.append(s1_split[i][::-1])
    
print(f'New Reverse as List:{each_word_new_list}')

each_word_new_string=' '.join(each_word_new_list)

print(f'New Reverse as String:{each_word_new_string}')