class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        decrement_amount = 1
        base = 1
        # find initial jump distance
        while n // base >= 10:
            decrement_amount = decrement_amount * 10 + 1
            base *= 10

        # we start at k, then try to reach 1, where our answer is
        cur = 1 # holds the value at our current index
        while k > 1:
            decrease_distance = False
            # try to jump as far as we can without passing k
            # or pass k by 1 * jump distance
            furthest = max(1, min((k - 1) // decrement_amount, n // base - cur))
            potential_next_cur = cur + furthest
            potential_next_k = k - decrement_amount * furthest
            # if we are at a case where there are less numbers
            # between than the actual jump distance, adjust our position
            if potential_next_cur > n // base:
                potential_next_k += base - (n + 1) % base
                decrease_distance = True
            
            if potential_next_k < 1:
                # jumping would overshoot k, so we decrease jump distance
                k -= 1
                cur *= 10
                decrease_distance = True
            else:
                cur = potential_next_cur
                k = potential_next_k
            if decrease_distance:
                base //= 10
                decrement_amount //= 10
        return cur