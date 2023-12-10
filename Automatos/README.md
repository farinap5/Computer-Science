# Conversor AFNe e AFN para AFD


Programa em python para conversão e teste de AFN/AFNe

### AFN

$$
(A, a)\to B
$$
$$
(A, a)\to C
$$
$$
(B, b)\to D
$$
$$
(C, c)\to D
$$
$$
(D, a)\to D
$$
$$
(D, c)\to C
$$

Grafo de transições
```mermaid
flowchart LR
	A-->|a|B
	A-->|a|C
	B-->|b|D
	C-->|c|D
	D-->|a|D
	D-->|c|C
```

Serão agregados todos os estados que consigo chegar a partir de um estado $X$ lendo $y$ qualquer, e então criado um novo estado.

Após a conversão da AFN para AFD.
```mermaid
flowchart LR
	A-->|a|BC
	BC-->|b|D
	BC-->|c|D
	D-->|a|D
	D-->|c|C
	C-->|c|D
```
Onde $D$ é um estado final.

---
### AFN-e

Transições:

$$
(A, a)\to A
$$
$$
(A, b)\to A
$$
$$
(A, b)\to B
$$
$$
(B, ê)\to C
$$
$$
(C, b)\to D
$$
$$
(D, a)\to D
$$
$$
(D, ê)\to C
$$
Grafo De Transições
```mermaid
flowchart LR
	A-->|a|A
	A-->|b|A
	A-->|b|B
	B-->|ê|C
	C-->|b|D
	D-->|a|D
	D-->|ê|C
```

Exemplo de conversão.
```mermaid
flowchart LR
	D-->|ê|D1
	D-->|ê|C
	D1-->|a|D2
	D2-->|ê|D3
	D2-->|ê|C2
```
Então, pode-se dizer que $D \to DC$.

Tabela de transições

| #   | A   | ABC  | ABCD | ADC  |
| --- | --- | ---- | ---- | ---- |
| a   | A   | A    | ADC  | ADC  |
| b   | ABC | ABCD | ABCD | ABCD | 

Grafo Final
```mermaid
flowchart LR
	A-->|a|A
	A-->|b|ABC
	ABC-->|a|A
	ABC-->|b|ABCD
	ABCD-->|a|ADC
	ADC-->|a|ADC
	ADC-->|b|ABCD
```
Onde $D$ é um estado final.