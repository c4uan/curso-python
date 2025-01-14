# método copy - retorna uma cópia rasa (shallow copy)
# módulo copy - retorna uma cópia profunda(deep copy)
import copy
##
##

#shallow copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1' : [0, 1, 2],
}

d2 = d1.copy()
d2['l1'][1] = 999
print('Shallow copy:')
print(d1,"\n",d2)

print()


#deep copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1' : [0, 1, 2],
}

d2 = copy.deepcopy(d1)
d2['l1'][1] = 999

print('Deep copy:')
print(d1,"\n",d2)