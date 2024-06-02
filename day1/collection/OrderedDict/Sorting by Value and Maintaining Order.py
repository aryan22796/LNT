from collections import OrderedDict
ordered_dict = OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
sorted_dict = OrderedDict(sorted(ordered_dict.items(), key=lambda x: x[1]))
print(sorted_dict)