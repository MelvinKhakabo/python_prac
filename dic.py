#create dictionary
bad_guys ={
    'daredevil' : 'kingpin',
    'x-men' : 'apocalypse',
    'batman' : 'bane'
}
# print(bad_guys)

# print(bad_guys['x-men'])

#add item
bad_guys['deadpool'] = "deadpool"
# print(bad_guys)

#update
# bad_guys['x-men'] = 'juggernaut'
# print(bad_guys)

#delete 
del bad_guys['deadpool']
print(bad_guys)