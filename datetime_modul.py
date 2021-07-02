import datetime
import calendar


def five_days_later():
    """Получить текущую дату +5 дней в формате ДД.ММ.ГГ"""
    day_today = datetime.datetime.today()
    plus_five_days = day_today + datetime.timedelta(days=5)
    print(plus_five_days.strftime('%d.%m.%y'))


def current_date():
    """Получить текущую дату в формате ДД.ММ.ГГГГ"""
    day_today = datetime.datetime.today().strftime('%d.%m.%Y')
    print(day_today)


def ten_days_later(date):
    """К дате прибавить 10 дней и вывести в формате ДД.ММ.ГГГГ"""
    date_format = datetime.datetime.strptime(date, '%d.%m.%y')
    plus_ten_days = date_format + datetime.timedelta(days=10)
    print(plus_ten_days.strftime('%d.%m.%Y'))


def first_day_of_month():
    """
    Вывести дату в формате ДД.ММ.ГГ,
    эта дата должна быть первым днем месяца
    """

    day_today = datetime.datetime.today()
    first_day = day_today.replace(day=1)
    print(first_day.strftime('%d.%m.%y'))


def last_day_of_month():
    """
    Вывести дату в формате ДД.ММ.ГГ,
    эта дата должна быть последним днем месяца
    """
    day_today = datetime.datetime.today()
    next_month = day_today.replace(day=28) + datetime.timedelta(days=4)
    last_day = next_month - datetime.timedelta(days=next_month.day)
    print(last_day.strftime('%d.%m.%y'))


def one_month_later(date):
    """Прибавить к дате 1 месяц и вывести в формате ДД.ММ.ГГГГ"""
    change_month(date, 1)


def change_month(date, month):
    """Прибавляет/вычитает переданное кол-во месяцев к дате"""
    date_format = datetime.datetime.strptime(date, '%d.%m.%y')
    new_month = (date_format.month + month) % 12
    if new_month == 0:
        new_month = 12
    if month >= 0:
        new_year = date_format.year + (date_format.month + month) // 12
    else:
        new_year = date_format.year + (date_format.month + month - 1) // 12
    new_day = min(date_format.day, calendar.monthrange(new_year, new_month)[1])
    new_date = datetime.date(new_year, new_month, new_day)
    print(new_date.strftime('%d.%m.%y'))


# five_days_later()
# current_date()
# ten_days_later('30.12.13')
# first_day_of_month()
# last_day_of_month()
one_month_later('29.01.21')
# change_month('30.01.21', 2)
