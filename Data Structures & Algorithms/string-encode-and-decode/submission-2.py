from itertools import accumulate
class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedLines = [str(len(line)) + "★" + line for line in strs]
        
        return '\n'.join(encodedLines)

    def decode(self, s: str) -> List[str]:
        result = []
        if s == "":
            return []

        for line in s.split('\n'):
            length, line = line.split('★')
            if length == 0:
                result.append("")
            else:
                result.append(line)

        return result