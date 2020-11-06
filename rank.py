#!/usr/bin/env python3

import random
import datetime


MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


class Show:
    def __init__(self, score, date):
        self.score = score
        self.date = date

    def __repr__(self):
        if self.date[0] < 10:
            day = f'0{self.date[0]}'
        else:
            day = str(self.date[0])
        if self.date[1] < 10:
            month = f'0{self.date[1]}'
        else:
            month = str(self.date[1])
        sc_txt = str(self.score)
        size = len(sc_txt)
        if size == 3:
            final = sc_txt
        elif size == 2:
            final = f' {sc_txt}'
        else:
            final = f'  {sc_txt}'
        text_date = f'{day}-{month}-{self.date[2]}'
        return f'{text_date} {final}'


def getScores():
    reviews = open('new_list.txt').readlines()

    shows = []
    for i in reviews:
        # only interested in lines where chars 2 and 5 are a -
        if len(i) < 8:
            continue
        if not (i[2] == '-' and i[5] == '-'):
            continue
        # make sure it's a real review
        data = i.split()
        if len(data[1]) != 2:
            continue
        if data[1] == '??':
            # ignore unrated
            continue

        date = data[0]
        score = data[1]
        try:
            dates = date.split('-')
            day = int(dates[0])
            month = int(dates[1])
            year = int(dates[2])
            shows.append(Show(score, [day, month, year]))
        except:
            pass
    return shows


if __name__ == '__main__':
    scores = getScores()
    for i in scores:
        print(i)
