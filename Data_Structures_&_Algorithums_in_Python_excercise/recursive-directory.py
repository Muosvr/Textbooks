import os


def checkSize(path):
    size = os.path.getsize(path)
    if os.path.isdir(path):
        for childFolder in os.listdir(path):
            childPath = os.path.join(path, childFolder)
            print("childPath", childPath)
            size += checkSize(childPath)
    return size


if __name__ == "__main__":
    path = str(input("Please enter a path to check for size: "))
    print(checkSize(path))
