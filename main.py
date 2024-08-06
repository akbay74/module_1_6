# Работа со словарями
my_dict = {'Ivan': 2001, 'Sasha': 1999,
           'Alex': 2003, 'Anna': 2008}
print(my_dict)
print(my_dict['Sasha'])
my_dict['Alla'] = 1998
print(my_dict['Alla'])
my_dict.update({'Sveta': 2006,
                'Misha': 1995})
print(my_dict)
del my_dict['Alex']
print(my_dict)

# Работа с множествами
my_set = {1, 2, 3, 1, 1, 5}
print(my_set)
my_set.add(7)
my_set.add(8)
print(my_set)
my_set.discard(1)
print(my_set)
