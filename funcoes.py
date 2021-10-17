def criar_cabecalho(titulo:str,temSinal = False,tamanhoLinha = 55):
    if temSinal == True:
        print("-=-"18)
        print(titulo.center(60))
        print("-=-"18)
    else:
        print("-"tamanhoLinha)
        print(titulo.center(tamanhoLinha))
        print("-"tamanhoLinha)


def criar_menu(lista,titulo:str,tamanhoLinha = 55):
    print("-"tamanhoLinha)
    print(titulo.center(tamanhoLinha))
    print("-"tamanhoLinha)
    for i,c in enumerate(lista):
        print("\033[1;33m[{}]\033[m {}".format(i+1,c))
    print("-"*tamanhoLinha)


def cadastrar_usuario(lista,nome:str,email:str):
    dadosAlunos = {"nome":nome,"email":email}
    lista.append(dadosAlunos.copy())
    dadosAlunos.clear()
    print("\033[1;32mUsuário {} cadastrado(a) com sucesso!\033[m".format(nome))
