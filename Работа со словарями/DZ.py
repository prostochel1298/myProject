'''Дан словарь с оценками учеников за семестр по программированию. Запрограммируйте возможность 
вычисления среднего балла по классу и распределению оценок в порядке возрастания. В программе 
необходимо наличие анонимных функций'''

score = {"Сергеев":5, "Иванов":3,"Петров":4, "Сушков":2,"Мармеладов":3}
b = list(score.items())
b.sort(key = lambda x:x[1])
d = 0
for i in b:
    d+=i[1]
print(d/len(b))
   

