"""
Provide an array of string, eg: ['a', 'ab', 'abc', 'cd', 'def', 'gh']. Write a
function to find the strings' length that appear most in this array. Write the
unit test function and provide some test cases. The result for the example array
is ['ab', 'cd', 'gh'].
"""


def f(
    L: list,
) -> list:
    counter = {}
    for item in L:
        if not counter.get(len(item)):
            counter[len(item)] = 0
        counter[len(item)] += 1

    # TODO: Change the implementation here to let it return an array of "lengths"
    required_length, appearance_count = max(
        counter.items(),
        key=lambda item: item[1]
    )
    satisfied_strings = [
        item
        for item in L
        if len(item) == required_length
    ]

    return satisfied_strings

def unit_test():
    test_inputs = [
        ["a", "ab", "abc", "cd", "def", "gh"],
        ["abc", "abcd", "bcd", "adbe", "a"],
        ["a", "b", "c", "d"],
    ]
    test_outputs = [
        ["ab", "cd", "gh"],
        ["abc", "abcd", "bcd", "adbe"],
        ["a", "b", "c", "d"],
    ]

    for test_input, test_output in zip(test_inputs, test_outputs):
        function_output = f(test_input)

        print(test_input)
        print(test_output)
        print(function_output)
        
        assert function_output == test_output

unit_test()
