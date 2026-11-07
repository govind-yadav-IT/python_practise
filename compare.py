print('Enter the first number:')
first_num = int(input('> '))

print('Enter the second number:')
second_num = int(input('> '))

if first_num > second_num:
    print('The bigger number is:', first_num)

elif second_num > first_num:
    print('The bigger number is:', second_num)

else:
    print('Both numbers are equal')
