class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        out_list = []
        for n in range(left, right+1):
            copy_n = n
            is_self_dividing = True
            while copy_n > 0:
                digit = copy_n % 10
                if digit == 0 or n % digit != 0:
                    is_self_dividing = False
                    break
                copy_n = int(copy_n / 10)
            if is_self_dividing:
                out_list.append(n)
        return out_list