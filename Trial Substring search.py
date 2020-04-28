# Overlapping substring search
# This one is correct

s = input("String:")

ss=input("Substring to find:")

count = 0

index=0
 

while True:
  
  index = s.find(ss, index)
  
  if index >= 0:
      count+=1  
      index+=1

  else:
      break

print("Overlapping substring occurence count:", count)