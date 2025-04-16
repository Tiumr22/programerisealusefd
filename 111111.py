class Level:
    def __init__(self, level_id, resources):
        self.level_id = level_id
        self.resources = resources
        self.next_level = None

    def set_next_level(self, next_level):
        self.next_level = next_level

    def get_resources(self):
        return self.resources

    def share_resources(self, amount):
        if amount <= self.resources:
            self.resources -= amount
            print(f"Level {self.level_id} shared {amount} resources.")
            return amount
        else:
            print(f"Level {self.level_id} doesn't have enough resources to share.")
            return 0

    def transfer_resources(self, amount):
        if self.next_level:
            transferred = self.share_resources(amount)
            self.next_level.receive_resources(transferred)

    def receive_resources(self, amount):
        self.resources += amount
        print(f"Level {self.level_id} received {amount} resources.")

    def __str__(self):
        return f"Level {self.level_id}: {self.resources} resources"

# Инициализация уровней
X = 10
levels = [Level(i + 1, 100) for i in range(X)]

# Установка связей между уровнями
for i in range(X - 1):
    levels[i].set_next_level(levels[i + 1])

# Пример действий
print("=== Initial State ===")
for level in levels:
    print(level)

# Уровень 1 передаёт 30 ресурсов уровню 2
levels[0].transfer_resources(30)

# Уровень 2 делится 20 ресурсами (например, с внешним игроком)
shared = levels[1].share_resources(20)

print("\n=== After Actions ===")
for level in levels:
    print(level)
