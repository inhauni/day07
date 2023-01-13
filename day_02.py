import random
limits=20
tweets = "pass" * random.randint(1, 10)
diff = limits -len(tweets)
if diff >=0:
    print(tweets)
else:
    print(f'글자수 {abs(diff)} 초과')