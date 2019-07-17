#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # store each weight in the input list as keys and
    # store each weight's list index as its value

    index = 0

    for item in weights:
        sum_weights = limit - item
        # check to see if the hash table contains an entry for weight
        existing_key = hash_table_retrieve(ht, item)

        if (existing_key == 0 or existing_key) and (limit - item == sum_weights):
            return (index, existing_key)
        hash_table_insert(ht, item, index)
        index += 1

    for item in weights:
        sum_weights = limit - item

        weight_index = hash_table_retrieve(ht, sum_weights)

        if weight_index is not None:
            current_index = hash_table_retrieve(ht, item)
            if current_index > weight_index:
                return (current_index, weight_index)
            else:
                return (weight_index, current_index)


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
