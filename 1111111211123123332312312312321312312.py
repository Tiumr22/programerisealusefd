class Event:
    def __init__(self, note, officer_name):
        self.timestamp = datetime.datetime.now()
        self.note = note
        self.officer_name = officer_name

    def show(self):
        print("date:", self.timestamp)
        print("officer:", self.officer_name)
        print("Note:", self.note)


class Case:
    def __init__(self, case_id, description):
        self.case_id = case_id
        self.description = description
        self.status = "open"
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def close_case(self):
        self.status = "closed"

    def get_timeline(self):
        for event in self.events:
            event.show()

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_case_id(self):
        return self.case_id


class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number
        self.cases = []

    def assign_case(self, case):
        self.cases.append(case)

    def get_info(self):
        print("Officer name:", self.name)
        print("Badge number:", self.badge_number)
       

def main():
    while True:
        print("Menu:")
        print("1. add officer")
        print("2. check case ")
        print("3. delete_case ")
        print("4. exit program ")
       
        choice = input("choose action (1-4): ")
       
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Incorrect selection. Please try again.")

main()









officer1 = PoliceOfficer("Pisun", "1488")
officer2 = PoliceOfficer("Neggri", "1945")
case1 = Case("1111", "smooking weed")
case2 = Case("2222", "stealing")
officer1.assign_case(case1)
officer2.assign_case(case2)
print("officer 1:")
officer1.get_info()
print("Crime:", case1.get_description())
print("officer 2:")
officer2.get_info()
print("Crime:", case2.get_description())
event1 = Event("First event", officer1.name)
case1.add_event(event1)
event2 = Event("Second event", officer2.name)
case2.add_event(event2)
print("Case", case1.get_case_id(), "history:")
case1.get_timeline()
print("Case", case2.get_case_id(), "history:")
case2.get_timeline()

