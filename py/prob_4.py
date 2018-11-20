class Solution:    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n_elem = len(nums1) + len(nums2)
        
        nums1_gen = (elem for elem in nums1)
        nums2_gen = (elem for elem in nums2)
        
        comb = []
        n1 = next(nums1_gen, None)
        n2 = next(nums2_gen, None)

        while n1 is not None or n2 is not None:
            if (n1 is not None and n2 is None):
                comb.append(n1)
                n1 = next(nums1_gen, None)
            elif (n1 is not None and n2 is not None):
                if n1 <= n2:
                    comb.append(n1)
                    n1 = next(nums1_gen, None)
                else:
                    comb.append(n2)
                    n2 = next(nums2_gen, None)
            else:
                comb.append(n2)
                n2 = next(nums2_gen, None)
                
        median_pos = ((n_elem + 1) / 2) - 1
        median = None

        if median_pos - int(median_pos) * 1 == 0:
            median = comb[int(median_pos)]
        else:
            hi_comp = comb[int(math.ceil(median_pos))]
            lo_comp = comb[int(math.floor(median_pos))]
            median = (hi_comp + lo_comp) / 2
            
        return median
