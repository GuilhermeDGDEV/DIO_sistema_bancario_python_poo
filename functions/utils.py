from datetime import datetime


def isfloat(num: str):
    try:
        num = num.replace(',', '.')
        float(num)
        return True
    except ValueError:
        return False
    

def isdate(date: str):
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
