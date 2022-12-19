import abc
"""
6bit cpu
has 64 value holders  which can hold up tp 64 bits
has 64 command holders which can hold up to [6bit,6bit,6bit]

there only 64 instructions






data types:
0-1 boolean
0-64 integer
"""

class BitHolder(abc.ABC):
    @abc.abstractmethod
    def read():
        pass

    @abc.abstractmethod
    def write():
        pass

class BitHolderSuperClass(BitHolder):
    def __init__(self, bit_len):
        self.value = []
        for i1 in range(bit_len):
            self.value.append(0)


    def read(self):
        return self.value


    def write(self, value):
        self.value = value


class _6BitHolder(BitHolderSuperClass):
    bit_len = 6
    def __init__(self):
        BitHolderSuperClass.__init__(self, 6)

class _6BitHolder_ReadOnly(BitHolderSuperClass):
    bit_len = 6
    def __init__(self):
        BitHolderSuperClass.__init__(self, 6)

    def write(self, value):
        pass


class CommandHolder():
    def __init__(self):
        self.addrs_holder = _6BitHolder_ReadOnly()
        self.uniuqe_code_holder = _6BitHolder()
        self.arg1_holder = _6BitHolder()
        self.arg2_holder = _6BitHolder()

    def return_addrs(self):
        return self.addrs_holder.read()


class AddresedValueHolder():
    def __init__(self, is_read_only=False):
        self.addrs_holder = _6BitHolder_ReadOnly()
        if is_read_only == True:
            self.value = _6BitHolder_ReadOnly()
        else:
            self.value = _6BitHolder()
        self.is_read_only = is_read_only

    def return_addrs(self):
        return self.addrs_holder.read()

    def return_value(self):
        return self.value

    def set_value(self, value):
        self.value = value




def uf1(n, m):
    output = []
    for i1 in range(2**6):
        this = m()
        a = bin(i1)
        a = str(a)[2:][::-1]
        for i1 in range(n-len(a)):
            a += "0"
        a = list(a)
        a = list(map(int, a))
        print(a)
        this.addrs_holder.write(a)
        output.append(this)


def uf2(n):
    output = []
    for i1 in range(6):
        output.append(_6BitHolder())
    return output



class CommandConstatData:
    def __init__(self, command_kw, command_unique_code, has_arg_1=False, has_arg_2=False):
        self.command_kw = command_kw
        self.command_unique_code = command_unique_code
        self.has_arg_1 = has_arg_1
        self.has_arg_2 = has_arg_2

def int2binlis(b:int)->list:
    #only works for values which are integer and has no sign !
    a = bin(b)
    a = str(a)[2:][::-1]
    for i1 in range(6-len(a)):
        a += "0"
    a = list(a)
    a = list(map(int, a))
    return a

def binlis2int(a:list)->int:
    b = "0b"
    for i1 in a[::-1]:
        b += str(i1)
    b = eval(b)
    return b

commands = """
read
write
readAVO
readAVO
and
or
xor
nand
nor
inv
jump
add
sub
copy
empty
dec
inc
shiftleft
shiftright
reverse
define
copyAVO
defineAVO
bitlen
fillCom
pass
"""

def assemble(code:str):
    pass


class FellowSimulatedCpu:
    def __init__(self):
        self.value_holders = uf2(6)
        self.CommandHolders = uf1(6, CommandHolder)


FellowSimulatedCpu()
