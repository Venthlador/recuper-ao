from json_storage import *
from Animes import *


class Persistencia():
    __storage = JsonStorage()

    def criar(self, dado: Animes) -> Animes:
        dados = self.selecionar_todos()
        dado.setId(self.__gerarId())
        dados.append(dado)
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def editar(self, dado: Animes) -> None:
        dados = self.selecionar_todos()
        for i, data in enumerate(dados):
            if data.getId() == dado.getId():
                dados[i] = dado
        self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def excluir(self, id: int) -> None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                dados.remove(dado)
                self.__storage.gravarJson(list(map(lambda x: x.toDict(), dados)))

    def selecionar(self, id: int) -> Animes | None:
        dados = self.selecionar_todos()
        for dado in dados:
            if dado.getId() == id:
                return dado
        return None

    def selecionar_todos(self) -> list:
        animes = []
        for i in self.__storage.lerJson():
            anime = Animes()
            anime.setId(i['id'])
            anime.setNome(i['nome'])
            anime.setEpisodios(i['episodios'])
            anime.setAnoLancamento(i['anoLancamento'])
            anime.setAutor(i['autor'])
            anime.setGenero(i['genero'])
            anime.setClassificacao(i['classificacao'])
            animes.append(anime)
        return animes

    def __gerarId(self) -> int:
        dados = self.selecionar_todos()
        if len(dados) == 0:
            return 1
        return dados[-1].getId() + 1
