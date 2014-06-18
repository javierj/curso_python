
def isLeapYear(param):
    result = divisibleBy_4_andNotBy_100(param) or divisibleBy_400_andNotBy_100(param)
    return result


def divisibleBy_4_andNotBy_100(year):
    module = (year % 4)
    return module == 0 and ((year % 100) != 0)


def divisibleBy_400_andNotBy_100(year):
    return ((year % 400) == 0 and (year % 100) == 0)

if __name__ == "__main__":
    print("1996 true", isLeapYear(1996))
    print("2000 true", isLeapYear(2000))
    print("2001 false", isLeapYear(2001))
    print("1900 false", isLeapYear(1900))