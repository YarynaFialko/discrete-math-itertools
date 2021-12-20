def product(*args):
    """
    Return the cartesian product of input iterables. 
    >>> list(product('ABCD', 'xy', '12'))
    [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'y', '1'),\
 ('A', 'y', '2'), ('B', 'x', '1'), ('B', 'x', '2'),\
 ('B', 'y', '1'), ('B', 'y', '2'), ('C', 'x', '1'),\
 ('C', 'x', '2'), ('C', 'y', '1'), ('C', 'y', '2'),\
 ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'y', '1'),\
 ('D', 'y', '2')]
    """
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