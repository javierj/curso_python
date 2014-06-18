if __name__ == '__main__':
    idontknow = ""
    filters = []
    filters.append(lambda val, prev: "Fizz" if ((val%3) == 0) else prev)
    filters.append(lambda val, prev: str(prev) + "Buzz" if ((val%5) == 0) else prev)
    filters.append(lambda val, prev: val if prev == idontknow else prev)

    result =[]
    for i in range(1, 16):
        value = idontknow
        for filter in filters:
            value = filter(i, value)
        result.append(value)

    #print (list)
    print(result)
    print ("ok")