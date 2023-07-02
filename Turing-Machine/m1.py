from machine import Machine

m = Machine()
m.setTape(["a","a","a","b","b",""])

# (q0,a)=(q0,a,>)
m.setRule("q0","a","q0","a",">")
# (q0,b)=(q1,b,>)
m.setRule("q0","b","q1","b",">")
# (q0,_)=(q2,_,>)
m.setRule("q0","","q1","",">")
# (q1,b)=(q1,b,>)
m.setRule("q1","b","q1","b",">")
# (q1,_)=(q2,_,>)
m.setRule("q1","","q2","",">")
m.setAccept("q2")

print(m.tape)
print("status ",m.run())
print(m.tape)