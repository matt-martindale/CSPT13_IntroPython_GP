# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array (list). 

# what do we do if smallest or largest is duplicated
# - we only consider 1 of smallest and 1 of largest to be valid

# what data type are we expecting to return?
# int / float?
# return an int

# centered_average([1, 2, 3, 4, 100]) → 3 >>> [2, 3, 4, 100] -> [2, 3, 4] -> 2 + 3 + 4 => 9 / 3 => 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5 >>> [1, 5, 5, 10, 8, 7] -> [1, 5, 5, 8, 7] -> 1 + 5 + 5 + 8 + 7 => 26 / 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3 >>> [-4, -2, -4, -2, 0] -> [-4, -2, -4, -2]  => -4 + -2 + -4 + -2 => -12 / 4 => -3

# centered_average([1, 2, 3, 4, 100]) -> 3 >>> [1, 2, 3, 4, 100] -> 1 + 2 + 3 + 4 + 100 => 110 => 110 - max => 10 - min => 9 / 3 => 3
# max = 100
# min = 1

# DEVISE A PLAN
# 1. Get the smallest number from the list
# 2. Get the largest number from the list
# 3. Sum up the list
# 4. Subtract the smallest and largest number
# 5. Floor divide the sum by the length of the list

# EXECUTE THE PLAN
def centered_avg1(ints):
    # 1. Get the smallest number from the list
    smallest = min(ints)
    # 2. Get the largest number from the list
    largest = max(ints)
    # 3. Sum up the list
    sum = 0
    # 3.5 Iterate over the data
    for num in ints:
        sum += num
        # 4. Subtract the smallest and largest number
    sum -= smallest
    sum -= largest
    # 5. Floor divide the sum by the length of the list
    final_number = sum // (len(ints) - 2)
    return final_number



# testing

numbers = [1, 2, 3, 4, 100]
print(centered_avg1(numbers))
import time

start = time.time()
# for i in range(1000):
    # centered_avg(numbers)
end = time.time()

print(end - start)

print("-----------------------")

start = time.time()
# for i in range(1000):
    # centered_avg2(numbers)
end = time.time()

print(end - start)