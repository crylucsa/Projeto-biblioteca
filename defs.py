import os
import time
from classes import Livro
dicionario={
    1 : Livro ( titulo = "Duna", autor = "Frank Herbert", genero = "Ficção Cientifica"),
    2 : Livro ( titulo = "Neuromancer", autor = "William Gibson", genero = "Ficção Cientifica"),
    3 : Livro ( titulo = "Fundação", autor = "Isaac Asimov", genero = "Ficção Cientifica"),
    4 : Livro ( titulo = "Snow Crash", autor = "Neal Stephenson", genero = "Ficção Cientifica"),
    5 : Livro ( titulo = "Admiravel Mundo Novo", autor = "Aldous Huxley", genero = "Ficção Cientifica"),
    6 : Livro ( titulo = "A máquina do tempo", autor = "H. G. Wells", genero = "Ficção Cientifica"),
    7 : Livro ( titulo = "O Senhor dos Anéis: A Sociedade do Anel", autor = "J. R. R. Tolkien", genero = "Fantasia"),
    8 : Livro ( titulo = "As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa", autor = "C. S. Lewis", genero = "Fantasia"),
    9 : Livro ( titulo = "A Canção de Gelo e Fogo: A Guerra dos Tronos", autor = "George R. R. Martin", genero = "Fantasia"),
    10 : Livro ( titulo = "Mistborn: O Império Final", autor = "Brandon Sanderson", genero = "Fantasia"),
    11 : Livro ( titulo = "O Nome do Vento", autor = "Patrick Rothfuss",genero = "Fantasia"),
    12 : Livro ( titulo = "Harry Potter e a Pedra Filosofal", autor = "J. K. Rowling", genero = "Fantasia"),
    13 : Livro ( titulo = "A Roda do Tempo: O Olho do Mundo", autor = "Robert Jordan", genero = "Fantasia"),
    14 : Livro ( titulo = "Orgulho e Preconceito", autor = "Jane Austen", genero = "Romance"),
    15 : Livro ( titulo = "Anna Kariênina", autor = "Liev Tolstói", genero = "Romance"),
    16 : Livro ( titulo = "Dom Casmurro", autor = "Machado de Assis", genero = "Romance"),
    17 : Livro ( titulo = "O Morro dos Ventos Uivantes", autor = "Emily Brontë", genero = "Romance"),
    18 : Livro ( titulo = "Cem Anos de Solidão", autor = "Gabriel García Márquez", genero = "Romance"),
    19 : Livro ( titulo = "E o Vento Levou", autor = "Margaret Mitchell", genero = "Romance"),
    20 : Livro ( titulo = "O Silêncio dos Inocentes", autor = "Thomas Harris", genero = "Suspense"),
    21 : Livro ( titulo = "Assassinato no Expresso do Oriente", autor = "Agatha Christie", genero = "Suspense"),
    22 : Livro ( titulo = "O Colecionador de Ossos", autor = "Jeffery Deaver", genero = "Suspense"),
    23 : Livro ( titulo = "Garota Exemplar", autor = "Gillian Flynn", genero = "Suspense"),
    24 : Livro ( titulo = "O Iluminado", autor = "Stephen King", genero = "Suspense"),
    25 : Livro ( titulo = "Dragão Vermelho", autor = "Thomas Harris", genero = "Suspense"),
}
#-------------------------------------------------
def adicionar_livro():
    print("Para adicionar um livro, preencha as seguintes informações:")
    titulo=input("Nome do livro -->").capitalize()
    autor=input("Autor -->").capitalize()
    genero=input("Genero -->").capitalize()
    novo_id = max(dicionario.keys()) + 1 #pega o ultimo id e adiciona 1 para o novo livro
    novo_livro=Livro(titulo, autor, genero) #adiciona uma variavel chamada novo_livro
    dicionario[novo_id]= novo_livro #adiciona dentro do novo id, as informaçoes perticentes a variavel novo_livro.
    print(f"Novo livro adicionado com sucesso! Está localizado na Id {novo_id}")
    time.sleep(2)
    os.system("cls")
#-------------------------------------------------
def remover_livro():
    print("Remover livro")
    remover_id=int(input("Digite o id:")) #solicita o id
    del dicionario[remover_id] #apaga as informaçoes do dicionario no local do id solicitado.
    os.system("cls")
    print(f"Livro {remover_id} removido com sucesso! ")
    os.system("pause")
