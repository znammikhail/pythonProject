import datetime

(y,m,d) = [int(n) for n in input().split()]
days = int(input())

a = datetime.date(y,m,d) # создали дату: 1 февраля 2011 года
delta = datetime.timedelta(days =days) # дельта в 2 дня

a += delta # Узнаем какое число будет через 2 дня в формате (yyyy-mm-dd)

print("{} {} {}".format(a.year,a.month,a.day))
