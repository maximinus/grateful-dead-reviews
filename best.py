#!/usr/bin/env python3

import datetime


MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


class Show:
    def __init__(self, score, date, review):
        self.score = score
        self.date = date
        self.review = review

    def __repr__(self):
        if self.date[0] < 10:
            day = f'0{self.date[0]}'
        else:
            day = str(self.date[0])
        text_date = f'{day}-{MONTHS[self.date[1] - 1]}-{self.date[2]}'
        return f'{self.score} {text_date} {self.review}'


def getScores():
    reviews = open('dead_reviews.txt').readlines()

    shows = []
    for i in reviews:
        data = i.split()
        if len(data) <= 2:
            continue
        date = data[0]
        score = data[1]
        try:
            review = ' '.join(data[2:])
        except:
            review = ''
        try:
            dates = date.split('-')
            day = int(dates[0])
            month = int(dates[1])
            year = int(dates[2])
            # only add 5's
            print(float(score))
            if float(score) > 4.6:
                shows.append(Show(score, [day, month, year], review))
        except:
            continue
    return shows


if __name__ == '__main__':
    scores = getScores()
    print(len(scores))
    for i in scores:
        print(i)
