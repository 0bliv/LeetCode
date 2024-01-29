class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        c = 0
        key_index = {"type": 0, "color": 1, "name": 2}  # Map ruleKey to index

        for item in items:
            if item[key_index[ruleKey]] == ruleValue:
                c += 1

        return c


        