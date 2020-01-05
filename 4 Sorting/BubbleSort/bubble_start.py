# Bubble sort algorithm


def bubbleSort(dataset):
    #start with the array length and decrement each time
    if len(dataset) > 0:
        print("dataset legnth: ", len(dataset))
        for i in range(len(dataset)-1, 0, -1):
            for j in range(i):
               if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp    
            print("Current state: ", dataset)
    else:
        print("Nothing to iterate")

def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)

    #passing empty dataset
    #bubbleSort([])


if __name__ == "__main__":
    main()
