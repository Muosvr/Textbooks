"""
C-4.9 Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.
"""


def _findMaxMin(S, max, min, next):
    if max == min == None:
        max = min = S[next]
    if next >= len(S):
        return max, min
    else:
        if S[next] > max:
            max = S[next]
        if S[next] < min:
            min = S[next]
        max, min = _findMaxMin(S, max, min, next + 1)
    return max, min


def findMaxMin(S):
    return _findMaxMin(S, None, None, 0)


if __name__ == "__main__":
    S = [3, 5, 2, 6, 1, 6, 3, 234, 1, 23, 231, 23, -2, 324, -34, -32, 3, 23]
    print(findMaxMin(S))
