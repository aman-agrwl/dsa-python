def valid_anagram(s1: str, s2: str):
  if len(s1) != len(s2):
    return False
  
  char_freq= {}
  
  for char in s1:
    char_freq[char] = char_freq.get(char, 0) + 1
    
    
  for char in s2:
    if char not in char_freq:
      return False
    
    char_freq[char]-=1
    
    if char_freq[char] ==0:
      del char_freq[char]
      
  return len(char_freq) == 0
      
  