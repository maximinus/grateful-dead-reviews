#!/usr/bin/env python3

# display the average scores

reviews = open('dead_reviews.txt').readlines()

years = [[] for x in range(31)]

for i in reviews:
    data = i.split()
    if len(data) <= 2:
        continue
    date = data[0]
    score = data[1]
    try:
        years[int(date.split('-')[-1]) - 65].append(float(score))
    except:
        continue

# add up scores etc
year = 0
tops = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in years:
    if len(i) > 0:
        print('{0}: {1}'.format(year + 65, sum(years[year]) / len(years[year])))
        print('    {0} *****'.format(years[year].count(float(5))))
        tops[0] += years[year].count(float(5))
        print('    {0} ****-'.format(years[year].count(float(4.5))))
        tops[1] += years[year].count(float(4.5))
        print('    {0} **** '.format(years[year].count(float(4))))
        tops[2] += years[year].count(float(4))
        tops[3] += years[year].count(float(3.5))
        tops[4] += years[year].count(float(3))
        tops[5] += years[year].count(float(2.5))
        tops[6] += years[year].count(float(2))
        tops[7] += years[year].count(float(1.5))
        tops[8] += years[year].count(float(1))
    year += 1
print('\nTotal Top Rated:')
print(f'  ***** {tops[0]}')
print(f'  ****- {tops[1]}')
print(f'  ****  {tops[2]}')
print(f'  ***-  {tops[3]}')
print(f'  ***   {tops[4]}')
print(f'  **-   {tops[5]}')
print(f'  **    {tops[6]}')
print(f'  *-    {tops[7]}')
print(f'  *     {tops[8]}')
