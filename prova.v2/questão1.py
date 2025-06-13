def salvar_livro(livro):
    try:
        with open("livro.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{livro['nome']};{livro['nome_livro']};{livro['autor']};{livro['numero']};{livro['isbn']}\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar livro: {e}")
        return False


def buscar_livro_por_titulo(titulo):
    try:
        with open("livro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(";")
                if dados[1].lower() == titulo.lower():
                    return {
                        "nome": dados[0],
                        "nome_livro": dados[1],
                        "autor": dados[2],
                        "numero": dados[3],
                        "isbn": dados[4]
                    }
        return None
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao buscar livro: {e}")
        return None