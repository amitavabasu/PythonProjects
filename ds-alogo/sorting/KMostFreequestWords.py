"""
Asymptotic complexity in terms of the length of `words` ( = `n`):
* Time: O(n * log(n)).
* Auxiliary space: O(n).
* Total space: O(n).
"""

def k_most_frequent(k, words):
    words_frequency = {}
    for word in words:
        if word not in words_frequency:
            words_frequency[word] = 0
        else:
            words_frequency[word] += 1
    sorted_words_by_frequency = sorted(words_frequency.items(), key=lambda item: [-item[1], item[0]], reverse=False)
    to_k_words_by_frequency = (item[0] for item in sorted_words_by_frequency[:k])
    return list(to_k_words_by_frequency)


if __name__ == '__main__':
    words = ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
    print(words)
    result = k_most_frequent(4, words)
    print(result)