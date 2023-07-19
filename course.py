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
        return f'Name: {self.name}, Grade: {self.grade}, Points: {self.points}'
