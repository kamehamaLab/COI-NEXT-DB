import os
import csv
from utils.GoogleDrivefunc import CUTLOGFILE, AUDIOSAVEDIR

def yes_no_input():
    while True:
        choice = input("Initialize Logs. OK? Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


def main():
    if not os.path.exists('token.json'):
        print("Please prepare a certification file.")
        return

    if not os.path.exists('Logs'):
        os.makedirs('Logs')
    print("Make Logs Dir")

    if not os.path.exists('RECdata'):
        os.makedirs('RECdata')
    print("Make RECdata Dir")

    if not os.path.exists(CUTLOGFILE):
        with open(CUTLOGFILE, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["datetime", "filename"])
    print("Make Logs/DeleteLog.csv")



if __name__ == '__main__':
    if yes_no_input():
        print("Initialize Logs...")
        main()
        print("Completed")

    else :
        print("Look forward to trying again!")
