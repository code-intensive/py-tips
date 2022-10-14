from bisect import bisect
from typing import Any, Dict, List

from time import perf_counter


def took_how_long(function, *args, **kwargs) -> None:
    """ helper function to get time of execution """
    start = perf_counter()
    function(*args, **kwargs)
    print(perf_counter() - start)

# It is possible to achieve this using the below algorithm but
# this could be a poor solution in terms of code reusability
# depending on the scenario it could do the trick
def calculate_grade(grade: int) -> str:
    if grade > 74:
        return 'A1'
    if grade > 69:
        return 'B2'
    if grade > 64:
        return 'B3'
    if grade > 59:
        return 'C4'
    if grade > 54:
        return 'C5'
    if grade > 49:
        return 'C6'
    if grade > 44:
        return 'D7'
    if grade > 39:
        return 'E8'
    return 'F9'

# We could make this cleaner and faster by leveraging the builtin bisect module

# A static approach using bisect
# We create a list of breakpoints, these must strictly match the grades
# and must be sorted in ascending order

breakpoints = [0, 40, 45, 50, 55, 60, 65, 70, 75]
grades = ['F9', 'E8', 'D7', 'C6', 'C5', 'C4', 'B3', 'B2', 'A1']


def grade_using_bisect_by_list(score: int, *, breakpoints: List[int], grades: List[str]) -> str:
    grade = bisect(breakpoints, score) - 1
    return grades[grade]

# Here is a dynamic approach, grade mapping can be updated dynamically
# We create a mapping of scores to grades

grade_map = {
    'F9': 0,
    'E8': 40,
    'C4': 60,
    'C6': 50,
    'C5': 55,
    'A1': 75,
    'B3': 65,
    'D7': 45,
    'B2': 70,
}

# def grade_using_bisect_by_dict(score: int, *,
#                                grade_map: Dict[str, int], key=lambda x: x[1],
#                                requires_sorting=False) -> str:
#     if requires_sorting:
#         sorted(grade_map, key=key)

#     grades = list(grade_map.keys())
#     breakpoints = list(grade_map.values())
#     grade = bisect(breakpoints, score) - 1
#     return grades[grade]


def grade_using_bisect_by_dict(score: int, *,
                               grade_map: Dict[str, Any],
                               requires_sorting=False, key=None) -> str:
    if requires_sorting:
        assert key is not None, (
            'key is required to perform sorting'
        )
        sorted(grade_map, key=key)

    grades = list(grade_map.keys())
    breakpoints = list(grade_map.values())
    grade = bisect(breakpoints, score) - 1
    return grades[grade]

took_how_long(calculate_grade, grade=75)
took_how_long(grade_using_bisect_by_dict, score=75, grade_map=grade_map)
took_how_long(grade_using_bisect_by_list, score=75, breakpoints=breakpoints, grades=grades)
