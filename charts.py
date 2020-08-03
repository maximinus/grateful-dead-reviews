#!/usr/bin/env python3

import pygal
import datetime

class Show:
    def __init__(self, score, date):
        self.score = score
        self.date = date

def getScores():
    reviews = open('dead_reviews.txt').readlines()

    years = [[] for x in range(31)]
    for i in reviews:
        data = i.split()
        if len(data) <= 2:
            continue
        date = data[0]
        score = data[1]
        try:
            dates = date.split('-')
            day = int(dates[0])
            month = int(dates[1])
            year = int(dates[2]) + 1900
            # form a datetime from this
            years[int(date.split('-')[-1]) - 65].append(float(score))
        except Exception as ex:
            continue
    return years



def average(scores):
    results = []
    avg_range = 40
    start = -avg_range
    end = avg_range
    for i in range(len(scores)):
        if start < 0:
            values = scores[0:end]
        elif end >= len(scores):
            values = scores[start:]
        else:
            values = scores[start:end]
        avg_score = float(sum(values)) / float(len(values))
        results.append(avg_score)
        start += 1
        end += 1
    return results


if __name__ == '__main__':
    scores = getScores()
    flattened_scores = scores.pop(0)
    for i in scores:
        flattened_scores.extend(i)

    averaged = average(flattened_scores)

    #line_chart = pygal.Line()
    #line_chart.title = 'Browser usage evolution (in %)'
    #line_chart.x_labels = map(str, range(2002, 2013))
    #line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    #line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    #line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    #line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    
    #line_chart = pygal.Line()
    line_chart = pygal.Line()
    line_chart.title = 'Show Ratings'
    #line_chart.x_labels = map(str, range(0, len(flattened_scores)))
    line_chart.add('Rating', averaged)
    line_chart.render_to_file('chart3.svg')

    print(float(sum(flattened_scores)) / float(len(flattened_scores)))
