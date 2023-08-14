# course.py

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Course:
    name: str = 'Unknown'
    grade: int = 0
    points: float = 0

    @classmethod
    def from_dict(cls, course_dict: dict) -> Course:
        return cls(**course_dict)

    def __str__(self) -> str:
        s = ''
        for field in self.__dataclass_fields__.values():
            field_name = field.name.replace('_', ' ').title()
            s += f'{field_name}: {getattr(self, field.name)}, '
        return s.rstrip(', ')

    def __lt__(self, other: Course) -> bool:
        return self.name < other.name

    def __eq__(self, other: Course) -> bool:
        return self.name == other.name
