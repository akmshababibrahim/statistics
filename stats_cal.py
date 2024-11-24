import math


class Stats:
    def __init__(self, data: list):

        self.data = data
        self.frequency = len(data)
        self.even = None
        self.median = 0
        self.mean = 0
        self.iqr = 0
        self.rangevalue = 0
        self.mode = 0
        self.q1 = 0
        self.q3 = 0
        self.arr = self.arranged()
        self.maximum = max(self.arr)
        self.minimum = min(self.arr)

    def arranged(self):
        count = 0
        while count < self.frequency:
            for i in range(self.frequency - 1):
                if self.data[i] > self.data[i + 1]:
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
            count += 1
        arranged_array = self.data
        return arranged_array

    def is_even(self):
        if self.frequency % 2 != 0:
            self.even = False
        self.even = True

    def mean_value(self):
        self.mean = round((sum(self.arr) / self.frequency), 2)
        # return self.mean

    def median_value(self):
        if self.even:
            n1 = int((self.frequency / 2)) - 1
            n2 = int(self.frequency / 2)
            self.median = round(((self.arr[n1] + self.arr[n2]) / 2), 2)
        else:
            n1 = math.ceil(self.frequency / 2) - 1
            self.median = round(self.arr[n1], 2)

        # return self.median

    def q1_value(self):
        if self.even:
            n1 = int(self.frequency / 4) - 1
            n2 = int(self.frequency / 4)
            self.q1 = round(((self.arr[n1] + self.arr[n2]) / 2), 2)
        else:
            n1 = math.ceil(self.frequency / 4) - 1
            self.q1 = round(self.arr[n1], 2)
        # return self.q1

    def q3_value(self):
        if self.even:
            n1 = int((self.frequency * 3) / 4) - 1
            n2 = int((self.frequency * 3) / 4)
            self.q3 = round(((self.arr[n1] + self.arr[n2]) / 2), 2)
        else:
            n1 = math.ceil((self.frequency * 3) / 4) - 1
            self.q3 = round(self.arr[n1], 2)
        # return self.q3

    def iqr_value(self):
        self.iqr = round(self.q3 - self.q1, 2)
        # return self.iqr

    def range_value(self):
        self.rangevalue = round(self.maximum - self.minimum, 2)
        # return self.rangevalue

    def mode_value(self):
        list_data = []
        list_count = []
        modal = []
        for i in self.arr:
            if i not in list_data:
                list_data += [i]
                list_count += [self.arr.count(i)]
        if sum(list_count) == len(list_data):
            modal.append("None")
            self.mode = modal
        else:
            max_count = max(list_count)
            for i in range(len(list_count)):
                if list_count[i] == max_count:
                    modal.append(str(list_data[i]))
            self.mode = modal
        # return self.mode

    def calculate(self):
        self.is_even()
        self.mean_value()
        self.median_value()
        self.mode_value()
        self.q1_value()
        self.q3_value()
        self.iqr_value()
        self.range_value()
        # print(f"Data: {self.arr}\nMean: {self.mean}\nMedian (Q2): {self.median}\nMode: {self.mode}\nQ1: {self.q1}\nQ3: {self.q3}\nIQR: {self.iqr}\nMaximum: {self.maximum}\nMinimum: {self.minimum}\nRange: {self.rangevalue}\n")
