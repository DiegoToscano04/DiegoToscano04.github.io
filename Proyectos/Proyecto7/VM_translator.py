import os

class VM_tanslator:
    TYPE = {
        'add': 'C_ARITHMETIC',
        'sub': 'C_ARITHMETIC',
        'neg': 'C_ARITHMETIC',
        'eq': 'C_ARITHMETIC',
        'gt': 'C_ARITHMETIC',
        'lt': 'C_ARITHMETIC',
        'and': 'C_ARITHMETIC',
        'or': 'C_ARITHMETIC',
        'not': 'C_ARITHMETIC',
        'push': 'C_PUSH',
        'pop': 'C_POP',
        'label': 'C_LABEL',
        'goto': 'C_GOTO',
        'if-goto': 'C_IF',
        'function': 'C_FUNCTION',
        'return': 'C_RETURN',
        'call': 'C_CALL'
    }
    BOOLEANS = 0
    BASIC_ADDRESS={
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
        'pointer': 3,
        'temp': 5,
        'static': 16,
    }

    def __init__(self, filename):
        self.firstParse(filename)
        self.parse(filename)

    def firstParse(self, filename):
        original = open(filename + ".vm")
        tmp = open(filename + ".tmp", "w")
        for line in original:
            tmpline = self.strip(line)
            if tmpline != "":
                tmp.write(tmpline + "\n")
        original.close()
        tmp.close()

    def strip(self, line):
        if line[0] == "\n" or line[0] == "/":
            return ""
        else:
            return line[0] + self.strip(line[1:])

    def parse(self, filename):
        tmp = open(filename + ".tmp")
        endfile = open(filename + ".asm", "w")
        for line in tmp:
            aux = self.commandType(line)
            endfile.write("// " + line + "\n")
            endfile.write(aux)
        tmp.close()
        endfile.close()
        os.remove(filename + ".tmp")

    def commandType(self, line):
        aux = line.split()

        if self.TYPE[aux[0]] == "C_ARITHMETIC":
            return self.arithmetic(aux[0])
        if self.TYPE[aux[0]] == "C_PUSH" or "C_POP":
            return self.pushPop(aux)

    def arithmetic(self, line):
        newline = ""
        if line not in ["not","neg"]:
             newline = self.pop_Stack()
        newline += self.decrement_SP()
        newline += self.SP()
        if line == "add":
            newline += "M=M+D\n"
        elif line == "sub":
            newline += "M=M-D\n"
        elif line == "and":
            newline += "M=M&D\n"
        elif line == "or":
            newline += "M=M|D\n"
        elif line == "neg":
            newline += "M=-M\n"
        elif line == "not":
            newline += "M=!M\n"

        elif line in ["eq","ls","gt"]:
            newline += "D=M-D\n"
            newline += "@C{}\n".format(self.BOOLEANS)

            if line == "eq":
                newline += "D;JEQ\n"
            elif line == "ls":
                newline += "D;JLT\n"
            elif line == "gt":
                newline += "D;JGT\n"

            newline += self.SP() + "M=0\n"
            newline += "@CONTINUE{}\n".format(self.BOOLEANS) + "0;JMP\n"

            newline += "(C{})".format(self.BOOLEANS)
            newline += self.SP() + "M=-1\n"

            newline += "(CONTINUE{})\n".format(self.BOOLEANS)
            self.BOOLEANS += self.BOOLEANS
        newline += self.increment_SP()
        return newline

    def SP(self):
        return "@SP\n" + "A=M\n"

    def increment_SP(self):
        return "@SP\n" + "M=M+1\n"

    def decrement_SP(self):
        return "@SP\n" + "M=M-1\n"

    def pop_Stack(self):
        return self.decrement_SP() + "A=M\n" + "D=M\n"

    def push_Stack(self):
        return self.SP() + "M=D\n" + self.increment_SP()

    def pushPop(self, line):
        newline = self.address(line[1], line[2])
        if line[0] == "push":
            if line[1] == "constant":
                newline += "D=A\n"
            else:
                newline += "D=M\n"
            newline += self.push_Stack()
        elif line[0] == "pop":
            newline += "D=A\n"
            newline += "@R14\n"
            newline += "M=D\n"
            newline += self.pop_Stack()
            newline += "@R14\n"
            newline += "A=M\n"
            newline += "M=D\n"

        return newline

    def address(self, segment, index):
        address = self.BASIC_ADDRESS.get(segment)
        aux = ""
        if segment == "constant":
            return "@" + str(index) + "\n"
        elif segment == "static":
            return "@static." + str(index) + "\n"
        elif segment in ["pointer","temp"]:
            return "@R" + str(address + int(index)) + "\n"
        elif segment in ["local", "this", "that", "argument"]:
            aux = "@" + address + "\n"
            aux += "D=M\n"
            aux += "@" + str(index) + "\n"
            aux += "A=D+A\n"
            return aux

VM_tanslator("BasicTest")
VM_tanslator("PointerTest")
VM_tanslator("SimpleAdd")
VM_tanslator("StackTest")
VM_tanslator("StaticTest")
