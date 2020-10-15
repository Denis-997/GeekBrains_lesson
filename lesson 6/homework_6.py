# 1). Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# (Для ожидания нескольких секунд можно использовать метод стандартной библиотеки time.sleep())
import time
#Первый вариант
class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def running(self):
        print (self.__color)

t = TrafficLight('красный')
t_2 = TrafficLight('желтый')
t_3 = TrafficLight('зеленый')
t.running()
time.sleep(7)
t_2.running()
time.sleep(2)
t_3.running()
time.sleep(15)
#Второй вариант (я думаю более правильный)
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зелёный']

    def running(self):
        count = 0
                # while True:  можно добавить эти строчки и поллучится бесконечный светофор.
                #     count = 0
        while count < 3:
            print(TrafficLight.__color[count])

            if count == 0:
                time.sleep(7)
            elif count == 1:
                time.sleep(2)
            elif count == 2:
                time.sleep(15)
            count += 1
t = TrafficLight()
t.running()


# 2). Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def weight_asphalt(self):
        weight = int((self._lenght * self._width) * (25 * 5)/1000)
        print(f'{weight} т.')
road = Road(20,5000)
road.weight_asphalt()

# 3). Реализовать базовый класс Worker (работник), в котором
# определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }

class Position(Worker):
    def get_full_name(self):
        return f"Worker's name {self.name} {self.surname}"
    def get_total_income(self):
        return f"Worker's income: {self._income['wage'] + self._income['bonus']}"

worker = Position('Ваня', 'Ладесов', 'topograf', 100, 50)
print(worker.get_full_name())
print(worker.get_total_income())
worker_2 = Position('Евгений', 'Левин', 'agent', 100, 20)
print(worker_2.get_full_name())
print(worker_2.get_total_income())

# 4). Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехал'
    def stop(self):
        return f'{self.name} остановился'
    def turn_right(self):
        return f'{self.color} {self.name} повернул направо'
    def turn_left(self):
        return f'{self.color} {self.name} повернул налево'
    def show_speed(self):
        return f'текущая скорость {self.name} {self.speed}'

class Towncar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость ,текущая скорость {self.name} {self.speed} '
        else:
            return f'текущая скорость {self.name} {self.speed}'

class Sportcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость, текущая скорость {self.name} {self.speed}'
        else:
            return f'текущая скорость {self.name} {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police == True:
            return f'Внимание это полиция!!!'

car = Towncar(100, 'red', 'mazda', False)
print(car.go())
print(car.show_speed())
print(car.stop())
print(car.color)
print(car.is_police)

car_2 = PoliceCar(50, 'black', 'ford', True)
print(car_2.police())
print(car_2.name)
print(car_2.color)
print(car_2.go())
print(car_2.turn_right())
print(car_2.show_speed())
print(car_2.stop())

car_3 = Sportcar(170, 'red', 'ferari', False)
print(car_3.color)
print(car_3.name)
print(car_3.is_police)
print(car_3.show_speed())
print(car_3.turn_left())

# 5). Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
# класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'Запуск отрисовки {self.title}.'

class Pen(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки  ручкой.'

class Pencil(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}.Запуск отрисовки  карандашом.'

class Handle(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки  маркером.'

st = Pen('Ручку')
print(st.draw())
st_2 = Pencil('Карандаш')
print(st_2.draw())
st_3 = Handle('Маркер')
print(st_3.draw())























