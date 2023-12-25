# Recursive implementation of the binary search algorithm to return
# the position of `target` in subarray nums[left…right]
def binarySearch(nums, left, right, target):

    # Base condition (search space is exhausted)
    if left > right:
        return -1

    # find the mid-value in the search space and
    # compares it with the target

    mid = (left + right) // 2

    # overflow can happen. Use below
    # mid = left + (right - left) / 2

    # Base condition (a target is found)
    if target == nums[mid]:
        return mid

    # discard all elements in the right search space,
    # including the middle element
    elif target < nums[mid]:
        return binarySearch(nums, left, mid - 1, target)

    # discard all elements in the left search space,
    # including the middle element
    else:
        return binarySearch(nums, mid + 1, right, target)


if __name__ == '__main__':
    nums = [int(num) for num in input().split(' ')] # [2, 5, 8, 10, 13, 19, 21, 32, 37, 52]
    target = 13

    (left, right) = (0, len(nums) - 1)
    index = binarySearch(nums, left, right, target)

    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
