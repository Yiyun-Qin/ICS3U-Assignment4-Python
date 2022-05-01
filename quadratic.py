#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, solving the quadratic equations


def main():
    # This function can solve quadratic equation.

    # input
    print(
        "A quadratic equation is like ax\u00b2+bx+c=0, while a, b and c are constants."
    )
    a_string = input("Enter the a of your quadratic equation: ")
    b_string = input("Enter the b of your quadratic equation: ")
    c_string = input("Enter the c of your quadratic equation: ")

    # process & output
    print("")
    try:
        a_integer = int(a_string)
        b_integer = int(b_string)
        c_integer = int(c_string)
        delta = pow(b_integer, 2) - 4 * a_integer * c_integer
        print(
            "The equation is {0}x\u00b2+{1}x+{2}=0.".format(
                a_integer, b_integer, c_integer
            )
        )
        if delta < 0:
            print("No real solutions for this quadratic equation!")
        elif delta == 0:
            x = (-b_integer + pow(delta, 1 / 2)) / 2
            print(
                "There is one solution for this quadratic equation. The answer is {:,.2f}.".format(
                    x
                )
            )
        else:
            x1 = (-b_integer + pow(delta, 1 / 2)) / 2
            x2 = (-b_integer - pow(delta, 1 / 2)) / 2
            print(
                "There are two solutions for this quadratic equation. The answers are {0:,.2f} and {1:,.2f}.".format(
                    x1, x2
                )
            )
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
