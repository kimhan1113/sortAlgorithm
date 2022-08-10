

def recursive_func(i):

    if i == 100:
        return

    print(i, i+1)
    recursive_func(i+1)
    print(i, '종료')


recursive_func(1)
