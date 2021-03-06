class Heilda:

    def __init__(self, f, g, x1, x2):
        self.f = self.endurSkrifa(f)
        self.g = self.endurSkrifa(g)
        self.F = self.heild(self.f)
        self.G = self.heild(self.g)
        self.x1 = x1
        self.x2 = x2

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

    def reikna(self, F, x):
        value = 0
        reikna = ""
        for i in F:
            if(i[1] == "-x"):
                if(i[2] % 2 == 0):
                    value += i[0] * x ** i[2]
                else:
                    value += i[0] * -(x ** i[2])
            else:
                value += i[0] * x ** i[2]


        return value

    def flatarmal(self, F):
        return self.reikna(F, self.x1) - self.reikna(F, self.x2)

    def Reiknaflatarmal(self):
        return round(abs(self.flatarmal(self.F) - self.flatarmal(self.G)),2)

    def test(self):
        return self.reikna(self.F, 3)


test = Heilda(input("Sláðu inn fall f(x) = "), input("Sláðu inn fall g(x) = "), int(input("Sláðu inn x fyrir efri mörk svæðis: ")), int(input("Sláðu inn x fyrir neðri mörk svæðis: ")))
print(" ")
print("Flatarmálið milli f(x) og g(x) er: {}".format(test.Reiknaflatarmal()))


