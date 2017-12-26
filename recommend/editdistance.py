def  minEditDistR(target, source):
   """ Minimum edit distance. Straight from the recurrence. """

   i = len(target); j = len(source)

   if i == 0:  return j
   elif j == 0: return i

   return(min(minEditDistR(target[:i-1],source)+1,
              minEditDistR(target, source[:j-1])+1,
              minEditDistR(target[:i-1], source[:j-1])+substCost(source[j-1], target[i-1])))

def substCost(x,y):
    if x == y: return 0
    else: return 2

print(minEditDistR("hello","hilo"))