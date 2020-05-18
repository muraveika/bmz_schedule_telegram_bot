import config
import dateparser
from datetime import datetime


class ScheduleLogic(object):

    @staticmethod
    def read_date(text):
        return dateparser.parse(text, locales=['ru-BY'])

    @staticmethod
    def is_date_parsed(date):
        return date is not None

    @staticmethod
    def is_date_before_works_founded(date):
        return date < config.FOUNDING_DATE

    @staticmethod
    def get_shifts_scheme(date):
        schedule_scheme = ScheduleLogic.__get_schedule_scheme(date)
        base_shift = ScheduleLogic.__get_base_sift(date)
        shifts_scheme = []
        start_shift = (base_shift - schedule_scheme if base_shift - schedule_scheme >= 0 else
                       base_shift - schedule_scheme + 4) + 1
        for i in range(4):
            shifts_scheme.append((start_shift + i) if (start_shift + i) <= 4 else (start_shift + i) - 4)
        return shifts_scheme

    @staticmethod
    def get_reply(date, shifts):
        verb = config.PAST_PRESENT_VERBS[0] if date.date() < datetime.now().date() else config.PAST_PRESENT_VERBS[1]
        return config.SCHEDULE_OUTPUT_LABEL.format(date.strftime('%d.%m.%Y'), verb, config.SHIFTS_LABELS[shifts[0]],
                                                   config.SHIFTS_LABELS[shifts[1]], config.SHIFTS_LABELS[shifts[2]],
                                                   config.SHIFTS_LABELS[shifts[3]])

    @staticmethod
    def __get_schedule_scheme(date):
        years_list = list(range(config.FOUNDING_DATE.year, date.year + 1))
        sliced_years_list = [years_list[x:x + len(config.SCHEDULE_SCHEME)] for x in range(0, len(years_list),
                                                                                          len(config.SCHEDULE_SCHEME))]
        scheme = False
        for i in sliced_years_list:
            if date.year in i:
                scheme = config.SCHEDULE_SCHEME[i.index(date.year)]
        return scheme

    @staticmethod
    def __get_base_sift(date):
        day_of_year = date.timetuple().tm_yday
        shifts_list = [list(range(1, day_of_year + 1))[x::4] for x in range(0, 4)]
        shift = False
        for i in shifts_list:
            if day_of_year in i:
                shift = shifts_list.index(i) + 1
        return shift
