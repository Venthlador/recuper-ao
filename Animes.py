class Animes():
    __id: int
    __nome: str
    __episodios: int
    __anoLancamento: int
    __autor: str
    __genero: str
    __classificacao: str


    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    def getEpisodios(self):
        return self.__episodios

    def setEpisodios(self, episodios):
        self.__episodios = episodios

    def getAnoLancamento(self):
        return self.__anoLancamento

    def setAnoLancamento(self, anoLancamento):
        self.__anoLancamento = anoLancamento

    def getAutor(self):
        return self.__autor

    def setAutor(self, autor):
        self.__autor = autor

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.__genero = genero

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getClassificacao(self):
        return self.__classificacao

    def setClassificacao(self, classificacao):
        self.__classificacao = classificacao

    def toDict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'episodios': self.__episodios,
            'anoLancamento': self.__anoLancamento,
            'autor': self.__autor,
            'genero': self.__genero,
            'classificacao': self.__classificacao
        }
