#Solution 1
'''
for i in range(1, 6 + 1):
    # Print leading space
    for j in range(1, 6 + 1):
        print("  ", end = "")
      
    for j in range(1, 6 + 1 - i + 1):
        print(j, end = " ")
    
    print()
'''

#Solution 2
for i in range(1, 6 + 1):
    for j in range(1, 6 + 1): 
       print(j if i <= j else " ", end = " ")
    print()
