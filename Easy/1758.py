class Solution(object):
    def minOperations(self, s):
        n = len(s)
        
        # Patterns:
        # Pattern 0: start with '0': '010101...'
        # Pattern 1: start with '1': '101010...'
        
        mismatch_0 = 0  # for pattern 0, where even indices should be '0' and odd indices should be '1'
        mismatch_1 = 0  # for pattern 0, where even indices should be '1' and odd indices should be '0'
        
        mismatch_2 = 0  # for pattern 1, where even indices should be '1' and odd indices should be '0'
        mismatch_3 = 0  # for pattern 1, where even indices should be '0' and odd indices should be '1'
        
        for i in range(n):
            expected_0 = '0' if i % 2 == 0 else '1'
            expected_1 = '1' if i % 2 == 0 else '0'
            
            # Count mismatches for pattern 0
            if s[i] != expected_0:
                if expected_0 == '0':
                    mismatch_0 += 1
                else:
                    mismatch_1 += 1
            
            # Count mismatches for pattern 1
            if s[i] != expected_1:
                if expected_1 == '1':
                    mismatch_2 += 1
                else:
                    mismatch_3 += 1
        
        # Minimum number of operations required
        return min(mismatch_0 + mismatch_1, mismatch_2 + mismatch_3)
