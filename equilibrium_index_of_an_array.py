# An index in an array is said to have an equilibrium index if the left_array_sum and right_array_sum of that index
# is same.
# At index 0 there will be no left_array so the index 0 is not considered to be an equilibrium index.


def prefix_sum_array(nums: list) -> list:
    prefix_sum = [nums[0]]
    for index in range(1, len(nums)):
        prefix_sum.append(prefix_sum[index - 1] + nums[index])
    return prefix_sum


def small_equilibrium_index(num_array):
    prefix_sum = prefix_sum_array(num_array)
    for index in range(1, len(prefix_sum)):
        if prefix_sum[index - 1] == (prefix_sum[len(prefix_sum) - 1] - prefix_sum[index]):
            return index
    return -1


try:
    print("Enter integer elements of an array separated by space to get the smallest equilibrium index : ")
    numbers_array = list(map(int, input().split()))
    print(small_equilibrium_index(numbers_array))
except ValueError:
    print("Invalid input. Please Enter only Integers separated by space")
