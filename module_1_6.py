my_dict = {'Amilia': 2011, 'Maxim': 2018, 'Anna': 2016, 'Esenia': 2015, 'Artem': 2017, 'Vadim': 2016}
print(my_dict)
print(my_dict['Maxim'])
print(my_dict.get('Sveta'))
my_dict.update({'Tatiana': 1982, 'Irina': 1989})
print(my_dict)
my_dict.pop('Anna')
print(my_dict)
a = my_dict.pop('Maxim')
print(a)
print()
my_set_ = {1,2,5,8, 'Песок', (2, 4, 6, 8,), False}
print(my_set_)
my_set_.add(2018)
my_set_.add('Груша')
print(my_set_)
my_set_.discard((2,4,6,8))
print(my_set_)