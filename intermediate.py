# x = 2 ** 3
# print(x)

# z = math.pow(2, 3)
# print(z)

# z = math.sqrt(4)
# z = 4 ** 0.5
# print(z)


# e = int('101010', 2)
# print(e)

# a = 3
# a += 1
# print(a)

# x = "Peyman"
# print(len(x))

# a = """this
# is a multi-line
# string literal.
# """
# print(a)


# name = r"Peyman\nBarjoueian"
# print(name)


# txt = "banana"

# x = txt.center(30)

# print(x, "is my favorite fruit.")


def find_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        if number >= maximum:
            maximum = number
        if number <= minimum:
            minimum = number
    return minimum, maximum


number_list = [10, 2, 5, 4, 1]
print(find_min_max(numbers=number_list))


# city = 'Vienna'
# temperature = 23


# print(f"weather in {city}: {temperature}°C")

# rather obsolete
# print('weather in %s: %f°C' % (city, temperature))

# 'weather in {0}: {1}°C'.format(city, temperature)
# 'weather in {}: {}°C'.format(city, temperature)
# print('weather in {c}: {t}°C'.format(c=city, t=temperature))

# f'weather in {city}: {temperature}°C'
