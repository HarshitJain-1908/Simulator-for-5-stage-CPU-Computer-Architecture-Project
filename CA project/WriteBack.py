# Must run in the first half of the clock cycle
class WriteBack:
    
    def writeback(self, RegisterFile, ex_o): #EXECUTE OUTPUT is the input parameter here
        #Assuming that EXECUTE_OUTPUT is a set {"instruction" : "...", "rd" : '...'}
        # sleep(0.25)

        if ex_o["instruction"] not in ["BEQ", "SW"]:

            if ex_o["instruction"] == "LW":
                RegisterFile[int(ex_o["rd"], 2)].setValue(ex_o["memValue"]) 
            else:
                RegisterFile[int(ex_o["rd"], 2)].setValue(ex_o["result"]) 

            # return RegisterFile

        