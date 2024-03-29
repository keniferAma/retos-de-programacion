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




nums = [1, 2, 1, 4, 5, 1, 4, 3, 2, 1, 3]
k = 2

def subarra_counter(array, k):
    counter = 0
    end_init = len(array)
    init_end = 0
    sub_array = array[init_end: end_init]

    for item_1 in sub_array:
        temporal_counter = 0
        for item_2 in sub_array:
            if item_1 == item_2:
                temporal_counter += 1
        if temporal_counter - 1 >= k:
            counter += 1
    
        if end_init - init_end <= 1:
            end_init -= 1
    



        

