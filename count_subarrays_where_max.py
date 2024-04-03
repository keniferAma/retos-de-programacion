"""You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times."""




nums = [1,3,2,3,3]
k = 2


def subarray_counter(number_list, k):
    if len(number_list) < 1 or k < 1:
        return 'Invalid data'
    
    init = 0
    end = len(number_list)
    result = 0
    while init <= end - 1:
        for i in number_list[init: end]:
            temporal_counter = 0
            for j in number_list[init: end]:
                if i == j:
                    temporal_counter += 1

            if temporal_counter >= k:
                result += 1
                break

            if k == 1:
                temporal_counter += 1
                
        
        end -= 1

        if len(number_list[init: end]) <= 1:
            end = len(number_list)
            init += 1


    return result




print(subarray_counter(nums, k))


# more efficient code provided by Copilot #

from collections import Counter

def subarray_counter(nums, k):
    # Initialize the result
    result = 0

    # Iterate over the array
    for i in range(len(nums)):
        # Initialize a counter for the current subarray
        counter = Counter()

        # Iterate over the rest of the array
        for j in range(i, len(nums)):
            # Update the counter for the current element
            counter[nums[j]] += 1

            # If the count of the current element is at least k, increment the result
            if counter[nums[j]] >= k:
                result += 1

    # Return the result
    return result

nums = [1,3,2,3,3]
k = 2
print(subarray_counter(nums, k))


# Example of Counter #

from collections import Counter

# Count the frequency of each character in a string
counter = Counter('hello world')
print(counter)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Find the most common character
print(counter.most_common(1))
# Output: [('l', 3)]

print(counter.total())