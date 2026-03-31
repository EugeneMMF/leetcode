class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True

            if tx == ty:
                # If tx and ty are equal, we cannot perform any backward operation
                # to get distinct positive integers.
                # Since the (tx, ty) point is not (sx, sy) (handled above),
                # it means (sx, sy) is unreachable from this path.
                return False

            if tx > ty:
                # The point (tx, ty) could only have come from (tx - ty, ty).
                # If ty is already sy, we must reduce tx to sx by subtracting ty.
                # Any further change to ty would make it unequal to sy.
                if ty == sy:
                    # Check if (tx - sx) is a non-negative multiple of ty.
                    # This means tx must be greater than or equal to sx,
                    # and the difference (tx - sx) must be perfectly divisible by ty.
                    return (tx >= sx) and ((tx - sx) % ty == 0)
                else:
                    # If ty is not sy, we can subtract ty from tx multiple times
                    # until tx is less than ty. This is equivalent to tx = tx % ty.
                    # If tx becomes 0, it means it was a multiple of ty. In this scenario,
                    # the previous valid point would have been (ty, ty), which we determined
                    # cannot be reached unless it was the starting point (sx, sy).
                    # The loop condition `tx >= sx` will handle this: if tx becomes 0,
                    # and sx >= 1, the loop terminates and correctly returns False.
                    tx %= ty
            else:  # ty > tx
                # The point (tx, ty) could only have come from (tx, ty - tx).
                # If tx is already sx, we must reduce ty to sy by subtracting tx.
                # Any further change to tx would make it unequal to sx.
                if tx == sx:
                    # Check if (ty - sy) is a non-negative multiple of tx.
                    # This means ty must be greater than or equal to sy,
                    # and the difference (ty - sy) must be perfectly divisible by tx.
                    return (ty >= sy) and ((ty - sy) % tx == 0)
                else:
                    # If tx is not sx, we can subtract tx from ty multiple times.
                    # Equivalent to ty = ty % tx.
                    # Similar to the tx > ty case, if ty becomes 0, the loop
                    # condition `ty >= sy` will handle it.
                    ty %= tx
        
        # If the loop terminates because tx < sx or ty < sy without ever
        # reaching the exact (sx, sy) point, then it's impossible to
        # convert (sx, sy) to (tx, ty).
        return False

