from pathlib import Path
from datetime import datetime


def find_files(directory: Path, *, recursive: bool = True, pattern: str = '*') -> set[Path]:
    """
    Finds all files in a directory (and subdirectories) that match a pattern.
    :param directory: The directory to search in.
    :param recursive: Whether to search recursively or not.
    :param pattern: The pattern to match.
    :return: A set of files that match the pattern.
    """
    return set(directory.rglob(pattern)) if recursive else set(directory.glob(pattern))

def file_creation_month(file: Path) -> int:
    """
    Returns the month of creation of a file.
    :param file: The file to check.
    :return: The month of creation.
    """
    return date_from_float(file.stat().st_birthtime).month

def file_creation_year(file: Path) -> int:
    """
    Returns the year of creation of a file.
    :param file: The file to check.
    :return: The year of creation.
    """
    return date_from_float(file.stat().st_birthtime).year

def date_from_float(__value: float) -> datetime:
    """
    Converts a float to a datetime.
    :param __value: The float to convert.
    :return: The converted datetime.
    """
    return datetime.fromtimestamp(__value)

def move_path(__file: Path, __new_home_directory: Path) -> Path:
    """
    Moves a file to a new home directory.
    :param __file: The file to move.
    :param __new_home_directory: The new home directory.
    :return: The new path of the file.
    """
    year = file_creation_year(__file)
    month = file_creation_month(__file)
    return __new_home_directory / str(year) / str(month) / __file.name

def move_file(__file: Path, __new_home_directory) -> None:
    """
    Moves a file to a new home directory.
    :param __file: The file to move.
    :param __new_home_directory: The new home directory.
    """
    new_path = move_path(__file, __new_home_directory)
    if not new_path.parent.exists():
        new_path.parent.mkdir(parents=True)
    __file.rename(new_path)


if __name__ == "__main__":
    dir = Path('/Users/anmolgorakshakar/Pictures')
    files = find_files(dir, recursive=True, pattern='*.dng')
    print(move_path(files.pop(), Path('/Users/anmolgorakshakar/Desktop')))