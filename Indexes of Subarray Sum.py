class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        start = 0
        curr_sum = 0

        for end in range(n):
            # Add current element to window ka sum
            curr_sum += arr[end]

            # Jab tak curr_sum > target, window ko left se shrink karo
            while curr_sum > target and start <= end:
                curr_sum -= arr[start]
                start += 1

            # Agar sum mil gaya, to return 1-based index
            if curr_sum == target:
                return [start + 1, end + 1]

        # Agar poori array scan karne ke baad bhi nahi mila
        return [-1]
