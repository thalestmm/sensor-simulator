from pydantic import BaseModel


class Machine(BaseModel):
    name: str = "General Machine"


# TODO: Maybe turn all fields into Pydantic's Field
class Sensor(Machine):
    min_reading: float  # TODO: Validate min_reading < max_reading
    max_reading: float
    steps: float  # TODO: Validate steps < (max_reading - min_reading)
    unit_of_measure: str


class Switch(Machine):
    pass


class BinarySwitch(Switch):
    pass


class ValueSwitch(Switch):
    pass
