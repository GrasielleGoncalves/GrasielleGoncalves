import sqlite3


def criar_tabela(cursor, conn):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()

def main():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    
    criar_tabela(cursor, conn)

    while True:
    
        print("Escolha uma opção:")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
           
            nome = input("Digite o Nome: ")
            quantidade = input("Digite a Quantidade: ")
            preco = input("Digite o Preço: ")

            cursor.execute('''
                INSERT INTO produtos (nome, quantidade, preco)
                VALUES (?, ?, ?)
            ''', (nome, quantidade, preco))

            conn.commit()
            print(f"Produto '{nome}' adicionado com sucesso!")

        elif opcao == '2':
            
            cursor.execute('SELECT * FROM produtos')
            produtos = cursor.fetchall()
            print("Produtos em estoque:")
            for produto in produtos:
                print(produto)

        elif opcao == '3':
           
            id_produto = input("Digite o ID do produto para atualizar a quantidade: ")
            nova_quantidade = input("Digite a nova quantidade: ")

            cursor.execute('''
                UPDATE produtos SET quantidade = ? WHERE id = ?
            ''', (nova_quantidade, id_produto))

            conn.commit()
            print("Produto atualizado com sucesso!")

        elif opcao == '4':
            
            id_produto = input("Digite o ID do produto para deletar: ")

            cursor.execute('DELETE FROM produtos WHERE id = ?', (id_produto,))
            conn.commit()
            print(f"Produto com ID {id_produto} deletado com sucesso!")

        elif opcao == '5':
            
            busca = input("Digite o ID ou nome do produto para buscar: ")

            cursor.execute('''
                SELECT * FROM produtos WHERE id = ? OR nome LIKE ?
            ''', (busca, f"%{busca}%"))
            produtos = cursor.fetchall()

            if produtos:
                print("Produto(s) encontrado(s):")
                for produto in produtos:
                    print(produto)
            else:
                print("Produto não encontrado.")

        elif opcao == '6':
           
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

  
    conn.close()


if __name__ == "__main__":
    main()