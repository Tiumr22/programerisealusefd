import random

class Level:
    def __init__(self, name):
        self.name = name
        self.resources = random.randint(20, 50)
        self.min_threshold = 10
        self.alive = True

    def show(self):
        status = "✅" if self.alive else "❌"
        print(f"{self.name}: {self.resources} ресурсов | Статус: {status}")

    def keep_resources(self):
        print(f"{self.name} сохраняет свои ресурсы.")

    def share(self, levels):
        if not self.alive:
            return
        amount = int(input(f"{self.name} - Сколько ресурсов поделить с соседями? "))
        neighbors = []
        index = levels.index(self)
        if index > 0 and levels[index - 1].alive:
            neighbors.append(levels[index - 1])
        if index < len(levels) - 1 and levels[index + 1].alive:
            neighbors.append(levels[index + 1])
        if not neighbors:
            print("Нет живых соседей для обмена.")
            return
        share_amount = amount // len(neighbors)
        for neighbor in neighbors:
            neighbor.resources += share_amount
        self.resources -= amount
        print(f"{self.name} поделился с соседями.")

    def transfer(self, levels):
        if not self.alive:
            return
        index = levels.index(self)
        if index < len(levels) - 1 and levels[index + 1].alive:
            target = levels[index + 1]
            loss = int(self.resources * 0.1)
            transfer_amount = self.resources - loss
            target.resources += transfer_amount
            print(f"{self.name} передал {transfer_amount} ресурсов -> {target.name} (потеря: {loss})")
            self.resources = 0
        else:
            print("Нельзя передать дальше.")

    def check_alive(self):
        if self.resources < self.min_threshold:
            self.alive = False
            print(f"{self.name} ВЫБЫЛ из игры!")


def show_all(levels):
    print("\n=== Статус всех уровней ===")
    for lvl in levels:
        lvl.show()
    print("===========================\n")


def main():
    levels = [Level(f"Уровень {i+1}") for i in range(10)]
    round_number = 1

    while any(l.alive for l in levels):
        print(f"\n=== Раунд {round_number} ===")
        for lvl in levels:
            if not lvl.alive:
                continue
            lvl.show()
            print("1 - Оставить ресурсы себе")
            print("2 - Поделиться с соседями")
            print("3 - Передать вниз")
            action = input("Выберите действие (1-3): ")

            if action == "1":
                lvl.keep_resources()
            elif action == "2":
                lvl.share(levels)
            elif action == "3":
                lvl.transfer(levels)
            else:
                print("Неверный выбор")

            lvl.check_alive()

        show_all(levels)
        round_number += 1

    print("Игра окончена. Все уровни выбыли.")


main()
