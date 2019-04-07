# Verkefni 6

### 1. Heildi og flatarmál.

    Í þessum hluta skipti ég heilduninni í nökkur skref.
    
    1. Fyrst skerfið er að endurskrifa.
    
        Þegar þú setur inn jöfnu kallast beint á "endurSkrifa()". Það fall skrifar fallið aftur svo ég gæti unnið meða það. Dæmi um keyrslu er hér fyrir neðan.
        1. Fyrst skerfið er að kalla á classan með f,g,x1,x2.
            ```python
            Heilda("-x2+5x-3", x, 3, 1)
            ```
            
        2. Í initinu kallar fallið á endurSkrifa().
            ```python
            self.f = self.endurSkrifa(f)
            self.g = self.endurSkrifa(g)
            ```
        3. Í endurSkrifan skilar hann fallinu í listum, Dæmi fyrir neðan.
            if fallið er kallað í með þessu value("-x2+5x-3"). Mynda það skila [[1,-x,2], [1,x,1], [-3]]
            
    2. Næst er að heilda.
        Þegar það er búið að heilda í init þá kallar á heilda(f) dæmi fyrir neðan.
        1. Fyrsta skrefið í heilda er í init.
            ```python
            self.F = self.heild(self.f)
            self.G = self.heild(self.g)
            ```
        2. Skerf tvö í heilda er að heilda.
            ```python
            tempf = f
            for i in range(len(tempf)):
                if (len(tempf[i]) == 1):
                    tempf[i][0] = int(tempf[i][0])
                    tempf[i].append("x")
                    tempf[i].append(1)
                elif (len(tempf[i]) == 3):
                    tempf[i][0] = int(tempf[i][0]) / ((int(tempf[i][2])) + 1)
                    tempf[i][2] = int(tempf[i][2]) + 1
            return tempf
            ```
    3. Seinast er að reikna.
        Reikna flatarmálið notar 3 föll.
        
        1. reikna()
            Reiknar fallið með x.
            ```python
            value = 0
            reikna = ""
            for i in F:
                if(i[1] == "-x"):
                    if(i[2] % 2 == 0):
                        value += i[0] * x ** i[2]
                    else:
                        value += i[0] * -(x ** i[2])
                else:
                    value += i[0] * x ** i[2]
            ```
        2. flatarmal()
            notar reiknar til ad reiknar f(x1)-f(x2)
        
        3. Reiknaflatarmal().
            Notor flatarmal til að reikna f()-g()
            
            
            
        



### 2. Memoization
    
    Í þessum hluta geri ég BETRI leiðina. frá botni til tops.
    ```pthon
    for i in range(len(input)-2, -1, -1):
        for ii in range(len(input[i])):
            if(input[i+1][ii] > input[i+1][ii+1]):
                input[i][ii] += input[i+1][ii]
            else:
                input[i][ii] += input[i+1][ii+1]
    ```


### 3. Binary Search Tree
    Eina sértaka við binary search verkefni er lastNodeRight() og lastNodeLeft().
    Það finnur seinast Nodeið annað hvort til hægri eða vinstr. Eftir hvort það þarf.
    
    Ef tala sem á að eyða er minn en head þarf delete fallið að nota right annar notar það left.
    
    ```pthon
    	def lastNodeLeft(this, last=None):
            if(this.left):
                return this.left.lastNodeLeft(this)
            else:
                last.left = None
                return this.tala

        def lastNodeRight(this, last=None):
            if(this.right):
                return this.right.lastNodeRight(this)
            else:
                print(last.right)
                last.right = None
                return this.tala
                
        def delete(this, n, upp):
            if(n == this.tala):
                if(upp):
                    this.tala = this.lastNodeLeft(this)
                else:
                    this.tala = this.lastNodeRight(this)
            elif(n > this.tala):
                if(this.right):
                    this.right.delete(n, upp)
                else:
                    return -1
            elif(n < this.tala):
                if(this.left):
                    this.left.delete(n, upp)
                else:
                    return -1
    ```
    
    Post og preorderPrint er næstum alveg eins einu munurinn er stadsetningin á print().
    
    ```pthone
    def preOrderPrint(this):
		print(this.tala)
		if(this.left):
			this.left.preOrderPrint()
		if(this.right):
			this.right.preOrderPrint()

	def postOrderPrint(this):
		if (this.left):
			this.left.postOrderPrint()
		if (this.right):
			this.right.postOrderPrint()
		print(this.tala)
    ```
### 4. Graph

    Ég notaði bara kóðan frá githubinu eins og þú sagðir fyrir grunnin. En ég bjó til mín eigin dfs & bfs. Lýsi því hér fyrir neðan.
    
    1. Dfs
        Ef þú vilt prenta með dfs. Þá kallarðu í Graph dfs fallið. Það býr til dictionary sem heldur utnam um hvaða verexa er búið að heimsækja, það er eina sem er öðruvísi.
        ```python
        def _dfs(self, vertex, visited):
            if(vertex not in visited):
                visited[vertex] = vertex
                print("Vertices",self.vertices[vertex].name)
                print(self.vertices[vertex].neighbors)
                for i in self.vertices[vertex].neighbors:
                    self._dfs(i,visited)

        def dfs(self, vertex):
            visited = {}
            self._dfs(vertex,visited)
        ``` 
    2.Bfs
        Bfs er svipað og dfs nema listin sem hann geimir. Ég nota aftur dictionary til að halda utanum þá vertexa sem ég ef heimsækjað. Q er listi sem heldur utan um hvað vertex á að skoða næst
        ```python
        def bfs(self, vertex):
            visited = {}
            q = []
            self._bfs(vertex, visited, q)

        def _bfs(self, vertex, visited, q):
            if (vertex not in visited):
                visited[vertex] = vertex
                print("Vertices", self.vertices[vertex].name)
                print(self.vertices[vertex].neighbors)
                if(len(q) > 0):
                    q.pop(0)

                for i in self.vertices[vertex].neighbors:
                    if(i not in q):
                        q.append(i)

                for i in q:
                        self._bfs(i, visited, q)
        ```