import os
from dataclasses import dataclass, field
from typing import List, Dict


class FileError(Exception):
    """Base error"""


class FileValueError(FileError):
    """Error raised due wrong type parsing"""


class FileInceptionError(FileError):
    """Yeah! maybe you will stay in a loop of dreams forever"""


@dataclass
class FileStats:
    path: str = None
    sum_numbers: float = 0.0
    total_sum: float = 0.0
    completed_path: List[str] = field(default_factory=list)
    exceptions: List[Exception] = field(default_factory=list)


def parse_line(data):
    try:
        data = data.strip()
        data = float(data)
    except (ValueError, AttributeError):
        # In case of being a path
        if isinstance(data, (bytes, bytearray)):
            return data.decode("utf-8")
    return data


def file_exists(filename):
    if not isinstance(filename, str):
        raise FileValueError(f"Filename {filename} is not a str")
    return os.path.exists(filename)


def read_file(
        filename: str,
        files: Dict[str, FileStats],
        completed_path: List[str] = []):
    """
    Function that reads a file and inner files, summing up all the values
    """
    if filename in completed_path:
        raise FileInceptionError(
            f"{completed_path} + {filename} will create an infinite loop"
        )
    if filename in files:
        # It's not necessary to calculate again
        return files[filename].total_sum, files[filename].completed_path

    file_stats = FileStats(path=filename, completed_path=[filename])
    files[filename] = file_stats
    with open(filename, "rb") as f:
        for line in f:
            try:
                line = parse_line(line)
                if isinstance(line, float):
                    file_stats.sum_numbers += line
                elif file_exists(line):
                    new_total_sum, new_completed_path = read_file(
                        line, files, file_stats.completed_path
                    )
                    file_stats.total_sum += new_total_sum
                    file_stats.completed_path += new_completed_path
            except FileError as e:
                file_stats.exceptions.append(e)
        file_stats.total_sum += file_stats.sum_numbers
        return file_stats.total_sum, file_stats.completed_path
