from machine import Machine

m = Machine()
m.setTape(["a","a","a","b","b","b",""])

# (q0,a)=(q1,_,>)
m.setRule("q0","a","q1","",">")
# (q1,a)=(q1,a,>)
m.setRule("q1","a","q1","a",">")
# (q1,b)=(q2,b,>)
m.setRule("q1","b","q2","b",">")
# (q2,b)=(q2,b,>)
m.setRule("q2","b","q2","b",">")
# (q2,_)=(q3,_,<)
m.setRule("q2","","q3","","<")
# (q3,b)=(q4,_,<)
m.setRule("q3","b","q4","","<")
# (q4,b)=(q5,b,<)
m.setRule("q4","b","q5","b","<")
# (q5,a)=(q5,a,<)
m.setRule("q5","a","q5","a","<")
# (q5,b)=(q5,b,<)
m.setRule("q5","b","q5","b","<")
# (q5,_)=(q0,_,>)
m.setRule("q5","","q0","",">")
# (q4,_)=(q6,_,>)
m.setRule("q4","","q6","",">")

m.setAccept("q6")

print(m.tape)
print(m.run())
print(m.tape)