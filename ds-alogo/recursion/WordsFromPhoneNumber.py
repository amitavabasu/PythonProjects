def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    result = []
    helper(phone_number, 0, "", result)
    return result


def helper(phone_number, i, ps, results):
    #base-case
    if i == len(phone_number):
        results.append(ps)
        return
    else:
        if phone_number[i] == '0' or phone_number[i] == '1':
            helper(phone_number, i + 1, ps, results)
        elif phone_number[i] == '2':
            helper(phone_number, i + 1, ps+'a', results)
            helper(phone_number, i + 1, ps+'b', results)
            helper(phone_number, i + 1, ps+'c', results)
        elif phone_number[i] == '3':
            helper(phone_number, i + 1, ps+'d', results)
            helper(phone_number, i + 1, ps+'e', results)
            helper(phone_number, i + 1, ps+'f', results)
        elif phone_number[i] == '4':
            helper(phone_number, i + 1, ps+'g', results)
            helper(phone_number, i + 1, ps+'h', results)
            helper(phone_number, i + 1, ps+'i', results)
        elif phone_number[i] == '5':
            helper(phone_number, i + 1, ps+'j', results)
            helper(phone_number, i + 1, ps+'k', results)
            helper(phone_number, i + 1, ps+'l', results)
        elif phone_number[i] == '6':
            helper(phone_number, i + 1, ps+'m', results)
            helper(phone_number, i + 1, ps+'n', results)
            helper(phone_number, i + 1, ps+'o', results)
        elif phone_number[i] == '7':
            helper(phone_number, i + 1, ps+'p', results)
            helper(phone_number, i + 1, ps+'q', results)
            helper(phone_number, i + 1, ps+'r', results)
            helper(phone_number, i + 1, ps+'s', results)
        elif phone_number[i] == '8':
            helper(phone_number, i + 1, ps+'t', results)
            helper(phone_number, i + 1, ps+'u', results)
            helper(phone_number, i + 1, ps+'v', results)
        elif phone_number[i] == '9':
            helper(phone_number, i + 1, ps+'w', results)
            helper(phone_number, i + 1, ps+'x', results)
            helper(phone_number, i + 1, ps+'y', results)
            helper(phone_number, i + 1, ps+'z', results)

if __name__ == '__main__':
    print(get_words_from_phone_number("1010101"))