#-------------------------------------------------
def emprestar_livro():
    id_livro = int(input("Digite o ID do livro que deseja emprestar: ")) #solicita o id do livro
    
    if id_livro in dicionario: #verifica se o id do livro esta no dicionario
        livro = dicionario[id_livro] #adiciona as informaçoes do id do dicionario a variavel livro
        if not livro.getEmprestado(): # Primeiro verifica o status de emprestimo usando getEmprestado
            livro.setEmprestado(True) # Modifica o status de emprestimo.
            print(f'Livro "{livro.getTitulo()}" emprestado com sucesso!')
        else:
            print(f'O livro "{livro.getTitulo()}" já está emprestado.') #Se o setEmprestado ja estiver True vai dar essa mensagem.
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def devolver_livro():
    id_livro = int(input("Digite o ID do livro que deseja devolver: ")) #solicita o id
    
    if id_livro in dicionario: #verifica se o id do livro esta no dicionario   SE ESTIVER
        livro = dicionario[id_livro] # acessa o dicionario usando a id solicitada
        if livro.getEmprestado(): #Verifica o Status de emprestimo usando getEmprestado
            livro.setEmprestado(False) #Modifica o status de emprestimo usando SetEmprestado(False)
            print(f'Livro "{livro.getTitulo()}" devolvido com sucesso!')
        else:
            print(f'O livro "{livro.getTitulo()}" não estava emprestado.')
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def listar_autor():
    autor_busca = input("Digite o nome do autor que deseja buscar: ").strip() #solicita o nome do autor

    encontrados = False #Essa variavel inicialmente começa como falsa como uma flag
    for id_livro, livro in dicionario.items(): #percorre o dicionario
        # Compara ignorando maiúsculas/minúsculas
        if livro.getAutor().lower() == autor_busca.lower(): #compara o nome do autor de cada livro com o nome que o usuario digitou
            print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Gênero: {livro.getGenero()}")
            encontrados = True #Se o nome do autor for encontrado, a variavel se torna true

    if not encontrados: #Se nao for encontrado o autor solicitado
        print(f"Não foram encontrados livros do autor {autor_busca}.")

    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def listar_genero():
    while True:
        escolha_genero = int(input(
            "Selecione o gênero que você deseja listar os livros:\n"
            "0 --> Sair\n"
            "1 --> Ficção Científica\n"
            "2 --> Fantasia\n"
            "3 --> Romance\n"
            "4 --> Suspense\n--> "
        )) #solicita um numero ao dicionario que será utilizado como id

        if escolha_genero == 0:
            break #sai do while true e da funçao, e retorna ao menu main

        mapa_genero = { #É criado um dicionario para mapear a escolha para o nome do gênero
            1: "Ficção Cientifica", #liga os numeros que o usuario digita 1,2,3,4
            2: "Fantasia", #aos nomes completos dos generos
            3: "Romance", #   <--
            4: "Suspense"
        }

        genero_selecionado = mapa_genero.get(escolha_genero) #tenta achar a chave, o numero selecionado pelo usuario no dicionario que acabamos de criar
        #se o usuario tiver digitado por exemplo 1, o metodo get retorna o genero 1 "Ficção Cientifica"
        if not genero_selecionado: #validação para caso o usuario digite um numero menor q 1 ou maior q 4
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")
            os.system("pause")
            os.system("cls")
            continue

        # Listando livros do gênero escolhido
        encontrados = False #Nossa variavel está como falsa inicialmente
        for id_livro, livro in dicionario.items(): #percorre o dicionario
            if livro.getGenero() == genero_selecionado: #Verifica todos os generos de todos os livros para ver se tem algum com o genero selecionado
                print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Autor: {livro.getAutor()}")
                #printamos as informaçoes e 
                #caso tenha algum com o genero selecionado mudamos a variavel pra true
                encontrados = True 
        if not encontrados: #se nao tiver nenhum livro com esse genero
            print(f"Não há livros cadastrados no gênero {genero_selecionado}.")

        os.system("pause")
        os.system("cls")


#-------------------------------------------------
def listar_todos(): 
    for id_livro, livro in dicionario.items(): #percorremos o dicionario 
        print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Autor: {livro.getAutor()} | Gênero: {livro.getGenero()}")
    os.system("pause")
#-------------------------------------------------
def listar_emprestado():
    encontrados = False #variavel começa como falsa até achar um livro
    for id_livro, livro in dicionario.items(): #percorremos o dicionario
        if livro.getEmprestado(): #Verifica se o metodo getEmprestado retorna True
            print(f"ID: {id_livro} | Título: {livro.getTitulo()} | Autor: {livro.getAutor()}")
            encontrados = True #se tiver algum livro emprestado vai mudar a variavel para true
    if not encontrados: #se nao tiver nada emprestado
        #vai printar e a variavel encotrados continua false
        print("Nenhum livro está emprestado.")
    
    os.system("pause")
    os.system("cls")

#-------------------------------------------------
def editar_livro():
    id_livroeditado = int(input("Digite a ID do livro que deseja editar: ")) #solicita a id

    if id_livroeditado in dicionario: #ve se a id solicitada esta no dicionario
        livro = dicionario[id_livroeditado] # acessa o dicionario usando a id solicitada

        print(f"\nLivro atual: {livro.getTitulo()} | {livro.getAutor()} | {livro.getGenero()}")
            #printa as informaçoes atuais do livro
        novo_titulo = input("Novo título (pressione Enter para manter): ")
        novo_autor = input("Novo autor (pressione Enter para manter): ")
        novo_genero = input("Novo gênero (pressione Enter para manter): ")
            #solicita as informaçoes novas do livro
        if novo_titulo.strip(): #strip retira os espaços em branco
            livro.setTitulo(novo_titulo)
            #chama o metodo setTitulo no objeto livro, que faz parte da classe Livro
            #é responsavel por atualizar o titulo do livro
        if novo_autor.strip():
            livro.setAutor(novo_autor)
        if novo_genero.strip():
            livro.setGenero(novo_genero)


        print("\nLivro atualizado com sucesso!")
        print(f"Novo cadastro: {livro.getTitulo()} | {livro.getAutor()} | {livro.getGenero()}")
        #imprime as novas informaçoes do livro.
    else:
        print("ID não encontrado!")
        #caso o id nao exista
    os.system("pause")
    os.system("cls")

#-------------------------------------------------