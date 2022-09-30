
![Screenshot 2022-09-30 at 00 59 47](https://user-images.githubusercontent.com/57086233/193174173-9ae83137-3d78-44d8-ac26-d493d04624da.png)

```python

# A good example of where bisect can be used is the school grading system
# Say we graded students based on their performance
# Using the Nigerian secondary school grading


from bisect import bisect
from typing import Dict, List

# It is possible to achieve this using the below algorithm
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

print(calculate_grade(75))

# We could make this cleaner and faster by leveraging the builtin bisect module

# A static approach using bisect
# We create a list of breakpoints, these must strictly match the grades
# and must be sorted in ascending order

breakpoints = [0, 40, 45, 50, 55, 60, 65, 70, 75]
grades = ['F9', 'E8', 'D7', 'C6', 'C5', 'C4', 'B3', 'B2', 'A1']


def grade_using_bisect_by_list(score: int, *, breakpoints: List[int], grades: List[str]) -> str:
    grade = bisect(breakpoints, score) - 1
    return grades[grade]

print(grade_using_bisect_by_list(75, breakpoints=breakpoints, grades=grades))


# Here is a dynamic approach, grade mapping can be updated dynamically
# We create a mapping of scores to grades

grade_map = {
    'F9': 0,
    'E8': 40,
    'D7': 45,
    'C6': 50,
    'C5': 55,
    'C4': 60,
    'B3': 65,
    'B2': 70,
    'A1': 75,
}

grade_map.update({'A0': 85})

def grade_using_bisect_by_dict(score: int, *, grade_map: Dict[str, int], key=lambda x: x[1], requires_sorting=False) -> str:
    if requires_sorting:
        sorted(grade_map, key=key)

    grades = list(grade_map.keys())
    breakpoints = list(grade_map.values())
    grade = bisect(breakpoints, score) - 1
    return grades[grade]

print(grade_using_bisect_by_dict(95, grade_map=grade_map, requires_sorting=True))

```
