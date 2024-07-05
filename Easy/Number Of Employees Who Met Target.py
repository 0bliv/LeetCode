class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        resp = 0
        for i in hours:
            if i >= target:
                resp+=1
        return resp