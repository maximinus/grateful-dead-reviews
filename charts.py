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


def getAverage():
    scores = getScores()
    flattened_scores = scores.pop(0)
    for i in scores:
        flattened_scores.extend(i)

    averaged = average(flattened_scores)
    line_chart = pygal.Line()
    line_chart.title = 'Show Rating, 40 show moving average'
    line_chart.show_legend = False
    line_chart.human_readable = True
    line_chart.x_labels = map(str, range(65, 96))
    line_chart.add('Rating', averaged)
    line_chart.render_to_file('chart3.svg')


def getYears():
    scores = getScores()
    # get average per year
    avg_years = []
    for i in scores:
        avg_years.append(sum([float(x) for x in i]) / len(i))

    bar_chart = pygal.Line(range=(2.6, 4.6))
    bar_chart.title = 'Average Score Per Year'
    bar_chart.add('Score', avg_years)
    bar_chart.show_legend = False
    bar_chart.human_readable = True
    bar_chart.render_to_file('years.svg')


def getStacked():
    scores = getScores()
    # get per year
    years = []
    for i in scores:
        total = [0 for x in range(9)]
        for j in i:
            single_score = int(j * 2) - 2
            total[single_score] += 1
        years.append(total)
    # we need these as a %
    new_years = []
    for i in years:
        total = sum(i)
        new_years.append([(float(x) / float(total)) * 100 for x in i])
    years = new_years

    bar_chart = pygal.StackedBar()
    bar_chart.title = 'Rating Types % / Year'
    bar_chart.x_labels = map(str, range(65, 96))
    bar_chart.add('1.0', [x[0] for x in years])
    bar_chart.add('1.5', [x[1] for x in years])
    bar_chart.add('2.0', [x[2] for x in years])
    bar_chart.add('2.5', [x[3] for x in years])
    bar_chart.add('3.0', [x[4] for x in years])
    bar_chart.add('3.5', [x[5] for x in years])
    bar_chart.add('4.0', [x[6] for x in years])
    bar_chart.add('4.5', [x[7] for x in years])
    bar_chart.add('5.0', [x[8] for x in years])
    bar_chart.human_readable = True
    bar_chart.render_to_file('stacked_years.svg')


if __name__ == '__main__':
    getAverage()
    getYears()
    getStacked()
