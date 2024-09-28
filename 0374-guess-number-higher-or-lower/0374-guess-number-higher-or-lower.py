# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        first, last = 1, n
        while first <= last:
            mid = first + (last - first) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                last = mid - 1
            else:
                first = mid + 1
        return -1
#         l, r = 1, n

#         while l<=r:
#             mid = (l+r) >> 1
#             res = self.guess(mid)
#             if res == 0:
#                 return mid
#             if res  == 1:
#                 l = mid+1
#             if res == -1:
#                 r = mid - 1
#         return -1
         

    