from django import template

register = template.Library()


def month_name(value):
    dic = {
        1: "Jan",
        2: "Feb",
        3: "March",
        4: "April",
        5: "May",
        6: "Jun",
        7: "July",
        8: "Aug",
        9: "Sept",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }
    return dic[value]


register.filter("month_name", month_name)
