from pydantic import BaseModel, field_validator
from pydantic_core import PydanticCustomError
from random import randrange

class Machine(BaseModel):
    name: str = "General Machine"


# TODO: Maybe turn all fields into Pydantic's Field
class Sensor(Machine):
    min_reading: float
    max_reading: float
    steps: float
    unit_of_measure: str

    @field_validator('min_reading')
    @classmethod
    def validate_min_reading(cls, v: float) -> float:
        if v >= cls.max_reading:
            raise PydanticCustomError(
                'interval_error',
                'The lower boundary for the readings must be less than the top boundary.',
                {'min_reading': v,
                 'max_reading': cls.max_reading},
            )
        return v

    @field_validator('steps')
    @classmethod
    def validate_steps(cls, v: float) -> float:
        if v >= (cls.max_reading - cls.min_reading):
            raise PydanticCustomError(
                'interval_error',
                'Value for the steps must be lower than the interval set for the readings.',
                {'steps': v,
                 'interval_distance': (cls.max_reading - cls.min_reading)},
            )
        return v

    # TODO: Test all validations
    # TODO: Add exporting into json for creating presets (pydantic already has this feature)
    # TODO: Add instance creation from preset

    def generate_value(self):
        pass

    def __str__(self):
        return f'{self.name} ({self.unit_of_measure})'


class Switch(Machine):
    pass


class BinarySwitch(Switch):
    pass


class ValueSwitch(Switch):
    pass
