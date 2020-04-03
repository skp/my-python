class Solution:
    def isValid(self, s):
        stack = []
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        patternSet = {"}", "]", ")"}
        for x in s:
            if x in map:
                stack.append(map[x])
            else:
                if x in patternSet:
                    if len(stack) != 0:
                        top_element = stack.pop()
                        if x != top_element:
                            return False
                        else:
                            continue
                    else:
                        return False
        return len(stack) == 0

if __name__ == '__main__':
    print("ha")
    print(Solution().isValid("(sd){}{zf}[]"))

