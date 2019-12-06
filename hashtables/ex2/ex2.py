#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    i = 0
    curr = 'NONE'
    while i < length:
        route[i] = hash_table_retrieve(hashtable, curr)
        curr = route[i]
        i += 1

    return route