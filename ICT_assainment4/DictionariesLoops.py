products = {
    "Elden ring": 17999,
    "Nine Sols": 7600,
    "Slay the princess": 4800,
    "Rain World": 6400,
    "Ultrakill": 6400,
}


sum = 0
for product, price in products.items():
    print(f"{product}: {price}₸")
    sum += price

print("Total cost is ", sum,"₸")