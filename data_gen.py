import concurrent.futures
import random
import string
import time
from pathlib import Path

from path import FILES_DIR_PATH


def str_time_prop(start, end, time_format, prop):
    """
    This function creates properties for generating date
    """
    s_time = time.mktime(time.strptime(start, time_format))
    e_time = time.mktime(time.strptime(end, time_format))
    p_time = s_time + prop * (e_time - s_time)
    return time.strftime(time_format, time.localtime(p_time))


def random_date(start, end, prop):
    """
    This function generates random time between two dates with the previous function
    """
    return str_time_prop(start, end, '%d.%m.%Y', prop)


def rand_lat_let(r):
    """
    This function generates random latin letters and connect them into one string
    """
    rand_string = ''.join(random.choice(string.ascii_letters) for _ in range(r))
    return rand_string


def rand_rus_lat(r):
    """
      This function generates random russian letters and connect them into one string
    """
    rus_alphabet = 'айцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮ'
    rand_string = ''.join(random.choice(rus_alphabet) for _ in range(r))
    return rand_string


def rand_int(min: int, max: int):
    """
      This function generates random int number between two numbers
    """
    while True:
        number = random.randint(min, max)
        if number % 2 == 0:
            break
    return number


def rand_float(min: float, max: float):
    """
          This function generates random float number between two numbers
    """
    return float("{0:.8f}".format(random.uniform(min, max)))


def generate_files(files_amount: int):
    """
    This function creates 8 txt files in time
    """
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(file_gen, range(1, files_amount + 1))


def file_gen(i):
    """
    This function fill empty txt files with data
    """
    with open(Path(FILES_DIR_PATH, f"file{i}.txt"), "w") as file:
        itr = 0
        while itr < 100000:
            file.write(random_date("30.11.2016", "30.11.2021", random.random()) + '||' + rand_lat_let(10) + '||' +
                       rand_rus_lat(10) + '||' + str(rand_int(1, 100000000)) + '||' + str(
                rand_float(1., 20.)) + '\n')
            itr += 1
    print(f"File {i} created!")
