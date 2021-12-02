from db_connector import *
from data_gen import generate_files
from data_concat import delete_lines, file_con

if __name__ == '__main__':
    print("Input 1 for generating files\nInput 2 to remove lines\nInput 0 to exit\n")
    chose = input("Input your variant: ")
    while chose:
        if chose == "1":
            generate_files(100)
            file_con()
            chose = input("Input your variant, if you wont to exit, input 0: ")
        if chose == "2":
            word = input("Input word: ")
            delete_lines(word)
            with Database("new_database.db") as db:
                db.create_table()
                db.insert_data()
                print(db.select_sum_avg())
                db.drop_table()
            chose = input("Input your variant, if you wont to exit, input 0: ")
        if chose == "0":
            exit()
