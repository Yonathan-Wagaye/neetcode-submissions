class Solution:

    def encode(self, strs: List[str]) -> str:
        charSep = '-'
        stringSep = '|'
        encoded = ''
        if not strs: return ''
        for string in strs:
            currStr = ''
            for char in string:
                currStr += charSep
                currStr += str(ord(char))
            if currStr: encoded += currStr[1:]
            else: encoded += '*1'
            encoded += stringSep
        if encoded: return encoded[:-1]
        return encoded             


    def decode(self, s: str) -> List[str]:
        if not s: return []
        stringSep = '|'
        charSep = '-'
        strs = s.split(stringSep)
        result = []
        for encodedStr in strs:
            currentEncoded = encodedStr.split(charSep)
            currentEncoded = [chr(int(encodedChar)) if encodedChar != '*1' else '' for encodedChar in currentEncoded]
            result.append(''.join(currentEncoded))
        return result
