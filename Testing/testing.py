import random
import asyncio
import math
import gc
import re
import numpy as np
import pandas as pd
import scipy.stats as spst
from datetime import datetime
from Testing.Card_Deck.deck import Deck
from Testing.Sorting.algorithms import SortAlgorithms
from Testing.class_testing import Name
from Testing.simple_class import SimpleClass


def main():
    to_sort = [x for x in range(20)]
    random.shuffle(to_sort)

    sorting = SortAlgorithms(to_sort)

    print("Before sorting the array:\n{}".format(to_sort))
    sorting.bubble_sort(sorting.to_sort)
    print("After sorting the array:\n{}".format(to_sort))

    COLORS = ['D', 'H', 'C', 'S']
    CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    JOCKERS = ['RJ', 'BJ']

    deck_obj = Deck(COLORS, CARDS, JOCKERS)
    deck_obj.build_deck()

    print("Cards number in our deck is: {}".format(len(deck_obj.structure)))
    print("Random card from our deck: {}".format(deck_obj.get_card()))

    my_name = Name("Pesho")
    print("The length of {0}, is {1} chars.".format(my_name.name, my_name.length))

    numpy_array = np.array([0])
    print(numpy_array)


async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


def factoriel(n):
    if n is 1:
        return n
    else:
        return n*factoriel(n-1)


def create_dict_from_1_to_n(n):
    return {n: n * n for n in range(1, n+1)}


def create_list_tuple(input):
    list_elements = input.split(',')
    tuple_element = tuple(list_elements)

    print("{0}\n{1}".format(list_elements, tuple_element))


def calculate_from_input():
    c = 50
    h = 30

    input_data = input("Please enter some integers/decimals by ',' separate: ")
    numbers = input_data.split(',')
    calculated = [int(round(math.sqrt((2 * c * float(x))/h))) for x in numbers]
    print(', '.join(map(lambda y: str(y), calculated)))


def two_dimensional_array():
    dimensions = input("Enter X,Y values (',' separated): ").split(',')
    rows_number = int(dimensions[0])
    cols_number = int(dimensions[1])

    matrix = [[y*x for y in range(cols_number)] for x in range(rows_number)]

    print(matrix)


def sort_words():
    words = input("Enter some words ',' separated: ")
    words_array = words.split(',')
    words_array.sort()

    print("The words sequence sorted: {}".format(','.join([w for w in words_array])))


def upper_lines():
    input_lines = []

    print("Write any kind of text you want:")

    while True:
        line = input()
        if line:
            input_lines.append(line)
        else:
            break

    print('\n'.join([line.upper() for line in input_lines]))


def all_even():
    output_numbers = []

    for number in range(1000,3001):
        digits = [int(x) for x in str(number)]

        if all(x % 2 == 0 for x in digits):
            output_numbers.append(number)

    print(','.join([str(el) for el in output_numbers]))


def calc_digits_letters():
    sentence = input("Enter a sentence: ")

    symbols = {'digits': len([d for d in sentence if d.isdigit()]),
               'letters': len([l for l in sentence if l.isalpha()])}

    print("Digits:{0}\nLetters:{1}".format(symbols['digits'], symbols['letters']))


def calc_sum_of_numbers():
    number = input("Enter a number: ")
    number1 = int(number)
    number2 = int("{0}{1}".format(number1, number1))
    number3 = int("{0}{1}{2}".format(number1, number1, number1))
    number4 = int("{0}{1}{2}{3}".format(number1, number1, number1, number1))
    sum_numbers = number1+number2+number3+number4

    print("{0}+{1}+{2}+{3}={4}".format(number1,number2,number3,number4,sum_numbers))


def check_symbol():
    text = "Some/*-*/@!text"
    print(re.search(r'/*-*/', text))


def panda_to_unix_time(timestamp):
    """takes a pandas time stamp and return a string representaion of that in unix time"""
    return int(float(timestamp.value/(10**9)))


