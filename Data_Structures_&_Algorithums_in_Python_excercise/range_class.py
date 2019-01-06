class Range:
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.k = -1
    def __len__(self):
        return (self.stop - self.start) // self.step

    def __getitem__(self, index):
        return self.start + index * self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.k += 1
        return self.start + self.k * self.step
    

if __name__ == "__main__":
    range = Range(0, 10, 2)
    print("Range between 0 to 10")
    print("Length of range:",len(range))
    print("Get item:", range[2])

