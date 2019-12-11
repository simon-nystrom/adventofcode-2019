class Storage:
    hdd = {}
    ram = []

    def __init__(self, code):
        self.ram = code

    def read(self, addr):
        if addr > len(self.ram) - 1:
            if addr in self.hdd:
                return self.hdd[addr]
            else:
                return 0
        return self.ram[addr]

    def write(self, addr, val):
        if addr > len(self.ram) - 1:
            self.hdd[addr] = val 
        else:
            self.ram[addr] = val

class IntcodeComputer:
    PC = 0
    rel_base = 0

    def __init__(self, code):
        self.code = code
        self.storage = Storage(code)
    
    OP_CODE_ARG_NUM_LOOKUP = {
        '01': 3, '02': 3, '03': 1,
        '04': 1, '05': 2, '06': 2,
        '07': 3, '08': 3, '09': 1,
        '99': 0
    }

    MODES = {
        'POSITIONAL': '0',
        'IMMEDIATE': '1',
        'RELATIVE': '2',
    }
    
    RETURN_CODES = {
        'HALT': lambda: (0, 0),
        'OUTPUT': lambda x: (1, x),
        'HAS_MORE': lambda: (2, 0)
    }

    def get_write_addr(self, param, mode):
        if mode == self.MODES['RELATIVE']:
            return param + self.rel_base
        return param

    def get_value(self, param, mode):
        if mode == self.MODES['IMMEDIATE']:
            return param
        if mode == self.MODES['RELATIVE']:
            return self.storage.read(param + self.rel_base)
        return self.storage.read(param)

    def add(self, p1, p2, p3, p1_mode, p2_mode, p3_mode, *_):
        addr = self.get_write_addr(p3, p3_mode)
        self.storage.write(addr, self.get_value(p1, p1_mode) + self.get_value(p2, p2_mode))
        self.PC += 3
        return self.RETURN_CODES['HAS_MORE']()
    
    def mul(self, p1, p2, p3, p1_mode, p2_mode, p3_mode, *_):
        addr = self.get_write_addr(p3, p3_mode)
        self.storage.write(addr, self.get_value(p1, p1_mode) * self.get_value(p2, p2_mode))
        self.PC += 3
        return self.RETURN_CODES['HAS_MORE']()
    
    def store_input(self, p1, p1_mode, _1, _2, program_input):
        addr = self.get_write_addr(p1, p1_mode)
        self.storage.write(addr, program_input)
        self.PC += 1
        return self.RETURN_CODES['HAS_MORE']()

    def output(self, p1, p1_mode, *_):
        self.PC += 1
        return self.RETURN_CODES['OUTPUT'](self.get_value(p1, p1_mode))

    def jnz(self, p1, p2, p1_mode, p2_mode, *unused):
        if self.get_value(p1, p1_mode) != 0:
            self.PC = self.get_value(p2, p2_mode)
        else:
            self.PC += 2
        return self.RETURN_CODES['HAS_MORE']()

    def jz(self, p1, p2, p1_mode, p2_mode, *unused):
        if self.get_value(p1, p1_mode) == 0:
            self.PC = self.get_value(p2, p2_mode)
        else:
            self.PC += 2
        return self.RETURN_CODES['HAS_MORE']()

    def lt(self, p1, p2, p3, p1_mode, p2_mode, p3_mode, *_):
        addr = self.get_write_addr(p3, p3_mode)
        if self.get_value(p1, p1_mode) < self.get_value(p2, p2_mode):
            self.storage.write(addr, 1)
        else:
            self.storage.write(addr, 0)
        self.PC += 3
        return self.RETURN_CODES['HAS_MORE']()
    
    def equals(self, p1, p2, p3, p1_mode, p2_mode, p3_mode, *_):
        addr = self.get_write_addr(p3, p3_mode)
        if self.get_value(p1, p1_mode) == self.get_value(p2, p2_mode):
            self.storage.write(addr, 1)
        else:
            self.storage.write(addr, 0)
        self.PC += 3
        return self.RETURN_CODES['HAS_MORE']()

    def adjust_rel_base(self, p1, p1_mode, *unused):
        self.PC += 1
        self.rel_base += self.get_value(p1, p1_mode)
        return self.RETURN_CODES['HAS_MORE']()

    def halt(self, *_):
        return self.RETURN_CODES['HALT']()

    OP_CODE_HANDLERS = {
        '01': add, '02': mul, '03': store_input,
        '04': output, '05': jnz, '06': jz,
        '07': lt, '08': equals, '09': adjust_rel_base,
        '99': halt,
    }

    def step(self, program_input):
        instruction = str(self.code[self.PC]).zfill(6)
        p3_mode, p2_mode, p1_mode, op_code = instruction[1], instruction[2], instruction[3], instruction[4:]
        self.PC += 1
        args = self.storage.ram[self.PC : self.PC + self.OP_CODE_ARG_NUM_LOOKUP[op_code]]
        return self.OP_CODE_HANDLERS[op_code](self, *args, p1_mode, p2_mode, p3_mode, program_input)
        

