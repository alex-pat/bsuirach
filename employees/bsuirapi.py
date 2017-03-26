import requests
from xml.dom import minidom

EMPLOYEES_URL = "https://www.bsuir.by/schedule/rest/employee"


def add_attr(employee, dom, attr_name):
    attr = dom.getElementsByTagName(attr_name)
    if attr and attr[0].childNodes:
        employee[attr_name] = attr[0].childNodes[0].data
    else:
        employee[attr_name] = ''


def parse(xml):
    xmldom = minidom.parseString(xml)
    empls = xmldom.getElementsByTagName('employee')
    prepods = []
    for empl_dom in empls:
        empl = {}
        add_attr(empl, empl_dom, 'academicDepartment')
        add_attr(empl, empl_dom, 'calendarId')
        add_attr(empl, empl_dom, 'firstName')
        add_attr(empl, empl_dom, 'id')
        add_attr(empl, empl_dom, 'lastName')
        add_attr(empl, empl_dom, 'middleName')
        add_attr(empl, empl_dom, 'photoLink')
        add_attr(empl, empl_dom, 'rank')
        prepods.append(empl)
    return prepods


def get_employees():
    empls_respond = requests.get(EMPLOYEES_URL)
    return parse(empls_respond.text)
