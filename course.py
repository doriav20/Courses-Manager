from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Course:
    name: str
    grade: int
    points: float

    @classmethod
    def from_dict(cls, course_dict: dict) -> Course:
        return cls(**course_dict)

    def __str__(self) -> str:
        s = ''
        for field in self.__dataclass_fields__.values():
            field_name = field.name.replace('_', ' ').title()
            s += f'{field_name}: {getattr(self, field.name)}, '
        return s.rstrip(', ')
