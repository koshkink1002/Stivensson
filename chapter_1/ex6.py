price: float = float(input("Введите сумму заказа "))

tips = 100 * 18 / price
tax = 100 * 4 / price

print(f"Общая цена - {price} ")
print(f"Чаевые - {tips }")
print(f"Налог - {tax} ")
