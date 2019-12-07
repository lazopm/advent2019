# operations
END = 99
ADD = 1
MUL = 2
IN = 3
OUT = 4
JMP_IFT = 5
JMP_IFF = 6
LESS = 7
EQL = 8

# param modes
POS_MODE = 0
VAL_MODE = 1

PARAM_ARITY = {
    END: 0,
    ADD: 3,
    MUL: 3,
    IN: 1,
    OUT: 1,
    JMP_IFT: 2,
    JMP_IFF: 2,
    LESS: 3,
    EQL: 3,
}

class Runtime:
    def __init__(self, program, input=None, output=None):
        self.program = program.copy()
        self.input_count = 0
        self.cursor = 0
        self.input = input
        self.output = output

    def _parse_instruction(self, instruction):
        opcode = int(instruction[-2:])
        arity = PARAM_ARITY[opcode]
        modecodes = list(instruction[:-2])
        modecodes.reverse()
        if arity > 0:
            modes = [int(modecodes[i]) if len(modecodes) > i else 0 for i in range(0, arity)]
        else: modes = None
        return (opcode, modes)

    def _read_params(self, modes):
        params = []
        for i in range(0, len(modes)):
            pos = self.cursor + i + 1;
            mode = modes[i]
            val = int(self.program[pos])
            if mode == VAL_MODE:
                params.append(val)
            elif mode == POS_MODE:
                params.append(int(self.program[val]))
        return params

    def _write_param(self, pos, val):
        write_pos = int(self.program[pos])
        self.program[write_pos] = str(val)

    def _input(self):
        if (self.input != None):
            return self.input(self)
        return input('user input #' + str(self.input_count + 1) +': ')

    def _output(self, val):
        if (self.output != None):
            self.output(val, self)
            return
        print('output: ' + str(val))

    def _execute_instruction(self):
        opcode, modes = self._parse_instruction(self.program[self.cursor])

        if opcode == END:
            self.running = False
            return
        elif opcode == ADD:
            a,b,*_ = self._read_params(modes);
            self._write_param(self.cursor + 3, a + b)
        elif opcode == MUL:
            a,b,*_ = self._read_params(modes);
            self._write_param(self.cursor + 3, a * b)
        elif opcode == IN:
            val = self._input()
            self._write_param(self.cursor + 1, val)
        elif opcode == OUT:
            a,*_ = self._read_params(modes)
            self._output(a)
        elif opcode == JMP_IFT:
            a,b,*_ = self._read_params(modes)
            if a != 0:
                self.cursor = b
                return
        elif opcode == JMP_IFF:
            a,b,*_ = self._read_params(modes)
            if a == 0:
                self.cursor = b
                return
        elif opcode == LESS:
            a,b,*_ = self._read_params(modes)
            self._write_param(self.cursor + 3, 1 if a < b else 0)
        elif opcode == EQL:
            a,b,*_ = self._read_params(modes)
            self._write_param(self.cursor + 3, 1 if a == b else 0)

        self.cursor += (PARAM_ARITY[opcode] + 1)

    def is_halted(self):
        opcode, _ = self._parse_instruction(self.program[self.cursor])
        return opcode == END

    def run_program(self):
        self.running = True
        while self.running == True:
            self._execute_instruction()


program = open('input.txt', 'r').read().strip().split(',')

#part 1
class Amps:
    def __init__(self, settings):
        self.done = False
        self.last_output = 0
        self.settings = settings
        Runtimk(program, self.input, self.output).run_program()
        Runtime(program, self.input, self.output).run_program()
        Runtime(program, self.input, self.output).run_program()
        Runtime(program, self.input, self.output).run_program()
        Runtime(program, self.input, self.output).run_program()

    def input(self):
        if self.done == False:
            self.done = True
            return str(self.settings.pop())
        self.done = False
        return str(self.last_output)
    def output(self, val):
        self.last_output = val

#part 2
class FeedbackAmps:
    def __init__(self, settings):
        self.last_output = 0
        self.settings = settings
        self.settings.reverse()

        runtimes = [
            Runtime(program, self.input, self.output),
            Runtime(program, self.input, self.output),
            Runtime(program, self.input, self.output),
            Runtime(program, self.input, self.output),
            Runtime(program, self.input, self.output),
        ]

        while set(map(lambda r: r.is_halted(), runtimes)) != set([True]):
            for runtime in runtimes:
                if runtime.is_halted() == False:
                    runtime.run_program()

        print(list(map(lambda r: r.setting, runtimes)), self.last_output)


    def input(self, runtime):
        if hasattr(runtime, 'setting'):
            #jprint(runtime.setting, 'in', self.last_output)
            return str(self.last_output)
        setting = str(self.settings.pop())
        runtime.setting = setting
        return setting

    def output(self, val, runtime):
        #print(runtime.setting, 'out', self.last_output)
        self.last_output = val
        runtime.running = False

from itertools import permutations
max_thrust = 0
for settings in permutations([5,6,7,8,9]):
    print(settings)
    out = FeedbackAmps(list(settings)).last_output
    max_thrust = max(max_thrust, out)
print(max_thrust)
