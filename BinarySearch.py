def main():
    values = input('Input values for array. Add space between values and make sure values are sorted \n')
    array = []
    for i in range(len(values)):
        if values[i] != ' ':
            array.append(int(values[i]))

    target = input ('Enter your target: \n')

    binarySearch = BinarySearch(array, target)
    print(binarySearch.executeBinarySearch())

class BinarySearch():

    def __init__(self, array, target):
        self.array = array
        self.target = target

    def executeBinarySearch(self):
        left = 0
        right = len(self.array) - 1

        while (left <= right):
            mid = int((right + left) / 2)
            if self.array[mid] == int(self.target):
                return mid
                break
            elif int(self.target) < self.array[mid]:
                #move left
                right = mid - 1
            else:
                #move right
                left = mid + 1

        #not found
        return None


main()