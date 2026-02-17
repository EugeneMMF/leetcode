class Solution:
  def reverseBits(self, n: int) -> int:
    bits = bin(n)[2:]
    bits = bits[::-1]
    return int(bits, 2) << (32 - len(bits))