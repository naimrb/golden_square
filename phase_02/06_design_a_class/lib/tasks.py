class TaskTracker():
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def list(self):
        return self.tasks
    
    def completed(self, task):
        self.tasks.remove(task)