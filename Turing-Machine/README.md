# Turing Machine

$$
M = (Q, Γ, b, Σ, δ, q0, F)
$$

Status:
- 0 pass
- 1 accepted
- 2 Length exceded
- 3 ptr under zero
- 4 direction error

Example code:
```python
from machine import Machine

m = Machine()
m.setTape(["a","a","a","b","b",""])

# δ(q0,a)=(q0,a,>)
m.setRule("q0","a","q0","a",">")
# δ(q0,b)=(q1,b,>)
m.setRule("q0","b","q1","b",">")
# δ(q0,_)=(q2,_,>)
m.setRule("q0","","q1","",">")
# δ(q1,b)=(q1,b,>)
m.setRule("q1","b","q1","b",">")
# δ(q1,_)=(q2,_,>)
m.setRule("q1","","q2","",">")

m.setAccept("q2")

print(m.tape)
print(m.run())
print(m.tape)
```
Output:
```
['a', 'a', 'a', 'b', 'b', '']
status  1
['a', 'a', 'a', 'b', 'b', '']
```

Machine 1: $L=\{a^{*}b^{*}\}$

Machine 2: $L=\{a^{n}b^{n}\}$

Machine 3: $L=\{a^{n}b^{n+1}\}$

Machine 4: $L=\{a^{n}b^{n}c^{n}\}$

Machine 5: $L=\{ww^{r}\}$