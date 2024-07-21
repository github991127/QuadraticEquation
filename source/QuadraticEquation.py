from math import fabs, sqrt


def funEquation(a, b, c):
    if (a == 0):  # 一次方程
        if (b == 0):
            return ("error")
        else:
            return ("x={0}".format(round(-c / b, 3)))
    else:
        d = b * b - 4 * a * c;
        if (fabs(d) <= 1e-6):  # 即==0（double防止溢出）
            return ("x1=x2={0}".format(round(-b / (2 * a), 3)))
        elif (d > 1e-6):
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            return ("x1={0}\nx2={1}".format(round(x1, 3), round(x2, 3)))
        else:
            return ("方程无实根")


if __name__ == "__main__":
    x = funEquation(1, 5, 2)
    # x = funEquation(9, 6, 1)
    # x = funEquation(0, 3, 5)
    # x = funEquation(0, 0, 5)
    print(x)
