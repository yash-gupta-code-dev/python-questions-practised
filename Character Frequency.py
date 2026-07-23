text = "programming"

def calculate_character_frequency(text):
    character_frequency = {}
    for character in text:
        if character not in character_frequency:
            character_frequency[character] = 1
        else:
            character_frequency[character] += 1

    return character_frequency
character_frequency = calculate_character_frequency(text)
print(character_frequency)



