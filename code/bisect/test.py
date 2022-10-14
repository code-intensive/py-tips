from code import grade_using_bisect_by_dict, took_how_long

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
took_how_long(grade_using_bisect_by_dict, score=55, grade_map=grade_map)