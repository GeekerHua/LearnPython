count = 20 * 2
price = 5

totalPrice = 0
i = 0
while i < count:
    if totalPrice < 100:
        totalPrice += price
    elif totalPrice < 150:
        totalPrice += price * 0.8
    elif totalPrice < 400:
        totalPrice += price * 0.5
    else:
        totalPrice += price
    i += 1
print("坐地铁的合计费用为:%f"%totalPrice)
