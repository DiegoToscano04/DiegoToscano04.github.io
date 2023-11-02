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
    BASIC_ADDRESS = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT',
        'pointer': 3,
        'temp': 5,
        'static': 16,
    }
    CURRENT_FILE = None
    CALLS = 0
    FUNCTIONS = 0

    def __init__(self, main_path):
        vmlist = []
        for item in os.listdir(main_path):
            if item.endswith(".vm"):
                vmlist.append(item)

        path = main_path.split("\\")[-1]
        file = open(path + ".asm", "w")
        path = map(lambda x: main_path + "\\" + x, vmlist)

        newline = "@256\n" + "D=A\n" + "@SP\n" + "M=D\n" + self.write_call("call Sys.init 0".split())
        file.write(newline)
        i = 0
        for p in path:
            self.CURRENT_FILE = vmlist[i].replace(".vm", "")
            self.firstParse(p)
            self.parse(p, file)
            i += 1
        file.close()

    def firstParse(self, filename):
        original = open(filename)
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

    def parse(self, filename, endfile):
        tmp = open(filename + ".tmp")

        for line in tmp:
            aux = self.commandType(line)
            endfile.write("// " + line + "\n")
            endfile.write(aux)
        tmp.close()
        os.remove(filename + ".tmp")

    def commandType(self, line):
        aux = line.split()

        if self.TYPE[aux[0]] == "C_ARITHMETIC":
            return self.arithmetic(aux[0])
        elif self.TYPE[aux[0]] == "C_PUSH":
            return self.pushPop(aux)
        elif self.TYPE[aux[0]] == "C_POP":
            return self.pushPop(aux)
        elif self.TYPE[aux[0]] == "C_LABEL":
            return self.label(aux[1])
        elif self.TYPE[aux[0]] == "C_GOTO":
            return self.goto(aux[1])
        elif self.TYPE[aux[0]] == "C_IF":
            return self.write_if(aux)
        elif self.TYPE[aux[0]] == "C_FUNCTION":
            return self.write_function(aux)
        elif self.TYPE[aux[0]] == "C_RETURN":
            return self.write_return()
        elif self.TYPE[aux[0]] == "C_CALL":
            return self.write_call(aux)

    def arithmetic(self, line):
        newline = ""
        if line not in ["not", "neg"]:
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

        elif line in ["eq", "lt", "gt"]:
            newline += "D=M-D\n"
            newline += "@C{}\n".format(self.BOOLEANS)

            if line == "eq":
                newline += "D;JEQ\n"
            elif line == "lt":
                newline += "D;JLT\n"
            elif line == "gt":
                newline += "D;JGT\n"

            newline += self.SP() + "M=0\n"
            newline += "@CONTINUE{}\n".format(self.BOOLEANS) + "0;JMP\n"

            newline += "(C{})\n".format(self.BOOLEANS)
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
            newline += "@R13\n"
            newline += "M=D\n"
            newline += self.pop_Stack()
            newline += "@R13\n"
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

    def label(self, line):
        return "({}${})".format(self.CURRENT_FILE, line) + "\n"

    def goto(self, line):
        return "@{}${}".format(self.CURRENT_FILE, line) + "\n" + "0;JMP\n"

    def write_if(self, line):
        return self.pop_Stack() + "@{}${}".format(self.CURRENT_FILE, line[1]) + "\n" + "D;JNE\n"

    def write_function(self, line):

        newline = "({})\n".format(line[1])
        newline += "@{}\n".format(line[2])
        newline += "D=A\n"
        newline += "(LOOP.ADD_LOCALS.{})\n".format(self.FUNCTIONS)
        newline += "@NO_LOCALS.{}\n".format(self.FUNCTIONS)
        newline += "D;JEQ\n"
        newline += "@SP\n"
        newline += "A=M\n"
        newline += "M=0\n"
        newline += "@SP\n"
        newline += "M=M+1\n"
        newline += "D=D-1\n"
        newline += "@LOOP.ADD_LOCALS.{}\n".format(self.FUNCTIONS)
        newline += "D;JNE\n"
        newline += "(NO_LOCALS.{})\n".format(self.FUNCTIONS)
        return newline

    def write_call(self, line):
        REF = line[1] + "REF" + str(self.CALLS)
        self.CALLS += 1
        newline = "@" + REF + "\n"
        newline += "D=A\n"
        newline += self.push_Stack()

        for x in ["@LCL", "@ARG", "@THIS", "@THAT"]:
            newline += x + "\n"
            newline += "D=M\n"
            newline += self.push_Stack()

        newline += "@SP\n"
        newline += "D=M\n"
        newline += "@{}\n".format(line[2])
        newline += "D=D-A\n"

        newline += "@5\n"
        newline += "D=D-A\n"
        newline += "@ARG\n"
        newline += "M=D\n"

        newline += "@SP\n"
        newline += "D=M\n"
        newline += "@LCL\n"
        newline += "M=D\n"

        newline += "@" + line[1] + "\n"
        newline += "0;JMP\n"
        newline += "({})\n".format(REF)

        return newline

    def write_return(self):
        FRAME = "R13"
        REF = "R14"

        newline = "@LCL\n"
        newline += "D=M\n"
        newline += "@" + FRAME + "\n"
        newline += "M=D\n"
        newline += "@5\n"
        newline += "D=A\n"
        newline += "@" + FRAME + "\n"
        newline += "A=M-D\n"
        newline += "D=M\n"
        newline += "@" + REF + "\n"
        newline += "M=D\n"

        newline += self.pop_Stack()

        newline += "@ARG\n"
        newline += "A=M\n"
        newline += "M=D\n"

        newline += "@ARG\n"
        newline += "D=M+1\n"
        newline += "@SP\n"
        newline += "M=D\n"

        i = 1

        for x in ["@THAT", "@THIS", "@ARG", "@LCL"]:
            newline += "@" + str(i) + "\n"
            newline += "D=A\n"
            newline += "@" + FRAME + "\n"
            newline += "A=M-D\n"
            newline += "D=M\n"
            newline += x + "\n"
            newline += "M=D\n"
            i += 1

        newline += "@" + REF + "\n"
        newline += "A=M\n"
        newline += "0;JMP\n"

        return newline








VM_tanslator("C:\\Users\\ASUS\\Desktop\\nand2tetris\\projects\\08\\FunctionCalls\\SimpleFunction")
