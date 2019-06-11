class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        scan_index_i = 0
        scan_index_j = len(numbers) - 1

        while scan_index_i < scan_index_j:
            while numbers[scan_index_i] + numbers[scan_index_j] < target:
                scan_index_i = scan_index_i + 1
            while numbers[scan_index_i] + numbers[scan_index_j] > target:
                scan_index_j = scan_index_j - 1
            if numbers[scan_index_i] + numbers[scan_index_j] == target:
                break

        return [scan_index_i+1, scan_index_j+1]

