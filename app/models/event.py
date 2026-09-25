class Event:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def display(self):
        print(f"Event: {self.title}")
        print(f"Description: {self.description}")