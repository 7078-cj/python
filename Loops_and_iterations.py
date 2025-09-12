nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
    
print('--------')
for num in nums:
    if num == 3:
        print('Found')
        break #it will stop the whole loop
    print(num)

print('--------')
for num in nums:
    if num == 3:
        print('Found')
        continue #it will continue
    print(num)
    
print('--------')
for num in nums:
    for letter in 'abc': #for every loop of nums the loop of letter runs
        print(num, letter)
        
print('--------')
for i in range(10): # it start at 0
    print(i)
    
print('--------')
for i in range(1, 11): # it starts at 1
    print(i)