from random import randrange


def shuffle(array):
    length = len(array)
    indices = [i for i in range(length)]
    newArr = [None] * length
    for i in range(length):
        chosen = indices.pop(randrange(len(indices)))
        newArr[i] = array[chosen]
    return newArr


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    a = shuffle(a)
    print(a)
