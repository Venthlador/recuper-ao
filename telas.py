import os
from Animes import Animes


def cadastrarAnime() -> Animes:
    limparTela()
    print("-------- Cadastro de anime --------")
    anime = Animes()
    anime.setNome(input('Nome: '))
    anime.setEpisodios(int(input('Episodios: ')))
    anime.setAnoLancamento(int(input('Ano de Lancamento: ')))
    anime.setAutor(input('Autor: '))
    anime.setGenero(input('Genero: '))
    anime.setClassificacao(input('Classificacao: '))

    return anime

def editarAnime() -> Animes:
    limparTela()
    anime = Animes()
    anime.setId(int(input('ID: ')))
    anime.setNome(input('Nome: '))
    anime.setEpisodios(int(input('Episodios: ')))
    anime.setAnoLancamento(int(input('Ano de Lancamento: ')))
    anime.setAutor(input('Autor: '))
    anime.setGenero(input('Genero: '))
    anime.setClassificacao(input('Classificacao: '))

    return anime


def excluirAnime():
    print("-------- Exclusão de Animes --------")
    limparTela()
    id = int(input('Id: '))
    return id


def selecionarAnime():
    limparTela()
    print("-------- Seleção de Animes por ID --------")
    id = int(input('Id: '))
    return id


def exibirAnime(anime: Animes):
    print("-------- Animes --------")
    print(f"Id: {anime.getId()}")
    print(f"Nome: {anime.getNome()}")
    print(f"Episodios: {anime.getEpisodios()}")
    print(f"Ano de Lançamento: {anime.getAnoLancamento()}")
    print(f"Id: {anime.getAutor()}")
    print(f"Genero: {anime.getGenero()}")
    print(f"Classificacao: {anime.getClassificacao()}")    

def exibirAnimes(animes):
    limparTela()
    print("---------------- Animes ----------------")
    for anime in animes:
        exibirAnime(anime)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()