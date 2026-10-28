from typing import List

def merge(left: List, right: List)->List:
    l = 0
    r = 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    if l < len(left):
        res.extend(left[l:])
    elif r < len(right):
        res.extend(right[r:])
    return res

def merge_sort(l: List)->List:
    if len(l) <= 1:
        return l
    n = len(l)
    return merge(merge_sort(l[:n//2]), merge_sort(l[n//2:]))
