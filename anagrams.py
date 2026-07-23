words = ["tea", "eat","ate","tan", "nat","bat"]


def anagram(word_list):
    anagram_dict = {}
    for word in word_list:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return anagram_dict


print(anagram(words))
