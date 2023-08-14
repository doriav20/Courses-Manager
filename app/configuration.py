# configuration.py

from __future__ import annotations

from configparser import ConfigParser
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional
from uuid import uuid4

from constants import (
    DEFAULT_COURSES_FILE_PATH,
    DEFAULT_NAME_COLUMN_WIDTH,
    DEFAULT_YEAR_COLUMN_WIDTH,
    DEFAULT_SEMESTER_COLUMN_WIDTH,
    DEFAULT_GRADE_COLUMN_WIDTH,
    DEFAULT_POINTS_COLUMN_WIDTH,
    CONFIGURATION_FILE_TEMPLATE,
)


@dataclass
class Configuration:
    courses_file_path: Path
    name_column_width: int = DEFAULT_NAME_COLUMN_WIDTH
    year_column_width: int = DEFAULT_YEAR_COLUMN_WIDTH
    semester_column_width: int = DEFAULT_SEMESTER_COLUMN_WIDTH
    grade_column_width: int = DEFAULT_GRADE_COLUMN_WIDTH
    points_column_width: int = DEFAULT_POINTS_COLUMN_WIDTH

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
    config_dict['name_column_width'] = int(config_dict['name_column_width'])
    config_dict['year_column_width'] = int(config_dict['year_column_width'])
    config_dict['semester_column_width'] = int(config_dict['semester_column_width'])
    config_dict['grade_column_width'] = int(config_dict['grade_column_width'])
    config_dict['points_column_width'] = int(config_dict['points_column_width'])

    return Configuration.from_dict(config_dict)
