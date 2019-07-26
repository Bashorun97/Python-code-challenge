def counter(intake):
    digit_count, alpha_count = 0, 0
    for i in intake:
        if i.isdigit():
            digit_count += 1
        elif i.isalpha():
            alpha_count += 1
    return digit_count, alpha_count


if __name__ == '__main__':
    intake = input('Enter input: ')
print(counter(intake))
