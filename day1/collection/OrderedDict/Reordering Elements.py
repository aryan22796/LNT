from collections import OrderedDict

ordered_dict = OrderedDict([('banana', 3), ('apple', 4), ('pear', 1)])
ordered_dict.move_to_end('banana')
print(ordered_dict)
