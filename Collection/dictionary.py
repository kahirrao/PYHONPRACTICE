my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'abc': 'value', 'k': 'k1', '10.5': '10.51'}
print(my_dict)
print(type(my_dict))
print(len(my_dict))
print(my_dict['one'])
print(my_dict.get('abc'))
my_dict['six'] = 6
print(my_dict)
my_dict.pop('k')
print(my_dict)
my_dict.update({'seven': 7, 'eight': 8})
print(my_dict)