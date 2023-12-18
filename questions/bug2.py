"""
Question

Find the bug in compare_ints implementation.

When you run the __main__ you will see that it works well for some integers but not for all of them

Why it's so?
How to fix it?

"""


def compare_ints(in1: int, in2: int) -> bool:
    if not isinstance(in1, int) or not isinstance(in2, int):
        return False
    if in1 is in2:
        return True
    else:
        return False


if __name__ == "__main__":
    valid_test_cases = [(1, 1), (22, 22), (255, 255), (259, 259), (1000, 1000), (0, 0)]
    for test_in1, test_in2 in valid_test_cases:
        print(f"is {test_in1} equal to {test_in2}?, {compare_ints(test_in1, test_in2)}")
