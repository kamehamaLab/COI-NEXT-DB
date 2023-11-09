import os
import csv
from utils.InitialValue import CUTLOGFILE, AUDIOSAVEDIR

def yes_no_input():
    while True:
        choice = input("Initialize Logs. OK? Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


def main():
    # check profile
    if not os.path.exists('token.json'):
        print("Please prepare a certification file.")
        return

    if not os.path.exists('Logs'):
        os.makedirs('Logs')
    print("Make Logs Dir")

    if not os.path.exists('RECdata'):
        os.makedirs('RECdata')
    print("Make RECdata Dir")

    # create Log files
    if not os.path.exists("Logs/cutLog.csv"):
        with open(CUTLOGFILE, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["datetime", "filename"])
    print("Make Logs/cutLog.csv")

    print("Completed")

if __name__ == '__main__':
    if yes_no_input():
        print("Initialize Logs...")
        main()

    else :
        print("Look forward to trying again!")
