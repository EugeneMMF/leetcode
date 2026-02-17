/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
  sMap = {};
  tMap = {};
  if (s.length != t.length) return false;
  for (let i=0; i<s.length; i++) {
    if (sMap[s[i]] !== undefined) {
      if (t[i] != sMap[s[i]]) return false;
    } else {
      sMap[s[i]] = t[i];
      if (tMap[t[i]] !== undefined) return false;
      tMap[t[i]] = s[i];
    }
  }
  return true;
};