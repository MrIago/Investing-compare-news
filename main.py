'''
import functions

n = int(input("Number of news together: "))
news = functions.news(n)

s = "n in news.news[0] "
for index in range(n):
    text = "and n in news.news["+str(index)+"] "
    s += text
    print(s)

i = 0
for n in news.news[0]:
    if n in news.news[1]:
        print(n)
    i += 1
'''

import functions

n = int(input("Number of news together: "))
news = functions.news(n)

i = 0
s = "n in news.news[0] "
for index in range(n):
    text = "and n in news.news["+str(index)+"] "
    s += text
    print(s)

for n in news.news[0]:
    check = eval(s)
    if check:
        print(n)
    i += 1
