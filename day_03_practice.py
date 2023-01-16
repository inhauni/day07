#5.1

song="""When an eel grabs your arm,
And it causes great harm,
That's a - moray!"""

song_list=song.split()
song_list[14]=song_list[14].replace('m', 'M')
song=' '.join(song_list)
print(song,'\n\n')


# 5.2
questions=["We don't serve strings around here. Are you a string?",
           "what is said on Father's DAy in the forest?",
           "What makes the sound 'Sis! Boom! Bah!'?"]
answers=["An exploding sheep.",
         "No, I'm a frayed knot.",
         "'Pop!' goes the weasel."]
count=0
while count<len(questions):
    question=questions[count]
    answer=answers[count]
    note_list=[question,answer]
    note='\n:'.join(note_list)
    print(note, '\n')
    count += 1
    count += 1



# 5.3


print('''My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he\'s a %s.''' % ('roast beef','ham','head','clam'))




#5.4 & 5.5

letter ='''Dear {0} {1},

Thank you for your letter. We are sorry that our {2} {3} in your {4}. Please note that it should never be used in a {4},\
 especially near any  {5}.
 
Send us your receipt and {6} for shipping and handling. We will send you another {2} that, in our tests, \
is {7}% less likely to have {3}.

Thank you for your support.
Sincerely,
{8}
{9}'''

print(letter.format('salutation','name','product','verbed','room','animals','amount','percent','spokesman','job_title'))



# 5.6

eng='Boaty McDuckface'
aus='Horsey McGourdface'
swd='Trainy McSpitzface'

eng_m='%.4s' % eng
aus_m='%.5s' % aus
swd_m='%.5s' % swd

eng=eng.replace(eng_m, 'Duck')
aus=aus.replace(aus_m, 'Gourd')
swd=swd.replace(swd_m, 'Spitz')

print('\n\n%s\n%s\n%s\n\n' % (eng, aus, swd))


# 5.7

m1='duck'
m2='gourd'
m3='spitz'

print('{}y McDuckface\n{}y McGourdface\n{}y McSpitzface\n\n'.format(m1,m2,m3))


# 5.8

print(f'{m1}y McDuckface\n{m2}y McGourdface\n{m3}y McSpitzface\n\n')


