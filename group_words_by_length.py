words = ["apple", "bat", "cat", "banana", "dog", "elephant"]


def sort_words_by_length(words):
    sorted_dict = {}
    for word in words:
        length = len(word)
        if length not in sorted_dict:
            sorted_dict[length] = []
        sorted_dict[length].append(word)
    return sorted_dict

anagram_dict = sort_words_by_length(words)
print(anagram_dict)