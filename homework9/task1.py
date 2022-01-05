from contextlib import ExitStack
from itertools import chain
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Merge integers from a number of files into one iterator
    :param file_list: List of files to merge
    :return: Iterator with integers from specified files
    """
    with ExitStack() as stack:
        files = [
            stack.enter_context(open(file_name)) for file_name in file_list
        ]
        merged_list = []
        for lines in chain(*files):
            lines = lines.strip()
            merged_list.append(int(lines))
        return sorted(merged_list)
