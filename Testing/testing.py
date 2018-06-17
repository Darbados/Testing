import random
import asyncio
import math
import re
import numpy as np
import os
from Testing.Card_Deck.deck import Deck
from Testing.Sorting.algorithms import SortAlgorithms
from Testing.Classes.class_testing import Name


def main():
    to_sort = [x for x in range(20)]
    random.shuffle(to_sort)

    sorting = SortAlgorithms(to_sort)

    print("Before sorting the array:\n{}".format(to_sort))
    sorting.bubble_sort(sorting.to_sort)
    print("After sorting the array:\n{}".format(to_sort))

    COLORS = ['D', 'H', 'C', 'S']
    CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    JOCKERS = ['RJ', 'BJ']

    deck_obj = Deck(COLORS, CARDS, JOCKERS)
    deck_obj.build_deck()

    print("Cards number in our deck is: {}".format(len(deck_obj.structure)))
    print("Random card from our deck: {}".format(deck_obj.get_card()))

    my_name = Name("Pesho")
    print("The length of {0}, is {1} chars.".format(my_name.name, my_name.length))

    numpy_array = np.array([0])
    print(numpy_array)


async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


def factoriel(n):
    if n is 1:
        return n
    else:
        return n*factoriel(n-1)


def create_dict_from_1_to_n(n):
    return {n: n * n for n in range(1, n+1)}


def create_list_tuple(input):
    list_elements = input.split(',')
    tuple_element = tuple(list_elements)

    print("{0}\n{1}".format(list_elements, tuple_element))


def calculate_from_input():
    c = 50
    h = 30

    input_data = input("Please enter some integers/decimals by ',' separate: ")
    numbers = input_data.split(',')
    calculated = [int(round(math.sqrt((2 * c * float(x))/h))) for x in numbers]
    print(', '.join(map(lambda y: str(y), calculated)))


def two_dimensional_array():
    dimensions = input("Enter X,Y values (',' separated): ").split(',')
    rows_number = int(dimensions[0])
    cols_number = int(dimensions[1])

    matrix = [[y*x for y in range(cols_number)] for x in range(rows_number)]

    print(matrix)


def sort_words():
    words = input("Enter some words ',' separated: ")
    words_array = words.split(',')
    words_array.sort()

    print("The words sequence sorted: {}".format(','.join([w for w in words_array])))


def upper_lines():
    input_lines = []

    print("Write any kind of text you want:")

    while True:
        line = input()
        if line:
            input_lines.append(line)
        else:
            break

    print('\n'.join([line.upper() for line in input_lines]))


def all_even():
    output_numbers = []

    for number in range(1000,3001):
        digits = [int(x) for x in str(number)]

        if all(x % 2 == 0 for x in digits):
            output_numbers.append(number)

    print(','.join([str(el) for el in output_numbers]))


def calc_digits_letters():
    sentence = input("Enter a sentence: ")

    symbols = {'digits': len([d for d in sentence if d.isdigit()]),
               'letters': len([l for l in sentence if l.isalpha()])}

    print("Digits:{0}\nLetters:{1}".format(symbols['digits'], symbols['letters']))


def calc_sum_of_numbers():
    number = input("Enter a number: ")
    number1 = int(number)
    number2 = int("{0}{1}".format(number1, number1))
    number3 = int("{0}{1}{2}".format(number1, number1, number1))
    number4 = int("{0}{1}{2}{3}".format(number1, number1, number1, number1))
    sum_numbers = number1+number2+number3+number4

    print("{0}+{1}+{2}+{3}={4}".format(number1,number2,number3,number4,sum_numbers))


def check_symbol():
    text = "Some/*-*/@!text"
    print(re.search(r'/*-*/', text))


def elements_of_target(array, target):
    diff = set()

    for el in range(len(array)):
        temp_el = target - array[el]
        if temp_el in diff:
            return array.index(array[el]), array.index(temp_el)
        diff.add(temp_el)
    else:
        return "There are no numbers with sum() = {}".format(target)


def list_files(start_path):
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))


def power_function(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        temp = base
        while exp > 1:
            temp *= base
            exp = exp - 1
        return temp


if __name__ == '__main__':
    #check_symbol()
    main()

    # Solving some python interview tasks
    result = [number for number in range(2000, 3201) if number % 7 == 0 and number % 5 != 0]
    print(', '.join(map(lambda x: str(x), result)))

    number = 8
    print("Factoriel of {0} is {1}".format(number, factoriel(number)))

    print("Dict from 1 to {0} is {1}".format(8, create_dict_from_1_to_n(8)))

    sequence = "1,2,4,6,8,10"
    print("List and tuple from a sequence: {}".format(sequence))
    # create_list_tuple(sequence)

    # simple_class = SimpleClass()
    # simple_class.get_string()
    # simple_class.print_upper()

    # calculate_from_input()

    # two_dimensional_array()

    # sort_words()

    # upper_lines()

    # all_even()

    # calc_digits_letters()

    #calc_sum_of_numbers()__file__

    a = [7,0,5,6,1,2,7]
    a = iter(a)
    print(next(a))
    print(next(a))

    # list_files('/home/pesho-ubuntu/Projects/Testing-Python')
    print(power_function(2, 5))
