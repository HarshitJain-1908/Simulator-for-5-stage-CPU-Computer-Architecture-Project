# Runs in the second half of the clock cycle. Must be triggered only after the first half of the clock cycle
# Decode the instruction and read the registers corresponding to register
# source specifiers from the register file. Do the equality test on the 
# registers as they are read, for a possible branch.
# The decoded instruction will be returned in the form of a dictionary,
# with format {"instruction" : "...", "rd" : '...', "rs1" : '...', "rs2" : '...', 'imm' : '...'}

class Decode: 

    def decode(self, inst, RegisterFile):
        
        # sleep(0.25)

        opcode = inst[-7 : ]
        if opcode == '0110011':
            return self.R_type(inst[ : -7], RegisterFile)
        
        elif opcode == '0010011':
            return self.ADDI(inst[ : -7], RegisterFile)
        
        elif opcode == '0000011':
            return self.LW(inst[ : -7], RegisterFile)
        
        elif opcode == '0100011':
            return self.SW(inst[ : -7], RegisterFile)
        
        elif opcode == '1100011':
            return self.BEQ(inst[ : -7], RegisterFile)


    def R_type(self, inst, RegisterFile):
        Dict = {}
        Dict["rd"] = inst[-5 : ]
        Dict['rs1'] = RegisterFile[int(inst[-13: -8], 2)].getValue()
        Dict['rs2'] = RegisterFile[int(inst[-18:-13], 2)].getValue()

        funct3 = inst[-8 : -5]
        if funct3 == '111':
            Dict["instruction"] = "AND"
        
        elif funct3 == '110':
            Dict["instruction"] = "OR"

        elif funct3 == '000':
            if inst[0:7] == '0000000':
                Dict["instruction"] = "ADD"
            
            else:
                Dict["instruction"] = "SUB"
        
        elif funct3 == '001':
            Dict["instruction"] = "SLL"
        
        elif funct3 == '101':
            Dict["instruction"] = "SRA"
        
        return Dict

    def ADDI(self, inst, RegisterFile):
        Dict = {}
        Dict["instruction"] = "ADDI"
        Dict["rd"] = inst[-5:]
        Dict["rs1"] = RegisterFile[int(inst[-13:-8], 2)].getValue()
        Dict["imm"] = inst[0 : 12]
        return Dict

    def LW(self, inst, RegisterFile):
        Dict = {}
        Dict["instruction"] = "LW"
        Dict["rd"] = inst[-5:]
        Dict["rs1"] = RegisterFile[int(inst[-13:-8], 2)].getValue()
        Dict["imm"] = RegisterFile[int(inst[0:12], 2)].getValue()
        return Dict

    def SW(self, inst, RegisterFile):
        Dict = {}
        Dict["instruction"] = "SW"
        Dict["rs1"] = RegisterFile[int(inst[-13:-8], 2)].getValue()
        Dict["rs2"] = RegisterFile[int(inst[-18:-13], 2)].getValue()
        Dict["imm"] = inst[0:6] + inst[-5:]
        return Dict

    def BEQ(self, inst, RegisterFile):
        Dict = {}
        Dict["instruction"] = "BEQ"
        Dict["rs1"] = RegisterFile[int(inst[-13:-8], 2)].getValue()
        Dict["rs2"] = RegisterFile[int(inst[-18:-13], 2)].getValue()
        Dict["imm"] = inst[0] + inst[-1] + inst[1:7]  + inst[-5:-1] +'0'
        if Dict["rs1"] == Dict["rs2"]: #check equality
            # Main.branch_target(Dict["imm"]) # branch_target should change the PC value to PC + 4 + Dict["imm"]
            #The next instruction should be executed
            return None
        else:
            return Dict