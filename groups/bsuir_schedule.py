#!/usr/bin/env python3

import requests
from xml.dom import minidom
from datetime import date, timedelta

CUR_DATE = None
CUR_WEEK = None

class Schedule:
    SCHEDULE_URL = "https://www.bsuir.by/schedule/rest/schedule/%s"

    DAYS = {
        'Понедельник': 0,
        'Вторник':     1,
        'Среда':       2,
        'Четверг':     3,
        'Пятница':     4,
        'Суббота':     5,
    }

    # self.schedule[week][day]
    schedule = [[[], [], [], [], [], []],
                [[], [], [], [], [], []],
                [[], [], [], [], [], []],
                [[], [], [], [], [], []]]

    def __init__(self, group_number):
        self.schedule_respond = requests.get(self.SCHEDULE_URL % group_number)

    def parse(self):
        self.schedule_respond.text.replace('<weekNumber>0</weekNumber>', '')
        xmldoc = minidom.parseString(self.schedule_respond.text)
        weekdays = xmldoc.getElementsByTagName('scheduleModel')
        for day_dom in weekdays:
            day_num = self.DAYS[self.attr(day_dom, 'weekDay')]
            lessons_dom = day_dom.getElementsByTagName('schedule')
            for lesson_dom in lessons_dom:
                lesson = {}

                lesson['auditory'] = self.attr(lesson_dom, 'auditory')
                lesson['lessonTime'] = self.attr(lesson_dom, 'lessonTime')
                lesson['lessonType'] = self.attr(lesson_dom, 'lessonType')
                lesson['subject'] = self.attr(lesson_dom, 'subject')
                lesson['numSubgroup'] = self.attr(lesson_dom, 'numSubgroup')
                lesson['teacher'] = self.teacher(lesson_dom)

                weeks = lesson_dom.getElementsByTagName('weekNumber')
                for week in weeks:
                    week_num = int(week.childNodes[0].data) - 1
                    self.schedule[week_num][day_num].append(lesson)
        return self.schedule

    def teacher(self, lesson_dom):
        employee_dom = lesson_dom.getElementsByTagName('employee')
        empl = {}
        if employee_dom:
            e_d = employee_dom[0]
            empl['lastName'] = e_d.getElementsByTagName(
                'lastName')[0].childNodes[0].data
            empl['firstName'] = e_d.getElementsByTagName(
                'firstName')[0].childNodes[0].data
        return empl

    def attr(self, dom, attr_name):
        attr = dom.getElementsByTagName(attr_name)
        return attr[0].childNodes[0].data if attr else None


class GroupScheduler:
    GROUPS_URL = "https://www.bsuir.by/schedule/rest/studentGroup"

    def __init__(self):
        self.groups_respond = requests.get(self.GROUPS_URL)
        self.groups_ids = self.parse()

    def parse(self):
        xmldom = minidom.parseString(self.groups_respond.text)
        groups_xml = xmldom.getElementsByTagName('studentGroup')
        groups = {}
        for group_dom in groups_xml:
            id = group_dom.getElementsByTagName('id')[0].childNodes[0].data
            name = group_dom.getElementsByTagName('name')[0].childNodes[0].data
            groups[name] = id
        return groups

    def group(self, number):
        schedule = Schedule(self.groups_ids[number])
        return schedule.parse()


def html(schedule):
    global CUR_DATE
    global CUR_WEEK
    today = date.today()
    if CUR_DATE is None or CUR_DATE != today or CUR_WEEK is None:
        CUR_DATE = today
        CUR_WEEK = int(requests.get(
            "https://www.bsuir.by/schedule/rest/currentWeek/date/%s" %
                 (today.strftime("%d.%m.%Y"))).text) - 1
    html = '<ul>'
    for lesson in schedule[CUR_WEEK][today.weekday()]:
        html += "<li>{lessonType}: {subject} {time} {place} ({firstName} {lastName})".format(
            lessonType=lesson['lessonType'],
            place=lesson['auditory'] or '',
            subject=lesson['subject'],
            firstName=lesson['teacher'].get('firstName'),
            lastName=lesson['teacher'].get('lastName'),
            time=lesson['lessonTime'],
        )
        if lesson['numSubgroup'] != '0':
            html += " (%s)" % lesson['numSubgroup']
        html += '</li>'
    html += '</ul>'
    return html

def html_table(schedule):
    html = '' if CUR_WEEK is None else '<p>{} неделя</p>'.format(CUR_WEEK + 1)
    html += '<table class="table table-striped table-bordered table-hover">'
    TIMES = [
        '08:00-09:35',
        '09:45-11:20',
        '11:40-13:15',
        '13:25-15:00',
        '15:20-16:55',
        '17:05-18:40',
        '18:45-20:20',
        '20:25-22:00',
    ]
    DAYS = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ']

    html += '<tr><th></th>'
    for time in TIMES:
        html += '<th>%s</th>' % time
    html += '</tr>'

    for week in range(4):
        html += ("<tr><td colspan='100%' class='info'><div style='text-align:center'><strong>" +
                 "%d неделя</strong></div></td></td>" % (week + 1))

        for day in range(6):
            html += '<tr><td><strong>%s</strong></td>' % DAYS[day]
            for time in TIMES:
                lessons = []
                lesson_type = None
                for lesson in schedule[week][day]:
                    if lesson['lessonTime'] == time:
                        lesson_type = lesson['lessonType']
                        _lesson = ''
                        if lesson['numSubgroup'] != '0':
                            _lesson += "(%s) " % lesson['numSubgroup']
                        _lesson += "{lessonType}: {subject} {time} {place}".format(
                            lessonType=lesson['lessonType'],
                            place=lesson['auditory'] or '',
                            subject=lesson['subject'],
                            time=lesson['lessonTime'],
                        )
                        if lesson['teacher'] != {}:
                            _lesson += ' ({firstName} {lastName})'.format(
                                firstName=lesson['teacher'].get('firstName'),
                                lastName=lesson['teacher'].get('lastName'),
                            )
                        lessons.append(_lesson)
                if len(lessons) == 0:
                    html += '<td>'
                else:
                   html += '<td class="{}" >'.format({
                       'ЛК': 'success',
                       'ПЗ': 'warning',
                       'ЛР': 'danger',
                    }[lesson_type]
                )
                html += "<hr>".join(lessons)
                html += '</td>'
            html += '</tr>'
    html += '<table>'
    return html
