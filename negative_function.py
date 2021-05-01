def greatest_product(my_list):
    num1 = 0
    num2 = 0
    product = 0

    for i in my_list:
        if i > num1:
            num1 = i
    for i in my_list:
        if i > num2 and i < num1:
            num2 = i
    print(f'num1: {num1} \nnum2: {num2}')

    product = num1 * num2    

    return product


print(negative([6,3,7,1,2]))