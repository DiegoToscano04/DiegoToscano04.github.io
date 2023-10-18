import os

class HackAssambler:
    SYMBOL_TABLE = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576,
    }
    COMP = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101"
    }
    DEST = {
        "null": "000",
        "M": "001",
        "D": "010",
        "A": "100",
        "MD": "011",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }
    JUMP = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }

    VARIABLE_SPOT=16
    def __init__(self, file):
        self.fullFill()
        self.firstPass(file)
        self.secondPass(file)

    def firstPass(self, name):
        original = open(name + ".asm")
        tmp=open(name + ".tmp", "w")

        linecounter = 0
        for line in original:
            tmpline = self.strip(line)
            if tmpline != "":
                if tmpline[0] == "(":
                    self.SYMBOL_TABLE[tmpline[1:-1]] = linecounter
                    tmpline = ""
                else:
                    linecounter += 1
                    tmp.write(tmpline + "\n")
        original.close()
        tmp.close()

    def secondPass(self, name):
        tmp = open(name + ".tmp")
        endfile = open(name + ".hack", "w")
        for line in tmp:
            tmpline = self.translate(line.split("\n")[0])
            endfile.write(tmpline + "\n")
        tmp.close()
        endfile.close()
        os.remove(name + ".tmp")

    def translate(self, line):
        if line[0] == "@":
            return self.translateA(line)
        else:
            return self.translateC(line)

    def translateA(self, line):
        if line[1].isalpha():
            value = self.SYMBOL_TABLE.get(line[1:], -1)
            if value == -1:
                self.SYMBOL_TABLE[line[1:]] = self.VARIABLE_SPOT
                value = self.VARIABLE_SPOT
                self.VARIABLE_SPOT += 1
        else:
            value = int(line[1:])
        return format(value,"b").zfill(16)

    def translateC(self, line):
        tmpline = line
        if not "=" in line:
            tmpline = "null=" + line
        if not ";" in line:
            tmpline = tmpline + ";null"
        tmpline = tmpline.split("=")
        dest = self.DEST.get(tmpline[0])
        tmpline = tmpline[1].split(";")
        comp = self.COMP.get(tmpline[0])
        jump = self.JUMP.get(tmpline[1])
        return "111" + comp + dest + jump





    def strip(self, line):
        if line[0] == "\n" or line[0] == "/":
            return ""
        elif line[0] == " ":
            return self.strip(line[1:])
        else:
            return line[0] + self.strip(line[1:])

    def fullFill(self):
        for i in range (0,16):
            self.SYMBOL_TABLE["R" + str(i)]=i

HackAssambler("Add")
HackAssambler("Max")
HackAssambler("MaxL")
HackAssambler("Pong")
HackAssambler("PongL")
HackAssambler("Rect")
HackAssambler("RectL")