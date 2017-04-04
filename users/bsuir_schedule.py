#!/usr/bin/env python3

from xml.dom import minidom
from datetime import date, timedelta

SUBGROUP = '2'
CUR_WEEK = 4 - 1
START_DATE = date.today()
END_DATE = START_DATE + timedelta(days=1)

schedule = None


def add_attr(lesson, dom, attr_name):
    attr = dom.getElementsByTagName(attr_name)
    lesson[attr_name] = attr[0].childNodes[0].data if attr else None


def parse():
    global schedule
    schedule = [[[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []],
                [[], [], [], [], []]]
    schedxml = open('users/sched.xml').read()
    schedxml.replace('<weekNumber>0</weekNumber>', '')
    xmldoc = minidom.parseString(schedxml)
    weekdays = xmldoc.getElementsByTagName('scheduleModel')
    for day_num, day_dom in enumerate(weekdays):
        lessons_dom = day_dom.getElementsByTagName('schedule')
        for lesson_dom in lessons_dom:
            subgroup = lesson_dom.getElementsByTagName(
                'numSubgroup')[0].childNodes[0].data

            if not (subgroup == '0' or subgroup == SUBGROUP):
                continue

            lesson = {}

            add_attr(lesson, lesson_dom, 'auditory')
            add_attr(lesson, lesson_dom, 'lessonTime')
            add_attr(lesson, lesson_dom, 'lessonType')
            add_attr(lesson, lesson_dom, 'subject')
            add_attr(lesson, lesson_dom, 'numSubgroup')

            employee = lesson_dom.getElementsByTagName('employee')
            lesson['teacher'] = employee[0].getElementsByTagName('lastName')[
                0].childNodes[0].data if employee else None

            weeks = lesson_dom.getElementsByTagName('weekNumber')
            for week in weeks:
                week_num = int(week.childNodes[0].data) - 1
                schedule[week_num][day_num].append(lesson)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_html():
    parse()
    html = ''
    week_num = CUR_WEEK
    for date in daterange(START_DATE, END_DATE):
        weekday = date.weekday()
        if weekday == 5:
            week_num = (week_num + 1) % 4
        if weekday > 4:
            continue
        html += '<ul>'
        for lesson in schedule[week_num][weekday]:
            html += "<li>{lessonType}: {time} {place} {subject} ({prep})</li>".format(
                lessonType=lesson['lessonType'],
                place=lesson['auditory'] or '',
                subject=lesson['subject'],
                prep=lesson['teacher'],
                time=lesson['lessonTime']
            )
        html += '</ul>'
    return html

if __name__ == '__main__':
    print(get_html())
