import random

#сюды можно добавить нужные лоты с определенным шансом выпадения. Сумма probability должна быть равна 100 
PRIZES = [
    {"name": "40%", "probability": 40},
    {"name": "25%", "probability": 25},
    {"name": "15%", "probability": 15},
    {"name": "12%", "probability": 12},
    {"name": "5%", "probability": 5},
    {"name": "2%", "probability": 2},
    {"name": "1%", "probability": 1},
]

def spin_wheel():
    r = random.randint(1, 100)
    print(r)
    cumulative = 0
    for prize in PRIZES:
        cumulative += prize["probability"]
        if r <= cumulative:
            return prize
    return PRIZES[-1]

result = spin_wheel()
print(f"Вам выпало: {result['name']}")
