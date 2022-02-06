"""
A product can be made of multiple parts, which themselves can be made of more parts. Given a final product and
a dictionary of key-value pairs, where the product is the key and a list of parts are the values, write a function to
return the count of each part that is needed to construct the final product.

parts = {
        'A': ['B', 'B', 'C'],
        'B': [],
        'C': ['D','E','F'],
        'D': [],
        'E': ['B','D'],
        'F': []
}

Ex: 'A' => {'B': 3, 'D': 2, 'F': 1} i.e. 3 Parts of B, 2 Parts of D and 1 Part of F
Ex: 'F' => {'F': 1}
"""

from collections import Counter


def parts_of_parts_recursive(prod, total_parts, parts):
    if prod in parts:
        part = parts[prod]
        if len(part) == 0:
            total_parts.append(prod)
            return

        for i in range(len(part)):
            parts_of_parts_recursive(part[i], total_parts, parts)

    return


def parts_of_parts_rec(prod, parts):
    total_parts = []
    parts_of_parts_recursive(prod, total_parts, parts)

    total_parts_map = dict()
    for t in total_parts:
        total_parts_map[t] = total_parts_map.get(t, 0) + 1

    return total_parts_map


if __name__ == "__main__":
    prod_parts = {
        'A': ['B', 'B', 'C'],
        'B': [],
        'C': ['D', 'E', 'F'],
        'D': [],
        'E': ['B', 'D'],
        'F': []
    }

    print(parts_of_parts_rec('A', prod_parts))
