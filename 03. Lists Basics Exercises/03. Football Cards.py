team_a = [1] * 11
team_b = [1] * 11
cards = input().split(" ")

for card in cards:
    sep = card.split("-")
    team = sep[0]
    player = sep[1]
    idx = int(player) - 1

    if team == "A":
        team_a[idx] = 0
    if team == "B":
        team_b[idx] = 0
    if sum(team_a) < 7 or sum(team_b) < 7:
        break

print(f"Team A - {sum(team_a)}; Team B - {sum(team_b)}")

if sum(team_a) < 7 or sum(team_b) < 7:
    print("Game was terminated")