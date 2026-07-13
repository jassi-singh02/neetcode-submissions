class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kd = {}
        bl = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            if num in kd:
                kd[num] += 1
            else:
                kd[num] = 1

        for key in kd:
            bl[kd[key]].append(key)

        for freq in range(len(bl) - 1, 0, - 1):
            for num in bl[freq]:
                res.append(num)

            if len(res) == k:
                return res

        return bl