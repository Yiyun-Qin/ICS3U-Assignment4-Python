#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, adding number from 1 to n


def main():
    # This function adds number from 1 to number the user enters

    # input
    add_string = input("Enter a positive integer: ")

    # process & output
    loop_counter = 0
    answer = 0
    print("")
    try:
        add_integer = int(add_string)
        while loop_counter <= add_integer:
            answer = answer + loop_counter
            loop_counter = loop_counter + 1
        print(
            "The sum of all positive integers from 1 to {0} is {1}.".format(
                add_string, answer
            )
        )
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
