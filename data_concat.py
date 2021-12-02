import glob
from pathlib import Path

from path import FILES_DIR_PATH, RESULT_FILE_PATH


def file_con():
    filenames = glob.glob(str(Path(FILES_DIR_PATH, "*.txt")))
    with open(RESULT_FILE_PATH, "w") as outfile:
        for f_name in filenames:
            outfile.writelines(read_file(f_name))


def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line


def delete_lines(letters):
    with open(RESULT_FILE_PATH, 'r+') as outfile:
        lines = outfile.readlines()
        outfile.seek(0)
        outfile.truncate(0)
        counter_del = 0
        for line in lines:
            if letters not in line.removesuffix('\n'):
                outfile.write(line)
            else:
                counter_del += 1
    print("%s lines deleted" % counter_del)
