from typing import List

def letter_combinations(digits: str) -> List[str]:
    """
    Generates all possible letter combinations from the input digits,
    following the mapping on a phone keypad (digits 2 to 9).
    
    :param digits: str - A string of digits (2-9)
    :return: List[str] - All possible letter combinations
    """
    if not digits:
        return []
    
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    result = []

    def backtrack(index: int, path: str):
        if index == len(digits):
            result.append(path)
            return
        for letter in phone_map[digits[index]]:
            backtrack(index + 1, path + letter)
    
    backtrack(0, "")
    return result

print(letter_combinations("23"))
