def criar_cabecalho(titulo:str,temSinal = False,tamanhoLinha = 55):
    if temSinal == True:
        print("-=-"*18)
        print(titulo.center(60))
        print("-=-"*18)
    else:
        print("-"*tamanhoLinha)
        print(titulo.center(tamanhoLinha))
        print("-"*tamanhoLinha)


def criar_menu(lista,titulo:str,tamanhoLinha = 55):
    print("-"*tamanhoLinha)
    print(titulo.center(tamanhoLinha))
    print("-"*tamanhoLinha)
    for i,c in enumerate(lista):
        print("\033[1;33m[{}]\033[m {}".format(i+1,c))
    print("-"*tamanhoLinha)


def cadastrar_usuario(lista,nome:str,email:str):
    jaTem = False
    for i,c in enumerate(lista):
        if c["email"] == email:
            jaTem = False
        elif i == len(lista) - 1:
            jaTem = True
    if jaTem == False:
        dadosAlunos = {"nome":nome,"email":email}
        lista.append(dadosAlunos.copy())
        dadosAlunos.clear()
        print("\033[1;32mUsuário {} cadastrado(a) com sucesso!\033[m".format(nome))
    else:
        print("\033[1;31mEsse endereço de email já existe! Erro ao cadastrar usuário!\033[m")
    
    
def exibir_usuarios_cadastrados(lista):
    for i,c in enumerate(lista):
        print("{} --> {}".format(i+1,c["nome"].title()))


def exibir_usuarios_cadastrados_ordem_alfabetica(lista):
    listaAux = list()
    for i in lista:
        listaAux.append(i["nome"].title())
    listaAux.sort()
    for i,c in enumerate(listaAux):
        print("{} --> {}".format(i+1,c))


def verificar_usuario_nome(lista,nome:str):
    for i,c in enumerate(lista):
        if c["nome"] == nome:
            return True
            break
        elif i == len(lista) - 1:
            return False
        
        
def verificar_usuario_email(lista,email:str):
    for i,c in enumerate(lista):
        if c["email"] == email:
            return True
            break
        elif i == len(lista) - 1:
            return False
        

def remover_aluno(lista,email:str):
    for i,c in enumerate(lista):
        if c["email"] == email:
            confirmacao = str(input("\033[1;33mTem certeza de que deseja excluir o usuário {} da lista? [S/N] : \033[m".format(c["nome"]))).upper().strip()
            if confirmacao == "S" or confirmacao == "SIM" or confirmacao == "SI":
                lista.pop(i)
                print("\033[1;32mUsuário {} removido(a) da lista com sucesso!\033[m".format(c["nome"]))
            else:
                print("\033[1;32mPedido de exclusão cancelado com sucesso!\033[m")
                

def alterar_nome_usuario(lista,email:str,novoNome:str):
    cont = 0
    for i,c in enumerate(lista):
        if c["email"] == email:
            print("\033[1;32mAlteração de {} para {} foi um sucesso!\033[m".format(c["nome"],novoNome))
            c["nome"] = novoNome
            break
