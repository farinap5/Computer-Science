from copy import deepcopy

class Automato:
    def __init__(self) -> None:
        self.Q = {} # Transaction list
        self.qInit = None # initial state
        self.F = None # final state
        self.T = []
        self.P = []
        self.A = None # simbles/alphabet
        self.ptr = 0 # pointer
        self.qList = None # list of states

    def Read(self, Name:str="input.txt") -> None:
        lines = open(Name,"r").readlines()
        for i in lines:
            if i[0] == "#":
                pass
            elif i[0] == "A":
                a = i[1:]
                a = a.replace(" ","")
                a = a.replace("\n","")
                self.A = a
            elif i[0] == "Q":
                q = i[1:]
                q = q.replace(" ","")
                q = q.replace("\n","")
                self.qList = q
            elif i[0] == "F":
                f = i[1:]
                f = f.replace(" ","")
                f = f.replace("\n","")
                self.F = f
            elif i[0] == "q":
                e = i[1:]
                e = e.replace(" ","")
                e = e.replace("\n","")
                self.qInit = e
            elif i[0] == "T":
                t = i[1:]
                t = t.replace(" ","")
                t = t.replace("\n","")
                self.T.append((t[0],t[1],t[2]))
            elif i[0] == "P":
                p = i[1:]
                p = p.replace(" ","")
                p = p.replace("\n","")
                self.P.append(p)

    def Add(self, fq:tuple, tq:str)->int:
        if not fq[0] in self.qList:
            return 1
        if not fq[1] in self.A and not fq[1] == "ê":
            return 2
        if not tq in self.qList:
            return 3
        
        v = (fq[0],)
        try:
            self.Q[(v,fq[1])] = self.Q[(v,fq[1])] + (tq,)
        except KeyError:
            self.Q[(v,fq[1])] = ()
            self.Q[(v,fq[1])] = self.Q[(v,fq[1])] + (tq,)
        return 0
    
    def ConvertAFNe(self):
        """
        Função para converter uma tabela de transições a partir de um
        Automato Finito Não Deterministico que possui transições vazias.
        """
        TN = {}
        for i in self.qList:
            for j in self.A:
                #print(j)
                # validar todas as transições vazias a partir de i
                # cria uma lista de estados y de x-e->y
                t1 = []
                t1 = [value for key, value in self.Q.items() if key[0] == (i,) and key[1] == "ê"]
                t1.append((i,))
                

                t2 = []
                for t in t1:
                    # para cada estado em t1, validar o proximo estado para determinado símbolo.
                    # isso deve ser testado para todos os simbolos.
                    # Um lista é retornada, com os estados vinais para cada relação de estado
                    # inicial e sombolo.
                    aux = [value for key, value in self.Q.items() if key[0] == t and key[1] == j]
                    for v in aux:
                        for k in v:
                            t2.append((k,))
                t3 = ()
                for t in t2:
                    # A partir do estado alcançado, deve-se ver para onde podemos ir apenas
                    # usando transições vazias.
                    auv = ()
                    aux = [value for key, value in self.Q.items() if key[0] == t and key[1] == "ê"]
                    for x in aux:
                        auv = auv + x
                    auv = auv + t
                    t3 = t3 + auv
                t3 = tuple(sorted(set(t3)))
                TN[((i,),j)] = t3

        auxK = []
        for i in TN:
            if TN[i] == ():
                auxK.append(i)
        for i in auxK:
            TN.pop(i)
        
        for i in range(10):
            TN = self.ParseAFNe(TN)
        return TN
    
    def ParseAFNe(self,TN):
        auxDict = deepcopy(TN)
        for k in TN:
            for v in TN[k]:
                for s in self.A:
                    aux = [value for key, value in TN.items() if key[0] == (v,) and key[1] == s]
                    #print(TN[k],k[1],aux)
                    for p in aux:
                        try:
                            auxDict[(TN[k], s)] = tuple(sorted(set(auxDict[(TN[k], s)] + p)))
                        except KeyError:
                            auxDict[(TN[k], s)] = ()
                            auxDict[(TN[k], s)] = tuple(sorted(set(auxDict[(TN[k], s)] + p)))
        return auxDict

    def ConvertAFN_AFD(self):
        """
        Função para converter uma tabela de transições a partir de um
        Automato Finito Não Deterministico.
        """
        ta = []
        for k in self.Q:
            if len(self.Q[k]) > 1:
                for i in self.Q[k]:
                    # Serão agregados todos os estados que consigo chegar a partir 
                    # de um estado $X$ lendo $y$ qualquer, e então criado um novo estado.
                    try:
                        value = [value for key, value in self.Q.items() if key[0] == (i,)][0]
                        read = [key[1] for key, value in self.Q.items() if key[0] == (i,)][0]
                        ta.append((self.Q[k], read, tuple(value)))
                    except IndexError:
                        pass

        for i in ta:
            # Atualizar o dicionario de transições
            try:
                self.Q[(tuple(i[0]),i[1])] = self.Q[(tuple(i[0]),i[1])] + i[2]
            except KeyError:
                self.Q[(tuple(i[0]),i[1])] = ()
                self.Q[(tuple(i[0]),i[1])] = self.Q[(tuple(i[0]),i[1])] + i[2]
        return 1 
    
    def CompileAFN(self):
        """
        Função para compilar uma tabela de transições a partir de um
        Automato Finito Não Deterministico.

        A fução CompileAFN() atualizará a matriz de transições Q pela função
        ConvertAFN_AFD(). Após seu uso, 
        a linguagem pode ser usada para verificar as palavras.
        """
        tc = 1
        for i in self.T:
            t = (i[0], i[1])
            r = self.Add(t, i[2])
            if r == 1:
                print(f"Error transaction {tc}: Base state {i[0]} not defined.")
            elif r == 2:
                print(f"Error transaction {tc}: Simble {i[1]} not defined!")
            elif r == 3:
                print(f"Error transaction {tc}: Transacted state {i[2]} not defined!")
            tc+=1

        self.ConvertAFN_AFD()
        

    def CompileAFNe(self):
        """
        Função para compilar uma tabela de transições a partir de um
        Automato Finito Não Deterministico que possui transições vazias.

        A fução CompileAFNe() atualizará a matriz de transições Q. Após seu
        uso, a linguagem pode ser usada para verificar as palavras.
        """
        tc = 1
        for i in self.T:
            t = (i[0], i[1])
            r = self.Add(t, i[2])
            if r == 1:
                print(f"Error transaction {tc}: Base state {i[0]} not defined.")
            elif r == 2:
                print(f"Error transaction {tc}: Simble {i[1]} not defined!")
            elif r == 3:
                print(f"Error transaction {tc}: Transacted state {i[2]} not defined!")
            tc+=1

        self.Q = deepcopy(self.ConvertAFNe())

    # export formated state list
    def EexportTransactions(self) -> str:
        T = ""
        for k,v in self.Q:
            T += f"T {k} {v} {self.Q[(k,v)]}\n"
        return T

    def VerifyWord(self, w:str, ptr:int=0):
        """
        Executa o automato sob a palavra w, tendo o dicionário
        de transições como base. 
        """
        q = (self.qInit,)
        self.ptr = ptr
        c = 0
        while True:
            if c > len(w)-1:
                break
            #print(f"{self.ptr} {c} {q} {w[self.ptr]} ", end="")
            try:
                q = self.Q[(q,w[self.ptr])]
            except KeyError:
                return 1
            #print(f"{q}")
            c+=1
            self.ptr+=1
        for i in q:
            for x in self.F:
                if i == x:
                    return 0
        else:
            return 1

    def Verify(self):
        m = []
        for i in self.P:
            m.append((self.VerifyWord(i),i))
        return m
    
    def ProcessResult(self, result):
        m = ""
        for i in result:
            if i[0] == 0:
                m += f"M aceita a palavra <{i[1]}>\n"
            else:
                m += f"M rejeita a palavra <{i[1]}>\n"
        return m
    
    def WriteToFile(self, data:str, name:str="out.txt"):
        f = open(name, 'w')
        f.write(data)
        f.close()
    

if __name__ == "__main__":
    # Testando uma AFNe
    m1 = Automato()
    m1.Read("input.txt")
    m1.CompileAFNe() # Utilizar quandos se trata de um AFNe
    r = m1.Verify() # Executar lista de palavras na linguagem
    out = m1.ProcessResult(r)
    print("Resultados AFNe\n"+out)
    m1.WriteToFile(out, name="afne.txt") # Escrever resultado no arquivo
    #m.CompileAFN() # Utilizar quandos se trata de um AFN


    # Testando uma AFN
    m2 = Automato()
    m2.Read("input1.txt")
    m2.CompileAFN() # Utilizar quandos se trata de um AFN
    r = m2.Verify() # Executar lista de palavras na linguagem
    out = m2.ProcessResult(r)
    print("Resultados AFN\n"+out)
    m2.WriteToFile(out, name="afn.txt") # Escrever resultado no arquivo
    
