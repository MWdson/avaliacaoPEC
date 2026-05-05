import sqlite3
from functools import partial

# =========================
# Setup do banco
# =========================
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER
)
""")
conn.commit()


# =========================
# CREATE (funcional)
# =========================

def montar_livro(titulo, autor, ano):
    return (titulo.strip(), autor.strip(), int(ano))


def inserir_livro(cursor, livro):
    cursor.execute(
        "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
        livro
    )
    return cursor.lastrowid


def create_livro(titulo, autor, ano):
    livro = montar_livro(titulo, autor, ano)
    operacao = partial(inserir_livro, cursor)
    livro_id = operacao(livro)
    conn.commit()
    return livro_id


# =========================
# READ (imperativo)
# =========================

def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        # gerado por IA
        """
        for livro in livros:
            print("ID:", livro[0])
            print("Título:", livro[1])
            print("Autor:", livro[2])
            print("Ano:", livro[3])
            print("-" * 20)
        """
        qtd_livros = len(livros)
        for x in range(0, qtd_livros):
            print("ID:", x[0])
            print("Título:", x[1])
            print("Autor:", x[2])
            print("Ano:", x[3])
            print("-" * 20)

# =========================
# UPDATE (imperativo)
# =========================

def atualizar_livro(id):
    cursor.execute("SELECT * FROM livros WHERE id = ?", (id,))
    livro = cursor.fetchone()

    if livro is None:
        print("Livro não encontrado.")
        return

    novo_titulo = input("Novo título: ")
    novo_autor = input("Novo autor: ")
    novo_ano = int(input("Novo ano: "))

    cursor.execute("""
        UPDATE livros
        SET titulo = ?, autor = ?, ano = ?
        WHERE id = ?
    """, (novo_titulo, novo_autor, novo_ano, id))

    conn.commit()
    print("Livro atualizado com sucesso!")


# =========================
# DELETE (funcional)
# =========================

def montar_id(id):
    return (int(id),)


def deletar(cursor, id_tuple):
    cursor.execute("DELETE FROM livros WHERE id = ?", id_tuple)
    return cursor.rowcount


def delete_livro(id):
    id_formatado = montar_id(id)
    operacao = lambda x: deletar(cursor, x)
    resultado = operacao(id_formatado)
    conn.commit()

    return resultado > 0


# =========================
# Menu
# =========================

def menu():
    while True:
        print("\n--- Biblioteca ---")
        print("1 - Criar livro")
        print("2 - Listar livros")
        print("3 - Atualizar livro")
        print("4 - Deletar livro")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")

            livro_id = create_livro(titulo, autor, ano)
            print(f"Livro criado com ID {livro_id}")

        elif op == "2":
            listar_livros()

        elif op == "3":
            id = int(input("ID: "))
            atualizar_livro(id)

        elif op == "4":
            id = input("ID: ")
            if delete_livro(id):
                print("Livro deletado!")
            else:
                print("Livro não encontrado.")

        elif op == "0":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
    conn.close()