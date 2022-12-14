per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input('Введите сумму: '))
deposit = []
for value in per_cent.values():
    income = int(money * value / 100)
    deposit.append(income)

print("Максимальная сумма, которую вы можете заработать — %d" % (max(deposit)))
