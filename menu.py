from telas import *
from persistencia import *


def menu():
    limparTela()
    print("-------- Sistema de Cadastro --------")
    print("1 - Cadastrar Anime")
    print("2 - Editar Anime")
    print("3 - Excluir Anime")
    print("4 - Selecionar Anime")
    print("5 - Listar Animes")
    print("6 - Sair")
    print("-------------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

persistencia = Persistencia()

while True:
    opcao = menu()

    if opcao == 1:
        anime = cadastrarAnime()
        persistencia.criar(anime)
        exibirMsg("Anime cadastrado com sucesso!")
    elif opcao == 2:
        anime = editarAnime()
        persistencia.editar(anime)
        exibirMsg("Anime editado com sucesso!")
    elif opcao == 3:
        limparTela()
        id = excluirAnime()
        persistencia.excluir(id)
        exibirMsg("Anime excluído com sucesso!")
    elif opcao == 4:
        id = selecionarAnime()
        anime = persistencia.selecionar(id)
        if anime == None:
            exibirMsg("Anime não encontrado!")
        else:
            exibirAnime(anime)
            travarTela()
    elif opcao == 5:
        animes = persistencia.selecionar_todos()
        exibirAnimes(animes)
    elif opcao == 6:
        break
