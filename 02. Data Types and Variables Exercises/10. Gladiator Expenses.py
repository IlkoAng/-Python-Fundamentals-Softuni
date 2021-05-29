number_of_losts = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
money = 0
shield_breaks = 0

for lost in range(1, number_of_losts +1):

    if lost % 2 == 0:
        money += helmet_price
    if lost % 3 == 0:
        money += sword_price
        if lost % 2 == 0:
            money += shield_price
            shield_breaks += 1
            if shield_breaks % 2 == 0:
                money += armor_price

print(f"Gladiator expenses: {money:.2f} aureus")
