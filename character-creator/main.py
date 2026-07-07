full_dot = '●'
empty_dot = '○'


def main():
    print("Running program")
    print(create_character("Luke", 4, 2, 1))


def create_character(character_name, strength, intelligence, charisma):

    if not isinstance(character_name, str):
        return "The character name should be a string"

    if character_name == "":
        return "The character should have a name"

    if len(character_name) > 10:
        return "The character name is too long"

    if " " in character_name:
        return "The character name should not contain spaces"

    stats = [strength, intelligence, charisma]
    total = 0
    for stat in stats:

        if not isinstance(stat, int):
            return "All stats should be integers"

        if stat < 1:
            return "All stats should be no less than 1"

        if stat > 4:
            return "All stats should be no more than 4"
        total += stat

    if total != 7:
        return "The character should start with 7 points"
    
    result = character_name + "\nSTR " + full_dot * strength + empty_dot * (10 - strength) + "\nINT " + full_dot * intelligence + empty_dot * (10 - intelligence) + "\nCHA " + full_dot * charisma + empty_dot * (10 - charisma)
    return result

if __name__ == "__main__":
    main()
