def product(*args):
    lst = []
    for i in args:
        lst.append(tuple(i))
    lst2 = [[]]
    for elem0 in lst:
        for elem1 in lst2:
            for elem2 in elem0:
                lst2 = lst2 + [elem1+[elem2]]
    new_lst = [elem3 for elem3 in lst2 if len(elem3) == (len(args))]
    for elem4 in new_lst:
        yield tuple(elem4)
