class Level:
    def __init__(self, level_id, level_name, people_count):
        self.level_id = level_id
        self.level_name = level_name  
        self.people_count = people_count

    def add_people(self, count):
        self.people_count += count

    def remove_people(self, count):
        self.people_count -= count

    def move_people_to(self, count, target_level, platform):
        if platform.resources.get("food", 0) < count or platform.resources.get("water", 0) < count:
            return
        
        self.remove_people(count)
        target_level.add_people(count)
        platform.remove_resource("food", count)
        platform.remove_resource("water", count)


class Platform:      
    def __init__(self, platform_id):
        self.platform_id = platform_id
        self.resources = {}
        
    def add_resources(self, resource_name, amount):
        self.resources[resource_name] = self.resources.get(resource_name, 0) + amount

    def remove_resource(self, resource_name, amount):
        if resource_name in self.resources:
            self.resources[resource_name] -= amount
            if self.resources[resource_name] <= 0:
                del self.resources[resource_name]

    def get_resources(self):
        return self.resources


platform1 = Platform(platform_id=1)
level1 = Level(level_id=1, level_name="first level", people_count=1000)
level2 = Level(level_id=2, level_name="second level", people_count=250)

platform1.add_resources("water", 50)
platform1.add_resources("food", 50)

level1.move_people_to(49, level2, platform1)
