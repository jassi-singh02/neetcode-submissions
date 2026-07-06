class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kd = {}

        for num in nums:
            if num in kd:
                kd[num] += 1
            else:
                kd[num] = 1

        keys = sorted(kd, key=kd.get)

        return keys[-k:]