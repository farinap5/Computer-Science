class Machine(object):
    def __init__(self, init:str="q0", accept:str="q0",ptr:int=0,tape:list=[]) -> None:
        self.init   = init
        self.accept = accept
        self.tape   = tape
        self.ptr    = ptr
        self.Q      = {}
        self.state  = init
        self.tapeLen = len(tape)

    def setRule(self, state, read, nstate, write, move) -> None:
        self.Q[(state,read)] = (nstate, write, move)
    
    def setTape(self,tape:list) -> None:
        self.tape = tape
        self.tapeLen = len(tape)

    def setAccept(self,accept:str) -> None:
        self.accept = accept
    
    def step(self):
        self.state,self.tape[self.ptr],d = self.Q[(self.state,self.tape[self.ptr])]
        if d == ">":
            self.ptr += 1
        elif d == "<":
            self.ptr -= 1
        elif d == "h":
            pass
        else:
            return (True,4)
        
        if self.state == self.accept:
            return (True,1)
        elif self.tapeLen == self.ptr:
            return (True,2)
        elif self.ptr < 0:
            return (True,3)
        else:
            return (False,0)

    def run(self) -> None:
        c = None
        while True:
            x,c = self.step()
            if x:
                break
        return c

if __name__ == "__main__":
    x = Machine()
    x.setTape(["a","a","a","a","a",""])

    # δ(q0,a) = (q0,b,>)
    x.setRule("q0","a","q0","b",">")
    # δ(q0,_) = (q1,b,>)
    x.setRule("q0","","q1","b",">")
    x.setAccept("q1")
    print(x.tape)
    print(x.run())
    print(x.tape)

# M = {Q,∑,δ,q0,F,B}
# δ(q0,a) = (q1,b,>)

# Status
# 0 pass
# 1 accepted
# 2 Length exceded
# 3 ptr under zero
# 4 direction error