class Platform:
    def __init__(self, levels):
        self.levels = levels

    def get_next_level(self, current_level):
        # Tagastab järgmise taseme
        level_index = self.levels.index(current_level)
        if level_index < len(self.levels) - 1:
            return self.levels[level_index + 1]
        return None

    def run_game(self, player):
        # Läbib kõik tasemed ja lubab mängijal teha otsuseid
        for level in self.levels:
            if level.is_active:
                player.make_decision(level)
                if not level.is_active:
                    break
class Player:
    def __init__(self, name):
        self.name = name

    def make_decision(self, level):
        # Mängija teeb otsuse, kas hoida ressursse, jagada või edasi anda
        print(f"Teed otsuse tasemel {level.level_id}.")
        action = input("Kuidas jagada ressursse (1: endale, 2: jagada, 3: edasi anda)? ")

        if action == "1":
            print(f"Tase {level.level_id} jättis kõik ressursid endale.")
        elif action == "2":
            amount = int(input("Kui palju ressursse jagada? "))
            level.share_resources(amount)
        elif action == "3":
            amount = int(input("Kui palju ressursse edasi anda? "))
            next_level = Platform.get_next_level(level)
            level.transfer_resources(amount, next_level)
class Level:
    def __init__(self, level_id, resources, min_threshold):
        self.level_id = level_id
        self.resources = resources
        self.min_threshold = min_threshold
        self.is_active = True

    def get_resources(self):
        return self.resources

    def lose_resources(self, amount):
        self.resources -= amount
        if self.resources < self.min_threshold:
            self.is_active = False
            print(f"Tase {self.level_id} on väljas mängust!")

    def transfer_resources(self, amount, next_level):
        transfer_amount = amount * 0.9  # 10% kadus
        self.lose_resources(amount)
        next_level.receive_resources(transfer_amount)

    def receive_resources(self, amount):
        self.resources += amount

    def share_resources(self, amount):
        self.resources -= amount
        print(f"Tase {self.level_id} jagas {amount} ressursse.")

