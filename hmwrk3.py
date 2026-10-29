class player:
    player_count = 0
    def __init__(self, name, level = 1):
        self.name = name
        self.level = level
        player.player_count += 1

print(player.player_count)


p1 = player("ანა")
p2 = player("დავითი", 5)
p3 = player(name="მარიამი", level = 3)

print("სულ მოთამაშე:", player.player_count)
print(f"{p1.name} {p1.level} \n{p2.name} {p2.level} \n{p3.name} {p3.level}")