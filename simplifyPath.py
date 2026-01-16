class Solution:
  def simplifyPath(self, path: str) -> str:
    parts = list(filter(lambda x: x != "", path.split("/")))
    abs = []
    for part in parts:
      if part == "..":
        abs = abs[:-1]
      elif part == ".":
        continue
      else:
        abs.append(part)
    return "/" + "/".join(abs)
  
print(Solution().simplifyPath("/home//foo/"))