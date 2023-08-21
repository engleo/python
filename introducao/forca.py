import random



def jogar():
    mensagem_inicial()


    

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    indice_palavras = random.randrange(0,len(palavras))
    palavra_secreta = palavras[indice_palavras].upper()
    tamanho_palavra = len(palavra_secreta)
    palavra_chute = ["_" for letra in palavra_secreta]
    palavra_secreta_lista = []
    enforcou = False
    acertou = False
    tentativas = 1
    print("A palavra secreta tem {} letras e vc tem direito a {} erros.".format(tamanho_palavra, tamanho_palavra))

    i = 0
    for letra in palavra_secreta:
        palavra_secreta_lista.insert(i,letra.upper())
        i = i + 1
    erro = 0
    while (not acertou and not enforcou):
        print("\n\n{}ª tentativa!".format(tentativas))
        chute = input("Qual letra? ")
        chute = chute.strip()

        errou = True
        
        letra_encontrada(palavra_chute, palavra_secreta, chute)

                
        if (errou == True):
            erro = erro + 1
            print("{}º erro, não encontrei a letra {}!".format(erro, chute.upper()))    
            
        print("\n",palavra_chute)
        
        if erro == tamanho_palavra:
            print("Vc teve {} erros e não acertou a palavra secreta.".format(erro))
            break
             
        if palavra_chute == palavra_secreta_lista:
            acertou = True
            print("PARABÉNS!\nVocê acertou a palavra secreta {} em {} tentativas.".format(palavra_secreta.upper(), tentativas))
            break
        tentativas = tentativas + 1    


def mensagem_inicial():
        print("*********************************")
        print("Bem vindo ao jogo de Forca!")
        print("*********************************")

def letra_encontrada(palavra_chute, palavra_secreta, chute):
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra.upper(), index))
                palavra_chute[index] = letra.upper()
                errou = False
                return errou, palavra_chute
            index = index + 1

if(__name__ == "__main__"):
    jogar()    