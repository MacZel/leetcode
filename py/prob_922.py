class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_list = []
        odd_list = []
        ret_list = []
        for n in A:
            if n % 2 == 0:
                even_list.append(n)
            else:
                odd_list.append(n)
        for i in range(len(even_list)):
            ret_list.extend([even_list[i], odd_list[i]])
        return ret_list