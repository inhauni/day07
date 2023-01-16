start = 'na '*4+'\n'
middle = "hey "*3+'\n'
end = 'bye'

print(start+start+middle+end)

univ='Inha University'

print(univ[:])
print(univ[2:])
print(univ[5:15])
print(univ[-10:-6])

pokemon_list=['피카츄','라이츄','파이리']
pokemon_string='*'.join(pokemon_list)
print(pokemon_string)

subjects =' ! phython, data structure, database !   !!!'
print(subjects)
print(subjects.strip())
print(subjects.strip('!')) # 단, !앞에 공백이 존재하면 제거되지 않는다


subjects2='pyhton, data structure, database'
print(subjects2.find('data'),subjects.index('data'))
print(subjects2.find('inha'))


thing=98.6
print('%12.3f' % thing)


print('duck is'.title())

thing='wereduck'
place='werepond'
print(f'{thing = :>10.3}')
print(f'{thing[-3:-1]=}')


song="""When an eel grabs your arm,
And it causes great harm,
That's -a moray!"""


idx = song.rfind('m')
#song = song.replace(song[idx], song[idx].upper())

print(song)