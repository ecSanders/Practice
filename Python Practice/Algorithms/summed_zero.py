# Determines any summation of number in the list equal 0
def summed_zero(my_list):
    for i in my_list:
        for j in my_list:
            if i + j == 0:
                return True          
    return False

print(summed_zero([1,2,3,4,5,-3]))
print(summed_zero([1,2,3,4,5]))

# Better solution: pseudo code
'''
for loop:
    if -i in list:
        return True
return False
'''