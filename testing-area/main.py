def main():
    #print(number_pattern(4))
    #print(number_pattern(0))
    
    key_value_pair = ('theme', 'dark')
    key, value = key_value_pair
    print(key)
    print(value)

    test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
    }
    for key, value in  test_settings.items():
        print(str(key) + " : " + str(value))

    
def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    result = ""
    for num in range(1,n+1):
        result += str(num)

        if not num == n:
            result += " "

    return result


if __name__ == "__main__":
    main()