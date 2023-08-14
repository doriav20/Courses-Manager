# configuration.py

from __future__ import annotations

from configparser import ConfigParser
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional
from uuid import uuid4

from constants import (
    DEFAULT_COURSES_FILE_PATH,
    DEFAULT_NAME_COLUMN_LENGTH,
    DEFAULT_GRADE_COLUMN_LENGTH,
    DEFAULT_POINTS_COLUMN_LENGTH,
    CONFIGURATION_FILE_TEMPLATE,
)


@dataclass
class Configuration:
    courses_file_path: Path
    name_length: int = DEFAULT_NAME_COLUMN_LENGTH
    grade_length: int = DEFAULT_GRADE_COLUMN_LENGTH
    points_length: int = DEFAULT_POINTS_COLUMN_LENGTH

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
        name_length=DEFAULT_NAME_COLUMN_LENGTH,
        grade_length=DEFAULT_GRADE_COLUMN_LENGTH,
        points_length=DEFAULT_POINTS_COLUMN_LENGTH,
    )

    if create_config_file:
        config_filename = generate_configuration_filename()
        config_path = Path(config_filename)
        save_configuration(config_obj, config_path)

    return config_obj


def save_configuration(config: Configuration, config_path: Path) -> None:
    parser = ConfigParser()
    parser['DEFAULT'] = config.to_dict()
    with open(config_path, mode='w') as config_file:
        parser.write(config_file)


def generate_configuration_filename() -> str:
    return CONFIGURATION_FILE_TEMPLATE.format(uuid4_hex=uuid4().hex)


def search_for_alternative_config_file() -> Optional[Path]:
    curr_dir_config_file = next(Path().glob('courses_manager_config_*.ini'), None)
    if curr_dir_config_file:
        return curr_dir_config_file


def load_configuration(configuration_path: Optional[Path]) -> Configuration:
    if configuration_path is None or not configuration_path.is_file():
        alt_config_file = search_for_alternative_config_file()
        if alt_config_file:
            return load_configuration(alt_config_file)

        return create_default_configuration()

    parser = ConfigParser()
    parser.read(configuration_path)

    config_dict = dict(parser['DEFAULT'])
    config_dict['courses_file_path'] = Path(config_dict['courses_file_path'])
    config_dict['name_length'] = int(config_dict['name_length'])
    config_dict['grade_length'] = int(config_dict['grade_length'])
    config_dict['points_length'] = int(config_dict['points_length'])

    return Configuration.from_dict(config_dict)
