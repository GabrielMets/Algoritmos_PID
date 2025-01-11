# Programa responsavel por realizar dilatacao da imagem 02.jpg
# Autores: Gabriel Tadioto e Gabriel Santos da Silva

import cv2
import copy

def sum_matriz(matriz):
    sum = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            sum += matriz[i][j]

    return sum

def dilatacao(imagem, elemento_estruturante):
    #pegar as caracteristicas da imagem binaria e da matriz elemento estruturante  
    altura = len(imagem)
    largura = len(imagem[0])

    altura_e = len(elemento_estruturante)
    largura_e = len(elemento_estruturante[0])
    
    #// 2 : divide por 2 e arredonda para baixo. Descobre o centro.
    meio_altura, meio_largura = altura_e // 2, largura_e // 2

    imagem_saida = copy.copy(imagem) # utilizei copy, pois se fosse atribuido apenas com "=", ele funciona como ponteiro alterando as 2 imagens

    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            imagem_saida[i][j] = 0

    for i in range(meio_altura, altura - meio_altura): #percorrerá todas as linhas da imagem, exceto as bordas, onde o elemento estruturante não caberia completamente
        for j in range(meio_largura, largura - meio_largura): #percorrerá todas as colunas da imagem, exceto as bordas, onde o elemento estruturante não caberia completamente

            #o roi é uma matriz que extrai um pedaço da imagem com o mesmo tamanho do elemento estruturante
            roi = imagem[i - meio_altura:i + meio_altura + 1, j - meio_largura:j + meio_largura + 1]
            
            if sum_matriz(roi):
                imagem_saida[i, j] = 255 #pinta de branco
            else:
                imagem_saida[i, j] = 0 #pinta de preto

    return imagem_saida

def main():
    #imagem em escala de cinza
    imagem = cv2.imread("../Imagens/01.jpg", cv2.IMREAD_GRAYSCALE)

    #imagem binária
    _, imagem_binaria = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)
    
    elemento_estruturante = [[1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1]]

    imagem_dilatada = dilatacao(imagem_binaria, elemento_estruturante)

    cv2.imshow("Imagem Binaria", imagem_binaria)
    cv2.imshow("Imagem Dilatada", imagem_dilatada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()