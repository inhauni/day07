# 8. 1

e2f={
    'dog':'chien',
    'cat' : 'chat',
    'walrus' : 'morse'
}

print(e2f,'\n')

# 8.2

print(f"warlus는 프랑스어로 {e2f['walrus']}이다. \n")

# 8.3


f2e={fre:eng for eng,fre in e2f.items()}

print(f2e,'\n')


# 8.4

for eng,fre in e2f.items():
    if fre == 'chien':
        print(eng,'\n')
    else:
        continue


# 8.5

print(list(e2f.keys()))
print(set(e2f.keys()),'\n')


#8.6

# life_under={
#     'cats':'Henri',
#     'octopi':'Grumpy',
#     'emus':'Lucy'
# }
# life={
#     'animals':life_under,
#     'plants':'',
#     'other':''
# }


life={
    'animals':{
        'cats':{'Henri', 'Grumpy','Lucy'},
        'octopi':{},
        'emus':{}
    },
    'plants':{},
    'other':{}
}
print(life,'\n')


# 8.7

print(list(life.keys()),'\n')

# 8.8

print( list ((life['animals']).keys()),'\n')

# 8.9

print( list((life['animals'])['cats']) ,'\n')

# 8.10

squares={i:i*i for i in range(10)}
print(squares,'\n')

# 8.11

set_odd={i for i in range(10) if i % 2 == 1}
print(set_odd,'\n')

# 8.13

d_key='optimist','perssimist','troll'
d_value='The glass is half full','The glass is half empty','How did you get a glass?'

d_dict=dict(zip(d_key,d_value))

print(d_dict,'\n')


# 8.14

titles=['Creature of Habit','Crewel Fate']
plots =['A nun turns into a monster','A haunted yarn shop']

movies=dict(zip(titles,plots))
print(movies)