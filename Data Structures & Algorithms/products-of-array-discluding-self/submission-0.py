class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, zeros = 1, 1, 0
        res = []
        freeze = False
        for n in nums:
            if n == 0:
                zeros += 1
                continue
            elif zeros == 1 and not freeze:
                left = right
                right = 1
                freeze = True
            right *= n
        for n in nums:
            if zeros >= 2:
                res.append(0)
                continue
            if zeros == 1:
                if n != 0:
                    res.append(0)
                else:
                    res.append(int(left*right))
            else:
                right /= n
                res.append(int(left*right))
                left *= n
        return res
