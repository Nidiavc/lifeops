class Goal:
    def __init__(self, title, progress=0):
        self.title = title
        self.progress = progress

    def display(self):
        print(f"Goal: {self.title}")
        print(f"Progress: {self.progress}%")