def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

print(add_item("Tea"), add_item("Vada"))