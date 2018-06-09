import random
from Testing.Card_Deck.deck import Deck
from Testing.Sorting.algorithms import SortAlgorithms


def main():
    to_sort = [x for x in range(20)]
    random.shuffle(to_sort)

    sorting = SortAlgorithms(to_sort)

    print("Before sorting the array:\n{}".format(to_sort))
    sorting.merge_sort(sorting.to_sort)
    print("After sorting the array:\n{}".format(to_sort))

    COLORS = ['D', 'H', 'C', 'S']
    CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    JOCKERS = ['RJ', 'BJ']

    deck_obj = Deck(COLORS, CARDS, JOCKERS)
    deck_obj.build_deck()

    print("Cards number in our deck is: {}".format(len(deck_obj.structure)))
    print("Random card from our deck: {}".format(deck_obj.get_card()))


if __name__ == '__main__':
    main()