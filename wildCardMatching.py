class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    s_ind, p_ind = 0, 0
    match, star = 0, -1
    len_s, len_p = len(s), len(p)
    while s_ind < len_s:
      if p_ind < len_p and (p[p_ind] == '?' or p[p_ind] == s[s_ind]):
        s_ind += 1
        p_ind += 1
      elif p_ind < len_p and p[p_ind] == '*':
        star = p_ind
        match = s_ind
        p_ind += 1
      elif star != -1:
        p_ind = star + 1
        match += 1
        s_ind = match
      else:
        return False
    while p_ind < len_p and p[p_ind] == '*':
      p_ind += 1
    return p_ind == len_p