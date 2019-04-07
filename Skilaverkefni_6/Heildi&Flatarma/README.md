# 1. ( 5/15 ) Heildi og flatarmál


Útfærðu forrit sem tekur inn tvö föll f(x) og g(x) og tvö gildi á talnalínu x1 og x2. Forritið þitt á
síðan að nota ákveðið heildi til að reikna flatarmál svæðis sem myndast milli f(x) og g(x) á bilinu
x1 og x2. Dæmi um keyrslu:


### Hverning ég leysti þetta.

* Ég byrja á því að endurskrifa föllin f og g. Svo ég enda alltaf með lista með listum með þrem stöðum. Dæmi, þú byrir meða þetta 2x2+2x+2 kalla á fallið og færð þetta [[2,x,2],[2,x],[2,x,1]]

```python

    def endurSkrifa(self, f):
        temp = ""
        f1 = []
        f2 = []
        for i in f:
            if (i == "x"):
                if (temp != "-"):
                    if (temp != ""):
                        f1.append(temp)

                    f1.append("x")
                    temp = ""
                else:
                    f1.append("-x")
                    temp = ""
            elif (i == "-"):
                if (len(f2) > 0):
                    if (temp != ""):
                        f1.append(temp)
                    f2.append(f1)
                    f1 = []
                    temp = "-"
                else:
                    temp = "-"
            elif (i == "+"):
                if (temp != ""):
                    f1.append(temp)
                temp = ""
                f2.append(f1)
                f1 = []
            else:
                temp += i
        if (temp != ""):
            f1.append(temp)
        f2.append(f1)

        for i in range(len(f2)):
            if (len(f2[i]) == 1):
                if (f2[i][0] == "x"):
                    f2[i].append(f2[i][0])
                    f2[i][0] = 1
                    f2[i].append(1)
            if (len(f2[i]) == 2):
                if (f2[i][1] == "x"):
                    f2[i].append(1)
                elif (f2[i][0] == "x" or f2[i][0] == "-x"):
                    f2[i].insert(0, 1)
                if (f2[i][0] == "-"):
                    f2[i][0] = "-1"

        return f2
```

* Næsta skref heilda ég. Þá nota ég heilda fallið.

```python

    def heild(self, f):
        tempf = f
        for i in range(len(tempf)):
            if (len(tempf[i]) == 1):
                tempf[i][0] = int(tempf[i][0])
                tempf[i].append("x")
                tempf[i].append(1)
            elif (len(tempf[i]) == 3):
                tempf[i][0] = int(tempf[i][0]) / ((int(tempf[i][2])) + 1)
                tempf[i][2] = int(tempf[i][2]) + 1
        return tempf
```

* Svo svara hin sér sjálf.