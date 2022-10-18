import datetime
import time

class Date_and_time:
    def today(self):
        """Дата сегодняшнего дня до минут, которая потом преобразовывается в Unix"""
        date = datetime.datetime.now() # Получаем дату
        result = self._Unicode(date)
        return str(result)

    def array(self):
        """Дата 2-дневной давности. Это второй аргумент для params, так как нужно нужны параметры для запроса на получение вопросов за 2 дня"""
        date = datetime.datetime.now() # Получаем дату
        date = str(date).split(' ') # Получаем элементы, которые потом изменяем для корректного преобразования в Unix(Из элемента дня вычитаем 2, а секунды вообще убиваем из даты)
        date[0] = date[0].split('-')  # Процесс, описанный выше
        date[0][2] = str(int(date[0][2]) - 2) # Процесс, описанный выше
        date[1] = date[1].split(':') # Процесс, описанный выше
        date[1].remove(date[1][2]) # Процесс, описанный выше
        date = date[0] + date[1] # Преобразовываем измененные элементы в 1 список
        date = {'year': int(date[0]), 'month' : int(date[1]), 'day' : int(date[2]), 'hour' : int(date[3]), 'minute' : int(date[4]) } # Так как библиотека datetime принимает в своем методе datetime только целые значения, я создаю словарь
        date = datetime.datetime(date['year'], date['month'], date['day'], date['hour'], date['minute'])
        result=time.mktime(date.timetuple()) #Преобразовываем в Unix, не вызывал функцию, так как она принимает только 1 аргумент, а мне бы пришлось передовать словарь
        return result

    def _Unicode(self, date):
        """Функция для преобразования в Unix"""
        result = time.mktime(date.timetuple()) 
        return result
