import Task1
import Task5


s = input('Введите команду: ')
while s != 'exit':
  if s.endswith(" -h"):
    if list(s.split())[0] == 'f':
      print("""
    
    Функция, которая возвращает значение f(x)
    
    :params x: значение x
    :params func: заданная функция в типе str()
    :return: значение в точке x.
    
    """)
s = input('Введите команду: ')
