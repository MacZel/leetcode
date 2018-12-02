class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ret = -1
        for l_hour, r_hour, l_min, r_min in itertools.permutations(A):
            hours = 10 * l_hour + r_hour
            mins = 10 * l_min + r_min
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ret:
                ret = time

        return "{:02}:{:02}".format(*divmod(ret, 60)) if ret >= 0 else ""