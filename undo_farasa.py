## Requires python3

import sys


tarmabuta_plus = "+ة"
tarmabuta = "ة"
at_plus = "+ات"
at = "ات"
a_plus = "+ا"
a = "ا"
iin_plus = "+ين"
iin = "ين"
on_plus = "+ون"
on = "ون"
t_plus = "+ت"
t = "ت"


with open(sys.argv[1]) as f:
  for line in f:
    line = line.rstrip('\n')
    line = line.replace(tarmabuta_plus, tarmabuta)
    line = line.replace(at_plus, at)
    line = line.replace(a_plus, a)
    line = line.replace(iin_plus, iin)
    line = line.replace(on_plus, on)
    line = line.replace(t_plus, t)
    print(line)

#+ة  
#+ات
#+ا
#+ا
#+ين
#+ون
#+ت

