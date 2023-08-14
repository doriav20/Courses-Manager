# configuration.py

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional
from uuid import uuid4

from constants import (
    DEFAULT_COURSES_FILE_PATH,
    DEFAULT_NAME_LENGTH,
    DEFAULT_GRADE_LENGTH,
    DEFAULT_POINTS_LENGTH,
    CONFIGURATION_FILE_TEMPLATE,
)


@dataclass
class Configuration:
    courses_file_path: Path
    name_length: int
    grade_length: int
    points_length: int

    @classmethod
    def from_dict(cls, config_dict: dict) -> Configuration:
        return cls(**config_dict)

    def to_dict(self) -> dict:
        d = asdict(self)
        d['courses_file_path'] = str(d['courses_file_path'].absolute())

        return d

    def __str__(self) -> str:
        s = ''
        for field in self.__dataclass_fields__.values():
            field_name = field.name.replace('_', ' ').title()
            s += f'{field_name}: {getattr(self, field.name)}, '
        return s.rstrip(', ')


def create_default_configuration(create_config_file: bool = False) -> Configuration:
    config_obj = Configuration(
        courses_file_path=Path(DEFAULT_COURSES_FILE_PATH),
        name_length=DEFAULT_NAME_LENGTH,
        grade_length=DEFAULT_GRADE_LENGTH,
        points_length=DEFAULT_POINTS_LENGTH,
    )

    if create_config_file:
        config_filename = generate_configuration_filename()
        config_path = Path(config_filename)
        save_configuration(config_obj, config_path)

    return config_obj


def save_configuration(config: Configuration, config_path: Path) -> None:
    with open(config_path, mode='w') as config_file:
        json.dump(config.to_dict(), config_file, sort_keys=True)


def generate_configuration_filename() -> str:
    return CONFIGURATION_FILE_TEMPLATE.format(uuid4_hex=uuid4().hex)


def search_for_alternative_config_file() -> Optional[Path]:
    curr_dir_config_file = next(Path().glob('courses_manager_config_*.json'), None)
    if curr_dir_config_file:
        return curr_dir_config_file


def load_configuration(configuration_path: Optional[Path]) -> Configuration:
    if configuration_path is None or not configuration_path.is_file():
        alt_config_file = search_for_alternative_config_file()
        if alt_config_file:
            return load_configuration(alt_config_file)

        return create_default_configuration()

    with open(configuration_path) as config_file:
        config_dict = json.load(config_file)
        return Configuration.from_dict(config_dict)
