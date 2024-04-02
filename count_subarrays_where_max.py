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