def essential_utilization(data_, building_floor, assigned_hc_only, interval=30, printing=False):
    """

    :type assigned_hc_only: object
    """
    # variable to store final utilization result
    OCCUP = pd.DataFrame()
    hours = 24
    seconds_in_hour = 3600
    minutes_in_hour = 60
    hours_x_two = 48

    # add dates to the column and generate unique dates, we will process day by day
    data_['date'] = data_['timestamp'] // (hours * seconds_in_hour)
    dates = np.unique(data_.date)

    # create a list of all buildings
    all_buildings = np.unique(building_floor['office_building_id'])

    # start to process day by day
    for date in dates:

        if printing:
            print("start processing date %s" % date)

        # selected day's data
        dat_ = data_[data_.date == date]

        # first and last timestamp of the day
        first_ts = date * seconds_in_hour * hours
        last_ts = first_ts + seconds_in_hour * (hours - 1)

        # create working-end time for each building according to average number of
        # observations for each badge_id that has ever shown for the building in ith day

        # average number of observations for each building
        x = [dat_.badge_id[dat_.office_building_id == b].value_counts().mean() for b in all_buildings.tolist()]

        # percentage used to calculate end time for each building
        y = [0.9 if xx >= 4 else -0.008333 * xx + 0.9333333 for xx in x]

        end_b = [dat_.timestamp[dat_.office_building_id == all_buildings[k]].quantile(q=y[k]) if np.isnan(y[k]) is False
                 else float('nan') for k in range(len(y))]  # end time

        end_mean = np.nanmean(end_b)

        # for building without any data (mostly because of missing data), use the average end time of other buildings
        end_b = [end_mean if np.isnan(b) else b for b in end_b]

        end_b = [(b - first_ts) / seconds_in_hour for b in end_b]

        # variable to store utilization for selected day
        Occup = pd.DataFrame()

        # departments that exit in selected day
        departments = np.unique(dat_['department_id'])
        departments = departments[departments > 0]

        # all floors that people go to
        # floors_to = np.unique(dat_.office_building_floor_id)

        # loop over each department
        for department in departments:

            if printing:
                print("    processing department %s" % department)

            # data for selected department
            badgeData = dat_[dat_.department_id == department]

            # only include floor that a department visit but not all floors for this department's utilization
            floors_to = np.unique(badgeData.office_building_floor_id)

            # create structure to store utilization
            time_interval = [r * interval * minutes_in_hour + first_ts for r in range(hours_x_two)]
            Time_Interval = time_interval * len(floors_to)

            occup = pd.DataFrame()
            occup['office_building_floor_id'] = np.repeat(floors_to, hours_x_two)
            occup['timestamp'] = Time_Interval
            occup['occup_assigned'] = 0.0
            occup['occup_in_campus'] = 0.0
            occup['occup_off_campus'] = 0.0

            # start with processing utilization for people who are assgined to the buildings being studied
            badgeData1 = badgeData[badgeData.assigned_building_id.isin(all_buildings)]

            # check if there is data for this department, will skip otherwise
            if len(badgeData1):

                ids1 = np.unique(badgeData1.badge_id)

                # loop over each badge id
                for _id in ids1:

                    # get data for selected badge id
                    dat = badgeData1[badgeData1.badge_id == _id]

                    # remove rows that are not helpful in determine where people are
                    if len(dat) > 2:
                        same_floor = np.delete(np.diff(dat.office_building_floor_id), -1)
                        row_delete = [n + 1 for n in np.where(same_floor == 0)]
                        if len(row_delete):
                            dat = dat.drop(dat.index[row_delete])

                    # get timestamps and visited places
                    timestamps = dat.timestamp.tolist()  # all timestamp
                    first_in = (timestamps[0] - first_ts) / float(seconds_in_hour)  # first badge in
                    last_in = (timestamps[len(timestamps) - 1] - first_ts) / float(seconds_in_hour)  # last badge in
                    assigned_building = dat.assigned_building_id.tolist()[0]  # assigned building
                    floors_visit = dat.office_building_floor_id.tolist()  # floors corresponding to timestamps
                    buildings_visit = dat.office_building_id.tolist()  # buildings corresponding to timestamps

                    end_time = end_b[np.where(all_buildings == assigned_building)[0][0]]

                    # geneate stay time. if first in is before building end time,
                    # using truncated normal distribution, otherwise uniform distribution
                    if first_in <= end_time:
                        mu = end_time - first_in
                        sigma = 1.5
                        # stay = last_in - first_in + 2
                        stay = spst.truncnorm(a=(last_in - first_in - mu) / sigma, b=(100 - first_in - mu) / sigma,
                                              loc=mu,
                                              scale=sigma).rvs()
                    else:
                        min_value = last_in - first_in
                        max_value = hours - first_in
                        stay = spst.uniform(loc=min_value, scale=max_value - min_value).rvs()
                        # stay = last_in - first_in + 2

                    # working end time for this badge_id
                    end = min([first_ts + (first_in + stay) * seconds_in_hour, last_ts])

                    # complete the useful timestamps and find what intervals they belong to
                    timestamps.append(end)
                    timestamps_interval = [(t - first_ts) / (interval * float(minutes_in_hour)) for t in timestamps]
                    timestamps_interval_loc = [int(math.floor(t)) for t in timestamps_interval]

                    # loop for each small utlization pieces to calculate
                    for k in range(len(timestamps) - 1):

                        if (assigned_building != buildings_visit[k]) and assigned_hc_only:
                            continue

                        # location for the k the badge-in
                        location = np.where(floors_to == floors_visit[k])[0].tolist()[0]

                        # calculate kth piece of utilization
                        temp_occup = [0] * hours_x_two

                        if timestamps_interval_loc[k] == timestamps_interval_loc[k + 1]:
                            temp_occup[timestamps_interval_loc[k]] = (timestamps[k + 1] - timestamps[k]) / (
                                        interval * float(minutes_in_hour))
                        elif timestamps_interval_loc[k] + 1 == timestamps_interval_loc[k + 1]:
                            temp_occup[timestamps_interval_loc[k]] = (time_interval[timestamps_interval_loc[k] + 1] -
                                                                      timestamps[k]) / (
                                                                                 interval * float(minutes_in_hour))
                            temp_occup[timestamps_interval_loc[k + 1]] = (timestamps[k + 1] -
                                                                          time_interval[
                                                                              timestamps_interval_loc[k + 1]]) / (
                                                                                     interval * float(minutes_in_hour))
                        else:
                            temp_occup[(timestamps_interval_loc[k] + 1):(timestamps_interval_loc[k + 1])] = [1] * len(
                                range((timestamps_interval_loc[k] + 1), (timestamps_interval_loc[k + 1])))
                            temp_occup[timestamps_interval_loc[k]] = (time_interval[timestamps_interval_loc[k] + 1] -
                                                                      timestamps[k]) / (
                                                                                 interval * float(minutes_in_hour))
                            temp_occup[timestamps_interval_loc[k + 1]] = (timestamps[k + 1] - time_interval[
                                timestamps_interval_loc[k + 1]]) / (interval * float(minutes_in_hour))

                        change_loc = range(location * hours_x_two, (location + 1 * hours_x_two))

                        # if badge id belongs to another building, add utilization to occup_in_campus; otherwise add to occup_assigned

                        try:
                            if assigned_building != buildings_visit[k]:
                                occup.loc[change_loc, 'occup_in_campus'] = occup.loc[
                                                                               change_loc, 'occup_in_campus'] + temp_occup
                            else:
                                occup.loc[change_loc, 'occup_assigned'] = occup.loc[
                                                                              change_loc, 'occup_assigned'] + temp_occup
                        except:
                            print(temp_occup)

            # if we want utilizztion for all people
            if assigned_hc_only is False:
                badgeData2 = badgeData[badgeData.assigned_building_id.isin(all_buildings) is False]

                if len(badgeData2):

                    ids2 = np.unique(badgeData2.badge_id).tolist()

                    # loop over each badge id that is not assgined the buidlings
                    for _id in ids2:

                        dat = badgeData2[badgeData2.badge_id == _id]
                        floors_visit = dat.office_building_floor_id.tolist()

                        # get all timestamps and their differences
                        timestamps = dat.timestamp.tolist()
                        time_diff = np.diff(timestamps) / float(seconds_in_hour)

                        # generate random stay time for each visit, but use min(stay, next_timestamp) as visit's end
                        stay = spst.expon(scale=1.5).rvs(size=len(timestamps)).tolist()
                        # stay = [1] * len(timestamps)
                        stay1 = stay[0:(len(stay) - 1)]
                        stay2 = stay[-1]

                        stay_change_loc = np.where(stay1 > time_diff)[0]
                        for loc in stay_change_loc:
                            stay1[loc] = time_diff[loc]
                        end = min(timestamps[-1] + stay2 * seconds_in_hour, last_ts)
                        stay2 = (end - timestamps[-1]) / float(seconds_in_hour)
                        stay1.append(stay2)
                        stay = stay1

                        # end of each visit
                        timestamp_start = timestamps
                        timestamp_end = [timestamp_start[l] + stay[l] * seconds_in_hour for l in range(len(stay))]

                        timestamp_start_interval = [(t - first_ts) / (interval * float(minutes_in_hour)) for t in
                                                    timestamp_start]
                        timestamp_end_interval = [(t - first_ts) / (interval * float(minutes_in_hour)) for t in
                                                  timestamp_end]

                        timestamp_start_interval_loc = [int(math.floor(t)) for t in timestamp_start_interval]
                        timestamp_end_interval_loc = [int(math.floor(t)) for t in timestamp_end_interval]

                        # loop for each two start & end timestamps
                        for k in range(len(timestamp_start)):
                            location = np.where(floors_to == floors_visit[k])[0].tolist()[0]
                            temp_occup = [0] * hours_x_two

                            if timestamp_start_interval_loc[k] == timestamp_end_interval_loc[k]:
                                temp_occup[timestamp_start_interval_loc[k]] = timestamp_end_interval[k] - \
                                                                              timestamp_start_interval[k]
                            elif timestamp_start_interval_loc[k] + 1 == timestamp_end_interval_loc[k]:
                                temp_occup[timestamp_start_interval_loc[k]] = 1 - (
                                            timestamp_start_interval[k] - timestamp_start_interval_loc[k])
                                temp_occup[timestamp_end_interval_loc[k]] = timestamp_end_interval[k] - \
                                                                            timestamp_end_interval_loc[k]
                            else:
                                temp_occup[(timestamp_start_interval_loc[k] + 1):(timestamp_end_interval_loc[k])] = \
                                    [1] * len(range((timestamp_start_interval_loc[k] + 1), (timestamp_end_interval_loc[k])))
                                temp_occup[timestamp_start_interval_loc[k]] = 1 - (timestamp_start_interval[k] - timestamp_start_interval_loc[k])
                                temp_occup[timestamp_end_interval_loc[k]] = timestamp_end_interval[k] - timestamp_end_interval_loc[k]

                            try:
                                change_loc = range(location * hours_x_two, ((location + 1) * hours_x_two))
                                occup.loc[change_loc, 'occup_off_campus'] = occup.loc[
                                                                                change_loc, 'occup_off_campus'] + temp_occup
                            except:
                                print(temp_occup)

            occup['department_id'] = department
            Occup.append(occup)

        OCCUP.append(Occup)

    return OCCUP


