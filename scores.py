
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
for i in years:
    if len(i) > 0:
        print('{0}: {1}'.format(year + 65, sum(years[year]) / len(years[year])))
        print('    {0} *****'.format(years[year].count(float(5))))
        print('    {0} ****-'.format(years[year].count(float(4.5))))
        print('    {0} **** '.format(years[year].count(float(4))))
    year += 1
