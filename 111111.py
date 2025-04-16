class Players:
    def __init__(self):
        # This dictionary will map the floor number to the number of players on that floor
        self.players_on_floor = {}

    def add_players(self, floor, num_players):
        if floor in self.players_on_floor:
            self.players_on_floor[floor] += num_players
        else:
            self.players_on_floor[floor] = num_players

    def get_players_on_floor(self, floor):
        return self.players_on_floor.get(floor, 0)

    def get_total_players(self):
        return sum(self.players_on_floor.values())