if __name__ == '__main__':
    #check_symbol()
    #main()

    # Solving some python interview tasks
    result = [number for number in range(2000, 3201) if number % 7 == 0 and number % 5 != 0]
    print(', '.join(map(lambda x: str(x), result)))

    number = 8
    print("Factoriel of {0} is {1}".format(number, factoriel(number)))

    print("Dict from 1 to {0} is {1}".format(8, create_dict_from_1_to_n(8)))

    sequence = "1,2,4,6,8,10"
    print("List and tuple from a sequence: {}".format(sequence))
    # create_list_tuple(sequence)

    # simple_class = SimpleClass()
    # simple_class.get_string()
    # simple_class.print_upper()

    # calculate_from_input()

    # two_dimensional_array()

    # sort_words()

    # upper_lines()

    # all_even()

    # calc_digits_letters()

    #calc_sum_of_numbers()

    """
    date1 = '2018-03-20'
    date2 = '2018-04-10'

    ts1 = panda_to_unix_time(pd.to_datetime(date1))
    ts2 = panda_to_unix_time(pd.to_datetime(date2)) + (24*3600) - 1

    end_date = (pd.to_datetime(date2) + pd.offsets.Day(1)).strftime('%Y-%m-%d')
    start_date = (pd.to_datetime(date1) - pd.offsets.Day(30)).strftime('%Y-%m-%d')

    print(end_date, start_date)
    """

    campus_list = np.array([0])

    campus = pd.read_csv('campus.csv')

    merged_raw_unfiltered = pd.read_csv('merged_raw_unfiltered.csv')

    util_list = []
    util_floor_list = []
    building_util_list = []

    for c in campus_list:
        input_c = campus[campus.campus_id == c]
        input_d = merged_raw_unfiltered[merged_raw_unfiltered.campus_id == c]

        for d in input_d.date.unique():
            try:
                util = essential_utilization(data_=input_d[input_d.date == d][['timestamp', 'badge_id',
                                                                           'office_building_floor_id',
                                                                           'office_building_id',
                                                                           'assigned_building_id', 'department_id']],
                                         building_floor=input_c[['office_building_id', 'office_building_floor_id']],
                                         assigned_hc_only=False)

                util['badge_occupancy'] = util.apply(
                    lambda x: x['occup_assigned'] + x['occup_in_campus'] + x['occup_off_campus'], axis=1)

                # put dep u for campus to db
                util_list.append(util)

                print('depu')
                print(c)
                # get floor u for campus
                floor_util = util.groupby(['office_building_floor_id', 'timestamp']).agg({'occup_assigned': sum,
                                                                                          'occup_in_campus': sum,
                                                                                          'occup_off_campus': sum,
                                                                                          'badge_occupancy': sum}).reset_index()

                util_floor_list.append(floor_util)
                # put floor utilization for campus to db

                print('F u')
                print(c)

                floor_util = pd.merge(floor_util, campus[['office_building_id', 'office_building_floor_id']],
                                      how='left',
                                      left_on='office_building_floor_id', right_on='office_building_floor_id')
                building_util = floor_util.groupby(['office_building_id', 'timestamp']).agg({'occup_assigned': sum,
                                                                                             'occup_in_campus': sum,
                                                                                             'occup_off_campus': sum,
                                                                                             'badge_occupancy': sum}).reset_index()
                # rename columns because occupancy by building uses building id
                building_util.rename(columns={'office_building_id': 'building_id'}, inplace=True)
                building_util_list.append(building_util)

                print(building_util)
                print('bu')
                print(c)
                print('finished')
                print(c)
            except:
                import traceback
                traceback.print_exc()


