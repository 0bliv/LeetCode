class Solution(object):
    def defangIPaddr(self, address):
        resp = address.replace('.','[.]')
        return resp
        
        