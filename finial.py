class Bus:

    def __init__(self, bus_name, chairs, destination):
        self.bus_name = bus_name
        self.chairs = chairs
        self.destination = destination


class Chair:
    def __init__(self, name, is_booked):
        self.name = name
        self.is_booked = is_booked


bus1 = Bus("Bus 1", [
    Chair("Chair 1", "Yes"),
    Chair("Chair 2", "No"),
    Chair("Chair 3", "Yes"),
    Chair("Chair 4", "No"),
    Chair("Chair 5", "No"),
], "Dest1 - Dest2")

bus2 = Bus("Bus 2", [
    Chair("Chair 1", "No"),
    Chair("Chair 2", "No"),
    Chair("Chair 3", "Yes"),
    Chair("Chair 4", "Yes"),
], "Dest1 - Dest2")

bus3 = Bus("Bus 3", [
    Chair("Chair 1", "Yes"),
    Chair("Chair 2", "No"),
    Chair("Chair 3", "Yes"),
    Chair("Chair 4", "Yes"),
], "Dest1 - Dest2")

buses_array = [bus1, bus2, bus3]

for bus in buses_array:
    print("Bus: " + bus.bus_name)
    print("Destination: " + bus.destination)
    print("==================================================")

user_input = input("Please enter the bus name: ")
is_user_choice_correct = False
user_bus = None
for bus in buses_array:
    if user_input == bus.bus_name:
        is_user_choice_correct = True
        user_bus = bus

if is_user_choice_correct:
    for chair in user_bus.chairs:
        print("Chair: " + chair.name)
        print("Is chair booked: " + chair.is_booked)
    user_input = input("Please enter the chair name: ")
    is_user_choice_correct = False
    user_chair = None
    for chair in user_bus.chairs:
        if user_input == chair.name:
            is_user_choice_correct = True
            user_chair = chair

    if is_user_choice_correct:
        if user_chair.is_booked == "Yes":
            print("You picked a booked chair, Please try again with an empty chair")
        else:
            user_chair.is_booked = "Yes"
            print("You booked the chair successfully!")
    else:
        print("Error in chair name")
else:
    print("Error in bus name")
