from random import choice, randint
import os

first_name = ("Жран", "Жмых", "Бром", "Дин", "Ван", "Грим")
last_name = ("Дикий", "Ужасный", "Яросный", "Угрюмый", "Вонючий", "Свирепый", "Старый")




def make_hero(
name=None,
hp_curret=None,
hp_max=20,
lvl=0,
xp_next=None,
xp_curret=0,
ATK_base=3,
ATK_weapon=None,
weapon=None,
defense_base=0,
defense_shield=0,
defense_armor=0,
shield=None,
armor=None,
luck=1,
inventory=None,
money=None,
mage=None,
mp_max=None,
mp_curret=None,
stamina_max=None,
stamina_curret=None
) -> list:
    if not name:
        name = choice(first_name) + " " + choice(last_name)
    if not money:
        money = randint(1, (5 + 10 * lvl))
    defense_curret = defense_base + defense_shield + defense_armor
    if not inventory:
        inventory = []
    if not xp_next:
        xp_next = 234 + 234 * (lvl * 2)
    if not hp_max:
        hp_max = 20 + 5 * lvl
    if not hp_curret:
        hp_curret = hp_max
    if not ATK_weapon and not weapon:
        ATK_weapon = 0
    ATK_curret = ATK_base + ATK_weapon
    if not mage:
        mage = choice([True, False])
    if mage == True and not mp_max:
        mp_max = 20 + 5 * lvl
    if not stamina_max:
        stamina_max = 20 + 5 * lvl
    if not mp_curret:
        mp_curret = mp_max
    if not stamina_curret:
        stamina_curret = stamina_max



    return [
        name,
        hp_max,
        hp_curret,
        lvl,
        xp_next,
        xp_curret,
        ATK_base,
        ATK_weapon,
        ATK_curret,
        weapon,
        defense_base,
        defense_shield,
        defense_armor,
        defense_curret,
        shield,
        armor,
        luck,
        inventory,
        money,
        mage,
        mp_max,
        mp_curret,
        stamina_max,
        stamina_curret
    ]

def show_hero(hero):
    name = hero[0]
    hp_max = hero[1]
    hp_curret = hero[2]
    lvl = hero[3]
    xp_next = hero[4]
    xp_curret = hero[5]
    ATK_base = hero[6]
    ATK_weapon = hero[7]
    ATK_curret = hero[8]
    weapon = hero[9]
    defense_base = hero[10]
    defense_shield = hero[11]
    defense_armor = hero[12]
    defense_curret = hero[13]
    shield = hero[14]
    armor = hero[15]
    luck = hero[16]
    inventory = hero[17]
    money = hero[18]
    mage = hero[19]
    mp_max = hero[20]
    mp_curret = hero[21]
    stamina_max = hero[22]
    stamina_curret = hero[23]

    print("Персонаж:\n")
    print(f"Имя: {name}")
    if mage == True:
        print("Имеет талант к магии")
    elif mage == False:
        print("Таланта к магии нет")
    print(f"HP: {hp_curret}/{hp_max}")
    if mage == True:
        print(f"MP: {mp_curret}/{mp_max}")
    print(f"Выносливость: {stamina_curret}/{stamina_max}")
    print(f"ATK: {ATK_curret} ({ATK_base} + {ATK_weapon})")
    print(f"Защита: {defense_curret} ({defense_base} + {defense_armor} + {defense_shield})")
    print(f"Удача: {luck}")
    print(f"XP: {xp_curret}/{xp_next}")
    print(f"Уровень: {lvl}")
    print(f"Оружие: {weapon}")
    print(f"Доспехи: {armor}")
    print(f"Щит: {shield}")
    print(f"Монеты: {money}\n")
    print("Инвентарь:\n")
    if not inventory:
        print("Пустой\n")
    else:
        print(inventory)
        print(" ")

def levelup(hero: list) -> None:
    while hero[5] >= hero[4]:
        hero[3] += 1
        for i in range(3):
            hero[4] = 234 + 234 * (hero[3])
            print(f"Поздравляем! {hero[0]} достиг {hero[3]} уровня.\n")
            print("Распределите характеристики:\n")
            print(f"1.Увеличить HP {hero[2]}/{hero[1]} + 5")
            print(f"2.Увеличить ATK {hero[6]} + 3")
            print(f"3.Увеличить Защиту {hero[10]} +")
            print(f"4.Увеличить удачу {hero[16]} + 1")
            print(f"5.Увеличть выносливость {hero[23]}/{hero[22]} + 5")
            if hero[19] == True:
                print(f"6.Увеличить ману {hero[21]}/{hero[20]} + 5")
            plus = input("Введите номер выбора и нажмите ENTER: ")
            if plus == "1":
                hero[1] += 5
                hero[2] += 5
            elif plus == "2":
                hero[6] += 3
            elif plus == "3":
                hero[10] += 2
            elif plus == "4":
                hero[16] += 1
            elif plus == "5":
                hero[22] += 5
            elif plus == "6" and hero[19]:
                hero[20] += 5
            if not hero[7]:
                hero[8] = hero[6]
            os.system("cls")
            

