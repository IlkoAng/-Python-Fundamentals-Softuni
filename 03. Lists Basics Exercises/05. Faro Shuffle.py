deck = input().split(" ")
shuffles = int(input())
left = []
right = []

for shuffle in range(shuffles):
    current_deck = []
    half = int(len(deck)/2)
    left = deck[0:half]
    right = deck[half::]
    for card in range(len(left)):
        current_deck.append(left[card])
        current_deck.append(right[card])
    deck = current_deck
print(deck)

