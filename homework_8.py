# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.
class Date:
    def __init__(self, day_month_year):
        self.date_month_year = str(day_month_year)
    @classmethod
    def extract(cls, day_month_year):
        integer = []
        for i in day_month_year.split():
            if  i.isdigit():
                integer.append(i)
        date_int = [int(x) for x in integer ]
        return f'{date_int[0]} {date_int[1]} {date_int[-1]}'

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Всё верно'
                else:
                    return f'Не правильный год'
            else:
                return f'Не правильный месяц'
        else:
            return f'Не правильный день'

data = Date('23 - 10 - 2020')
print(data)
print(Date.extract('23 - 10 - 2020'))
print(Date.validate(10, 12, 2020))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.
class ZeroDevision(Exception):
    def __init__(self, txt):
        self.txt = txt

def division(a_int, b_int):
    if b_int == 0:
        raise ZeroDevision('на ноль делить нельзя')
    else:
        return a_int / b_int

print(division(40, 4))
print(division(55, 10))
print(division(10, 0))


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать
# проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
class Err:
    def __init__(self, *args):
        self.new_list = []

    def inp_numbers(self):
        lst = []
        stop_comm = True
        while stop_comm:
                number = input('Введите числа, если хотите закончить введите "stop" :')
                if number == 'stop':
                    stop_comm = False
                else:
                    if number.isdigit():
                        lst.append(number)
                    else:
                        print('вы ввели не число')
        self.new_list = [int(x) for x in lst]
        return self.new_list

int_num = Err()
print(int_num.inp_numbers())

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#  А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

#Не могу понять что тут нужно сделать дальше , если вам не трудно могли бы вы сбросит в комментарии на почту вот это
# задание (выполненное) хочу провести анализ , в каком месте я не догоняю

class OfficeEquipment:
    def __init__(self, name, quatity, release_date):
        self.name = name
        self.quatity =quatity
        self.release_date = release_date
        self.lst = []


    def reception(self):
        dic =  {'наименование модели': self.name,
                     'количество': self.quatity,
                     'дата приема': self.release_date}
        self.lst.append(dic)
        return self.lst


    def passing(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, quatity, release_date, color):
        super().__init__(name, quatity, release_date)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, quatity, release_date, price):
        super().__init__(name, quatity, release_date)
        self.price = price


class Xerography(OfficeEquipment):
    def __init__(self, name, quatity, release_date, weight):
        super().__init__(name, quatity, release_date)
        self.weight = weight


of_1 = Printer('hp', 5, 2005, 'red')
of_2 = Printer('cannon', 10, 2001, 'blue')
of_3 = Printer('def', 1, 2020, 'green')
print(of_2.reception())
print(of_1.reception())
print(of_3.reception())


# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
#
class ComplexNumber:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2


    def __add__(self, other):
        return f'complex number = {self.number_1 + other.number_1} + {self.number_2 + other.number_2}j'
    def __mul__(self, other):
        return f"complex number = {self.number_1 * other.number_1 - self.number_2 * other.number_2} +" \
               f"{self.number_2 * other.number_1 + self.number_1 * other.number_2}j "

z = ComplexNumber(1, 2)
z_2 = ComplexNumber(3, 4)
print(z + z_2)
print(z * z_2)


