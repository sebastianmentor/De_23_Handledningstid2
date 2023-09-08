
while True:
    number = input('Vänligen skriv in ett positivt heltal större än 0: ')

    if number.isdigit() and int(number)>0:
        number = int(number)
        break
    print('Fel vid input!!!')


# for i in range(1,number):
#     print(i)

numbers_between = 1
while numbers_between < number: # Extra tydlighet om ni vill så while 1<= numbers_between < number

    print(numbers_between)
    numbers_between += 1