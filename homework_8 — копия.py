# Задание 1
def multiplication_table(a, b):
    numbers = [[x * y for x in range(1, a + 1)] for y in range(1, b + 1)]
    table = ''
    for line in numbers:
        for item in line:
            table += f'{item}\t'
        table += f'\n'
    return table


print(multiplication_table(5, 5))
print(multiplication_table(2, 2))
print(multiplication_table(4, 5))
print(multiplication_table(9, 9))
print(multiplication_table(10, 10))


# Задание 2
def print_directory_contents(spath):
    import os
    for x in os.listdir(spath):
        fullname = os.path.join(spath, x)
        if os.path.isdir(fullname):
            print_directory_contents(fullname)
        else:
            print(fullname)


print(print_directory_contents('../lesson Geekbrains'))


# Задание 3
def generator_random_number(start=int, stop=int):
    lst_randint = []
    dict_elem = {}
    import random
    for x in range(start, stop + 1):
        rand_num = random.randint(start, stop)
        lst_randint.append(rand_num)
    for x in lst_randint:
        dict_elem[f'elem_{x}'] = x
    return f'{lst_randint} \n{dict_elem}'


print(generator_random_number(10, 20))


# Задание 4
def bank_deposit(amount=float, date=int):
    global summ_deposite, summ_capitalization, summ_amount
    if 1000 < amount < 10000:
        if date == 6:
            summ_deposite = amount * (0.05 / 12) * date
            summ_capitalization = summ_deposite * (0.05 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
        elif date == 12:
            summ_deposite = amount * (0.06 / 12) * date
            summ_capitalization = summ_deposite * (0.06 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
        elif date == 24:
            summ_deposite = amount * (0.05 / 12) * date
            summ_capitalization = summ_deposite * (0.05 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
    elif 10000 <= amount < 100000:
        if date == 6:
            summ_deposite = amount * (0.06 / 12) * date
            summ_capitalization = summ_deposite * (0.06 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
        elif date == 12:
            summ_deposite = amount * (0.07 / 12) * date
            summ_capitalization = summ_deposite * (0.07 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
        elif date == 24:
            summ_deposite = amount * (0.065 / 12) * date
            summ_capitalization = summ_deposite * (0.065 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
    elif 100000 <= amount <= 1000000:
        if date == 6:
            summ_deposite = amount * (0.07 / 12) * date
            summ_capitalization = summ_deposite * (0.07 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
        elif date == 12:
            summ_deposite = amount * (0.08 / 12) * date
            summ_capitalization = summ_deposite * (0.08 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
        elif date == 24:
            summ_deposite = amount * (0.075 / 12) * date
            summ_capitalization = summ_deposite * (0.075 / 12) * date + summ_deposite + amount
            summ_amount = summ_deposite + amount
    return {'begin_sum': amount, 'end_sum_capitalization': summ_capitalization,
            'end_sum': summ_amount, 'date': date}


print(bank_deposit(10000, 24))
