class Solution(object):
    def decode(self, encoded, first):
        n = len(encoded) + 1
        arr = [first]

        for i in range(n - 1):
            arr.append(arr[i] ^ encoded[i])
        return arr
        