salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

safety_capsule = 0
for _ in range(months):
    profit = salary - spend
    spend *= (1+increase)
    if (profit < 0): safety_capsule += abs(profit)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {safety_capsule:.2f}")
