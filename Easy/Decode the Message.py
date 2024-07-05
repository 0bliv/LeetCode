class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {" ": " "}
        i = ord('a')
        for c in key:
            if c not in d:
                d[c] = chr(i)
                i += 1
        return "".join(d[c] for c in message)
