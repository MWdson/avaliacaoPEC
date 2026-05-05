# -----------------------------
# FUNÇÕES PURAS (FUNCIONAL)
# -----------------------------

def criar_livro(livros, id_livro, titulo):
    return livros + [{"id": id_livro, "titulo": titulo}]


def listar_livros(livros):
    return livros


def atualizar_livro(livros, id_livro, novo_titulo):
    return [
        {"id": l["id"], "titulo": novo_titulo} if l["id"] == id_livro else l
        for l in livros
    ]


def deletar_livro(livros, id_livro):
    return [l for l in livros if l["id"] != id_livro]


def criar_usuario(usuarios, id_usuario, nome):
    return usuarios + [{"id": id_usuario, "nome": nome}]


def listar_usuarios(usuarios):
    return usuarios


def atualizar_usuario(usuarios, id_usuario, novo_nome):
    return [
        {"id": u["id"], "nome": novo_nome} if u["id"] == id_usuario else u
        for u in usuarios
    ]


def deletar_usuario(usuarios, id_usuario):
    return [u for u in usuarios if u["id"] != id_usuario]


# -----------------------------
# PARTE IMPERATIVA (MENU)
# -----------------------------

livros = []
usuarios = []

id_livro = 1
id_usuario = 1

while True:
    print("\n1 - Criar Livro")
    print("2 - Listar Livros")
    print("3 - Atualizar Livro")
    print("4 - Deletar Livro")
    print("5 - Criar Usuário")
    print("6 - Listar Usuários")
    print("7 - Atualizar Usuário")
    print("8 - Deletar Usuário")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        titulo = input("Título: ")
        livros = criar_livro(livros, id_livro, titulo)
        id_livro += 1

    elif op == "2":
        for l in listar_livros(livros):
            print(l)

    elif op == "3":
        i = int(input("ID: "))
        t = input("Novo título: ")
        livros = atualizar_livro(livros, i, t)

    elif op == "4":
        i = int(input("ID: "))
        livros = deletar_livro(livros, i)

    elif op == "5":
        nome = input("Nome: ")
        usuarios = criar_usuario(usuarios, id_usuario, nome)
        id_usuario += 1

    elif op == "6":
        for u in listar_usuarios(usuarios):
            print(u)

    elif op == "7":
        i = int(input("ID: "))
        n = input("Novo nome: ")
        usuarios = atualizar_usuario(usuarios, i, n)

    elif op == "8":
        i = int(input("ID: "))
        usuarios = deletar_usuario(usuarios, i)

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida")
