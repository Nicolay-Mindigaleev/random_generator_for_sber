import random
import json

#сюды можно добавить нужные лоты с определенным шансом выпадения. Сумма probability должна быть равна 100 
def load_prizes():
    """Загружает лоты из JSON-файла"""
    with open('data_base.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data['prizes']
def check_chance(prize_list: list[dict]):
    sum = 0
    for i in prize_list:
        sum += i["probability"]
    if abs(sum - 100) > 0.01:
        raise ValueError("Нарушено условие нормировки")
     
def spin_wheel():
    prizes = load_prizes()
    check_chance(prizes)
    r = random.randint(1, 100)
    print(r) #для отлдаки
    cumulative = 0
    for prize in prizes:
        cumulative += prize["probability"]
        if r <= cumulative:
            return prize
    return prizes[-1]

result = spin_wheel()
print(f"Вам выпало: {result['name']}")
