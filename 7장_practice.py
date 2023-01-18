# 7.1

birth_year=int(input('출생연도를 입력하세요 : '))
year_list=[year for year in range(birth_year, birth_year+5)]
print(year_list,'\n')

# 7.2

print('세번째 생일은',year_list[3],'년도 이다.\n')


# 7.3

print(f'가장 나이가 많은 연도는 {year_list[-1]}년도 이다.\n')

#7.4 , 7.5

things=['mozzarella','cinderella','salmonella']

things[1]=things[1].capitalize()

print(things,'\n')


# 7.6

things=[things[n].capitalize() for n in range(len(things))]

print(things,'\n')

# 7.7

things.remove('Salmonella') # 여기서 things = things.remove('Salmonella')를 하면 remove는 값을 반환하지 않으므로 things에 None이 들어감
print(things,'\n')

# OR del 사용

# del things[-1]


# 7.8 , 7.9

surprise=["Groucho","Chico","Harpo"]

# harpo=surprise[-1]
surprise[-1]=(surprise[-1].lower())[::-1].capitalize()

print(surprise,'\n')


# 7.10

even_list = [i for i in range(10) if i%2 == 0]
print(even_list,'\n')

# 7.11

start1 = ["fee","fie","foe"]
rhymes=[                        #튜플이 리스트 요소인 경우
    ("flop","get a mop"),
    ("fope","turn the rope"),
    ("fa","get your ma"),
    ("fudge","call the judge"),
    ("fat","pet the cat"),
    ("fog","walk the dog"),
    ("fun","say we're done")
]
start2="Someone better"


start1_str=' '.join([i.capitalize()+'! ' for i in start1])

for first, second in rhymes:
    print(f"{start1_str} {first.capitalize()+'! '}")
    print(f'{start2} {second}.')


