class Fish:
    name = ""
    weight = 0
    color = ""

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def status(self):
        print(Fish(self.name, self.weight, self.color))

    def feed(self, name, weight, color):
        if self.name == "First_type":
            self.weight += 1
        elif self.name == "Second_type":
            self.weight += 1
        elif self.name == "Third_type":
            self.weight += 2
            return
        else:
            print("No fish to feed")
