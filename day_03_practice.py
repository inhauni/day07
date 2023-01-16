#Q2

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



#6.1

for k in [3,2,1,0]:
    print(k, end=' ')