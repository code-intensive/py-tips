def string_reversal_method_1(value: str) -> str:
    reverse = []
    for val in value:
        reverse.insert(0, val)
    return ''.join(reverse)

def string_reversal_method_2(value: str) -> str:
    return reduce(lambda a, b: ''.join([b, a]), value)

def string_reversal_method_3(value: str) -> str:
    value_as_list = [val for val in value]
    value_as_list.reverse()
    return ''.join(value_as_list)

def string_reversal_method_4(value: str) -> str:
    return value[::-1]
