class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        val = ""
        length = len(s) + 1

        for r in range(len(s) - len(t) + 1):
            val2 = ""
            temp = t

            # end scans forward from the candidate starting position.
            for end in range(r, len(s)):
                current = s[end]

                # Every character belongs in val2 because the answer
                # must be an actual continuous substring of s.
                val2 += current

                # Only remove the character if it is still required.
                #
                # Without this check, temp.index(current) crashes when
                # current does not exist in temp.
                if current in temp:
                    index = temp.index(current)
                    temp = temp[:index] + temp[index + 1:]

                # temp being empty means this substring contains
                # every required occurrence from t.
                if temp == "":
                    if len(val2) < length:
                        val = val2
                        length = len(val2)
                    break

        return val