budget = float(input())
price_per_kg_flour = float(input())
price_per_l_milk = 0
cozonacs = 0
eggs = 0
#eggs = 1 pack
#flour = 1 kg
#milk = 0.250 l

price_per_pack_eggs = price_per_kg_flour * 0.75
price_per_l_milk = price_per_kg_flour * 0.25
price_per_l_milk += price_per_kg_flour
total_price_cozonac = price_per_pack_eggs + price_per_kg_flour + (price_per_l_milk * 0.25)

while budget > total_price_cozonac:
    budget -= total_price_cozonac
    cozonacs += 1
    eggs += 3
    if cozonacs % 3 == 0:
        loses = cozonacs -2
        eggs -= loses
print(f"You made {cozonacs} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")
