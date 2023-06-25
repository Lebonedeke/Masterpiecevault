
def binary_earch(list,target):

    mid = 0
    start = 0
    end = len(list)
    steps = 0

    while start<= end:
        print(f"step, {steps} :" + str(list[start:end+1]))

        steps = steps+1
        mid = (start + end) // 2

        if target == list[mid]:
            return mid
        elif target > list[mid]:
            start = mid + 1
        elif target < list[mid]:
            end = mid -1
    return  -1


print(binary_earch([2, 4, 6, 8, 10], 8))