class Nodo:
    def __init__(self, caractere):
        self.caractere = caractere
        self.proximo = None  # Referência para o próximo nó
        self.anterior = None  # Referência para o nó anterior

# Criar e manipular a lista duplamente encadeada
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None #Primeiro elemento da lista
        self.cauda = None 

    def inserir(self, caractere):
        # Cria um novo nó com o caractere inserido
        novo_nodo = Nodo(caractere)
        if not self.cabeca: 
            self.cabeca = self.cauda = novo_nodo  # Define o novo nó como cabeça e cauda
        else:
            # Conecta o novo nó ao final da lista
            self.cauda.proximo = novo_nodo
            novo_nodo.anterior = self.cauda
            self.cauda = novo_nodo  # Atualiza a cauda para o novo nó

    def criptografar(self, deslocamento):
        atual = self.cabeca  # Começa do primeiro nó
        while atual:
            if atual.caractere.isalpha():  # Apenas letras do alfabeto são criptografadas
                base = 'A' if atual.caractere.isupper() else 'a'  # Define a base para maiúsculas ou minúsculas
                # Fórmula da cifra de César para deslocar o caractere
                atual.caractere = chr((ord(atual.caractere) - ord(base) + deslocamento) % 26 + ord(base))
            atual = atual.proximo  # Avança para o próximo nó

    def descriptografar(self, deslocamento):
        # Para descriptografar, basta aplicar a cifra com o deslocamento negativo que foi selecionado
        self.criptografar(-deslocamento)

    def exibir(self):
        mensagem = ""  # String vazia que armazenará a mensagem completa
        atual = self.cabeca  # Começa do primeiro nó
        while atual:
            mensagem += atual.caractere  # Adiciona o caractere do nó na mensagem
            atual = atual.proximo  # Avança para o próximo nó
        print(mensagem)  # Exibe a mensagem completa no console

# Função principal para interação com o usuário
def main():
    lista = ListaDuplamenteEncadeada()  # Cria uma lista duplamente encadeada sem conteúdo
    
    #Input que pede a mensagem para criptografar
    mensagem = input("Digite a mensagem para criptografar: ")
    
    for caractere in mensagem:
        lista.inserir(caractere)
    
    # Solicita o deslocamento e valida se é um número inteiro
    while True:
        try:
            deslocamento = int(input("Digite o valor do deslocamento (inteiro): "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    # Criptografa a mensagem
    lista.criptografar(deslocamento)
    print("\nMensagem criptografada:")
    lista.exibir()
    
    # Pergunta ao usuário se deseja descriptografar
    resposta = input("\nDeseja descriptografar a mensagem? (s/n): ").lower()
    if resposta == 's':
        lista.descriptografar(deslocamento)
        print("\nMensagem descriptografada:")
        lista.exibir()
    else:
        print("Encerrando o programa.")

if __name__ == "__main__":
    main()
