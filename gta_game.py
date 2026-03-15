class GTAPlayer:
    def __init__(self, name):
        self.name = name
        self.cheat_codes = []
        self.missions = []
        self.inventory = []
        self.wanted_level = 0
        self.money = 0
        self.level = 1
        self.vehicles = []
        self.progression = 0

    def add_cheat_code(self, code):
        self.cheat_codes.append(code)

    def complete_mission(self, mission):
        self.missions.append(mission)
        self.progression += 1

    def earn_money(self, amount):
        self.money += amount

    def update_wanted_level(self, level):
        self.wanted_level = level

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def interact(self):
        # Placeholder for interaction logic
        pass

    def update_inventory(self, item):
        self.inventory.append(item)

    def display_info(self):
        print(f"{self.name} - Money: ${self.money}, Wanted Level: {self.wanted_level}, Level: {self.level}")

class Mission:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return f"Mission: {self.title} - {self.description}"

# Game loop placeholder
if __name__ == '__main__':
    player = GTAPlayer('Player1')
    # Placeholder for interactive game loop
    while True:
        player.display_info()
        action = input('What would you like to do? ')
        if action == 'exit':
            break
