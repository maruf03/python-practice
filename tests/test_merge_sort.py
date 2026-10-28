from merge_sort import merge_sort, merge

def test_merge():
    l = [1, 2, 3, 4, 5]
    r = [6, 7, 8, 9, 10]
    out = merge(l, r)
    assert out == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_merge2():
    l = [1, 3, 5, 7, 9]
    r = [2, 4, 6, 8, 10]
    out = merge(l, r)
    assert out == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_merge3():
    l = [1, 3, 5, 7, 9]
    r = [2, 4, 6, 8, 10, 11, 12]
    out = merge(l, r)
    assert out == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def test_merge4():
    l = [1, 3, 5, 7, 9, 11, 12]
    r = [2, 4, 6, 8, 10]
    out = merge(l, r)
    assert out == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def test_reversed_list():
    inp = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    out = merge_sort(inp)
    assert out == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_empty_list():
    inp = []
    out = merge_sort(inp)
    assert out == []

def test_list_with_one_item():
    inp = [1]
    out = merge_sort(inp)
    assert out == [1]

def test_already_sorted_list():
    inp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    out = merge_sort(inp)
    assert out == inp
