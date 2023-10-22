money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital #бюджет в самом начале
months = 0
while True:
    budget += (salary - spend)
    if budget < 0: break
    spend *= (1 + increase)
    months += 1


print("Количество месяцев, которое можно протянуть без долгов:", months)
