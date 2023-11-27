class Solution(object):
    def average(self, salary):
        count = len(salary) - 2
        total = sum(salary) - min(salary) - max(salary)
        return float(total) / count if count > 0 else 0
        