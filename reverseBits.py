class Solution:
  def reverseBits(self, n: int) -> int:
    bits = bin(n)[2:]
    bits = "0"*(32-len(bits)) + bits
    bits = bits[::-1]
    return int(bits, 2)