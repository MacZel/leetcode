class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_odd_list = []
        for number in A:
            if number % 2 == 0:
                # even_odd_list = even_odd_list.insert(0, number)
                even_odd_list = [number] + even_odd_list
            else:
                # even_odd_list = even_odd_list.push(number)
                even_odd_list = even_odd_list + [number]
        return even_odd_list
