class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * n

        cur = 0

        # Forward pass: compute lengths
        for i, ch in enumerate(s):
            if ch.isalpha():
                cur += 1
            elif ch == '*':
                if cur > 0:
                    cur -= 1
            elif ch == '#':
                cur *= 2
            else:          # %
                pass

            length[i] = cur

        if k >= cur:
            return '.'

        # Backward pass
        for i in range(n - 1, -1, -1):

            ch = s[i]
            cur = length[i]

            if ch.isalpha():

                if k == cur - 1:
                    return ch

            elif ch == '#':

                prev = cur // 2
                k %= prev
                continue

            elif ch == '%':

                k = cur - 1 - k
                continue

            elif ch == '*':

                # restore deleted position
                continue

        return '.'