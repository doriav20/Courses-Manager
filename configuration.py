from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional
from uuid import uuid4


@dataclass
class Configuration:
    grades_file_path: Path
    name_length: int
    grade_length: int
    points_length: int

    @classmethod
    def from_dict(cls, config_dict: dict) -> Configuration:
        return cls(**config_dict)


def create_default_configuration() -> Configuration:
    config_filename = generate_configuration_filename()
    config_path = Path(config_filename)

    config_obj = Configuration(
        grades_file_path=config_path,
        name_length=30,
        grade_length=3,
        points_length=4,
    )
    save_configuration(config_obj, config_path)
    return config_obj


def save_configuration(config: Configuration, config_path: Path) -> None:
    with open(config_path, mode='w') as config_file:
        json.dump(asdict(config), config_file, sort_keys=True)


def generate_configuration_filename() -> str:
    return f'grades_manager_config_{uuid4().hex}.json'


def load_configuration(configuration_path: Optional[Path]) -> Configuration:
    if configuration_path is None or not configuration_path.is_file():
        return create_default_configuration()

    with open(configuration_path) as config_file:
        config_dict = json.load(config_file)
        return Configuration.from_dict(config_dict)
