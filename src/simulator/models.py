class BaseMachine():
    def __init__(self, model, name):
        self.model = model
        self.name = name

    def __str__(self):
        return "{} - {}".format(self.model, self.name)


class BaseSensor(BaseMachine):
    def __init__(self, min_reading: float, max_reading: float, steps: float):
        self.min_reading = min_reading
        self.max_reading = max_reading
        self.steps = steps
