class Area:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def display(self):
        print(f"Area: {self.name}")
        print(f"Description: {self.description}")