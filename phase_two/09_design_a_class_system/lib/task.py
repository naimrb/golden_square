class Task():
    # Public properties:
    #   name:   a string, name of the task
    #   status: a boolean, True if completed False if not (False by default)

    def __init__(self, name):
        self.name = name
        self.status = False
    
    def completed(self):
        self.status = True