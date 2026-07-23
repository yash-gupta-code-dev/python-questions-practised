s = "car"
t = "rac"


def character_frequency(string):
    map_dict = {}

    for char in string:
        if char not in map_dict:
            map_dict[char] = 1
        else :
            map_dict[char] += 1
    return map_dict

if character_frequency(s) == character_frequency(t):
    print("YES")
else:
    print("NO")