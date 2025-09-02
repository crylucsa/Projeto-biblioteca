# A classe 'Livro' serve como um molde (ou 'blueprint') para criar objetos que representam livros.
# Cada objeto 'Livro' terá suas próprias informações, como título, autor e gênero.
class Livro:
    # O método '__init__' é o construtor da classe. Ele é chamado automaticamente
    # toda vez que um novo objeto 'Livro' é criado.
    # 'self' se refere à própria instância do objeto que está sendo criada.
    # '__titulo', '__autor', '__genero' são os atributos do objeto. O uso de dois
    # underscores no início (__) indica que esses atributos são "privados", ou seja,
    # não devem ser acessados diretamente de fora da classe.
    def __init__(self, titulo, autor, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        # O atributo '__emprestado' é inicializado como 'False' por padrão.
        # Isso significa que, ao ser criado, um livro já é considerado disponível.
        self.__emprestado = False

    # O método mágico '__repr__' (representação) é usado para criar uma string
    # que representa o objeto. É muito útil para depuração, pois, quando você
    # imprime o objeto, ele mostra uma representação legível e informativa.
    def __repr__(self):
        # Retorna uma string formatada que se parece com a forma como o objeto foi criado.
        return f'Livro("{self.titulo}", "{self.autor}", "{self.genero}")'

    # --- Métodos 'getter' para acessar os atributos ---
    # Os métodos 'get' são usados para obter (ler) os valores dos atributos privados.
    # Eles fornecem uma maneira controlada de acessar os dados, em vez de acessar
    # os atributos diretamente.

    def getTitulo(self):
        return self.__titulo
    #-------------------------
    def getAutor(self):
        return self.__autor
    #-------------------------
    def getGenero(self):
        return self.__genero
    #-------------------------
    def getEmprestado(self):
        return self.__emprestado

    # --- Métodos 'setter' para modificar os atributos ---
    # Os métodos 'set' são usados para definir (mudar) os valores dos atributos privados.
    # Eles também garantem que a modificação dos dados seja feita de forma controlada.
    # Note que eles retornam o novo valor, o que pode ser útil em alguns casos,
    # mas a principal função é a atribuição.
    def setTitulo(self, titulo):
        self.__titulo = titulo
        return self.__titulo
    #------------------------
    def setAutor(self, autor):
        self.__autor = autor
        return self.__autor
    #-----------------------
    def setGenero(self, genero):
        self.__genero = genero
        return self.__genero
    #-----------------------
    def setEmprestado(self, status):
        # Este método atualiza o status de empréstimo do livro.
        # O valor do parâmetro 'status' (True ou False) é atribuído ao atributo '__emprestado'.
        self.__emprestado = status