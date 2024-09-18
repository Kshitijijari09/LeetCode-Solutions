class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        stack = []
        for i in digits:
            s += str(i)
        new_digit = int(s) + 1
        print(new_digit)
        for i in str(new_digit):
            stack.append(int(i))
        return stack