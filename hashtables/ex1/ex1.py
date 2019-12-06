#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)    

    for i, v in enumerate(weights):
        if hash_table_retrieve(ht, v) is not None:
            pair = limit - v
            if hash_table_retrieve(ht, pair) is not None:
                index = hash_table_retrieve(ht, pair)
                if i >= index:
                    return (i, index)
                else:
                    return (index, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