def buy_item(hero: list, item, price: int) -> None:
    if hero[18] >= price:
        hero[18] -= price
        hero[17].append(item)
        print(f"\n{hero[0]} купил {item} за {price} монет!\n")
    else:
        print(f"\n{hero[0]} не хватило {price - hero[18]} монет!\n")

def consume_item(hero: list, idx: int) -> None:
    if idx <= len(hero[17]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[17][idx]}\n")
        if hero[17][idx] == "зелье лечения":
            hero[17].pop(idx)
            hero[2] += 10
            if hero[2] > hero[1]:
                hero[2] = hero[1]
        elif hero[17][idx] == "зелье маны" and hero[20] is not None:
            hero[17].pop(idx)
            hero[21] += 10
            if hero[21] > hero[20]:
                hero[21] = hero[20]
        elif not hero[20]:
                print("У вас нет таланта к магии чтобы употребить зелье\n")
        elif hero[17][idx] == "зелье выносливости":
            hero[17].pop(idx)
            hero[23] += 10
            if hero[23] > hero[22]:
                hero[23] = hero[22]
        elif hero[17][idx] == "яблоко":
            pass
    else:
        print("Нет такого предмета")

def play_dice(hero: list, bet: int) -> None:
    if bet > 0:
        if hero[18] >= bet:
            hero_score = randint (2, 12)
            casino_score = randint(2, 12)
            print(f"\n{hero[0]} выбросил {hero_score}")
            print(f"Трактирщик выбросил {casino_score}\n")
            if hero_score > casino_score:
                hero[18] += bet
                print(f"{hero[0]} победил и забирает {bet} монет!\n")
            elif hero_score < casino_score:
                hero[18] -= bet
                print(f"{hero[0]} проиграл {bet} монет\n")
            else:
                print("Ничья\n")

        else:
            print(f" У {hero[0]} нет столько монет!\n")
    else:
        print("Такая ставка не возможна! Ставки начинааются от 1 монеты!")

def start_fight(hero: list, enemy: list) -> None:
    while hero[2] > 0 and enemy[2] > 0:
        os.system("cls")
        combat_turn(hero, enemy)
        combat_turn(enemy, hero)
        print("")
        show_hero(hero)
        show_hero(enemy)
        turn = input("\nНажмите ENTER чтобы продолжить бой: ")
    combat_result(hero, enemy)

def combat_turn(attacker: list, defender: list) -> None:
    if attacker[2] > 0:
        damage = (attacker[8] + randint(0, (attacker[3] + 1)) - defender[13])
        defender[2] -= damage
        print(f"{attacker[0]} атаковал {defender[0]} на {damage}!")

def combat_result(hero: list, enemy: list) -> None:
    os.system("cls")
    if hero[2] > 0 and enemy[2] <= 0:
        xp = 100 + 100 * enemy[3]
        print(f"{hero[0]} победил {enemy[0]} и в награду получает:")
        hero[5] += xp
        print(f"{xp} опыта")
        hero[18] += enemy[18]
        print(f"{enemy[18]} монет")
        print(f"И забирает предметы: ", end="")
        for item in enemy[17]:
            print(item, end=", ")
        hero[17] += enemy[17]
        levelup(hero)
    else:
        print("Вы умерли")

def choose_option(hero: list, text: str, options: list) -> int:
    os.system("cls")
    show_hero(hero)
    print(text)
    print(" ")
    print("Что будете делать дальше?\n")
    for num, option in enumerate(options):
        print(f"{num}. {option}")
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except:
        print("Ввод должен быть целым неотрицательным числом")
    else: 
        if option <= len(options) - 1 and option > -1:
            return option
        else:
            print("Нет такого выбора")

def visit_hub(hero: list):
    text = f"{hero[0]} приехал в город. В нём есть несколько дорог"
    options= [
        "Сыграть в кости",
        "Поехать в мрачный лес",
        "Купить зелье за 10 монет",
        "Выпить зелье"    
    ]
    option = choose_option(hero, text, options)
    if option == 0:
        bet = int(input("Введите желаемую ставку: "))
        play_dice(hero, bet)
    elif option == 1:
        enemy = make_hero()
        start_fight(hero, enemy)
    elif option == 2:
        buy_item(hero, "зелье", 10)
    elif option == 3:
        consume_item(hero, 0)
    input("\n Нажмите ENTER чтобы продолжить")