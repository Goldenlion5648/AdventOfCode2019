from math import *
from collections import deque
# signal = 80871224585914546619083218645595
signal = 69317163492948606335995924319873
signal = 12345678
signal = 19617804207202209144916044189917
# signal = 59791871295565763701016897619826042828489762561088671462844257824181773959378451545496856546977738269316476252007337723213764111739273853838263490797537518598068506295920453784323102711076199873965167380615581655722603274071905196479183784242751952907811639233611953974790911995969892452680719302157414006993581489851373437232026983879051072177169134936382717591977532100847960279215345839529957631823999672462823375150436036034669895698554251454360619461187935247975515899240563842707592332912229870540467459067349550810656761293464130493621641378182308112022182608407992098591711589507803865093164025433086372658152474941776320203179747991102193608
digits = list(map(int, str(signal)))
print(digits)

OGpattern = deque([0, 1, 0, -1]) 
pattern = deque(OGpattern * (ceil(len(digits) //len(OGpattern)) + 1))

total = 0

phaseNum = 0
totalPhaseCount = 4
totalPhaseCount = 1000
newDigits = deque([])
seen = deque()
while phaseNum < totalPhaseCount:
    # print(pattern)
    for j in range(len(digits)):
        pos = 0
        total = 0
        # print('pattern before', pattern)
        pattern.popleft()
        # print('pattern after', pattern)
        while pos < len(digits):
            # print(pos)
            cur = digits[pos] * pattern[pos]
            total += cur
            # print(digits[pos], pattern[pos],'equals', cur)
            # print(total)
            pos += 1
        # print("total", total)
        newDigits.append(abs(total)%10)
        # print('cur newDigits', newDigits)
        pattern = deque([])
        # if j != 0:
        for x in range(len(OGpattern)):
            pattern += [OGpattern[x]] * (j+2)
        # else:
        #     pattern = deque(OGpattern * (ceil(len(digits) //len(OGpattern)) + 1))
        pattern = deque(pattern * (ceil(len(digits) //len(pattern)) + 1))
    pattern = deque(OGpattern * (ceil(len(digits) //len(OGpattern)) + 1))

    digits = newDigits.copy()
    if digits not in seen:
        seen.append(digits.copy())
    else:
        print("broke out on", phaseNum)
        print("seen at", seen.index(digits))
        break
    # print("newDigits",newDigits)
    newDigits = deque([])
    phaseNum += 1
        
print("newDigits",digits)
print(list(digits)[:8])