def phoneword(phonenumber: str):
    """
      Return all phone words respective to a phone number
    :param:
    :phonenumber: str
    :return: list[str] with all phone words
    """
    digit_chars = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    size_phonenumber = len(phonenumber)

    def phoneword_rec(previous_result, current_index):
        if current_index == size_phonenumber:
            return previous_result

        character = phonenumber[current_index]
        results = []
        for char in digit_chars[character]:
            results.extend(prev_result+char for prev_result in previous_result)

        return phoneword_rec(results, current_index + 1)

    return phoneword_rec([''], 0)


print(phoneword(''))
print(phoneword('736'))
