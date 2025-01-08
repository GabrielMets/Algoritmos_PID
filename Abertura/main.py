import cv2
import numpy as np

def dilatacao(imagem, elemento_estruturante):
    #pegar as caracteristicas da imagem binaria e da matriz elemento estruturante  
    altura, largura = imagem.shape
    altura_e, largura_e = elemento_estruturante.shape
    
    #// 2 : divide por 2 e arredonda para baixo. Descobre o centro.
    meio_altura, meio_largura = altura_e // 2, largura_e // 2

    #cria imagem de saida
    imagem_saida = np.zeros_like(imagem)
    # cont = 1
    #arosão:
    for i in range(meio_altura, altura - meio_altura): #percorrerá todas as linhas da imagem, exceto as bordas, onde o elemento estruturante não caberia completamente.
        for j in range(meio_largura, largura - meio_largura): #percorrerá todas as colunas da imagem, exceto as bordas, onde o elemento estruturante não caberia completamente.
            #cont += 1
            #o roi é uma matriz que extrai um pedaço da imagem com o mesmo tamanho do elemento estruturante. 
            roi = imagem[i - meio_altura:i + meio_altura + 1, j - meio_largura:j + meio_largura + 1]
            # print("iteração: ", cont)
            # print("roi: ", roi)
            #print()
            #verifica se a imgem cabe no tamanho do elemento_estruturante usando o "np.array_equal" que verifica se dois arrays são iguais elemento a elemento.
            if np.sum(roi):
                imagem_saida[i, j] = 255 #pinta de branco, se o pixel cabe no elemento_estruturante.
            else:
                imagem_saida[i, j] = 0 #pinta de preto, se o pixel não cabe no elemento_estruturante.

    return imagem_saida

def erosao(imagem, elemento_estruturante):
    #pegar as caracteristicas da imagem binaria e da matriz elemento estruturante  
    altura, largura = imagem.shape
    altura_e, largura_e = elemento_estruturante.shape
    
    #// 2 : divide por 2 e arredonda para baixo. Descobre o centro.
    meio_altura, meio_largura = altura_e // 2, largura_e // 2

    #cria imagem de saida
    imagem_saida = np.zeros_like(imagem)
    #cont = 1
    #arosão:
    for i in range(meio_altura, altura - meio_altura): #percorrerá todas as linhas da imagem, exceto as bordas, onde o elemento estruturante não caberia completamente.
        for j in range(meio_largura, largura - meio_largura): #percorrerá todas as colunas da imagem, exceto as bordas, onde o elemento estruturante não caberia completamente.
            #cont += 1
            #o roi é uma matriz que extrai um pedaço da imagem com o mesmo tamanho do elemento estruturante. 
            roi = imagem[i - meio_altura:i + meio_altura + 1, j - meio_largura:j + meio_largura + 1]
            #print("iteração: ", cont)
            #print("roi: ", roi)
            #print()
            #verifica se a imgem cabe no tamanho do elemento_estruturante usando o "np.array_equal" que verifica se dois arrays são iguais elemento a elemento.
            if np.array_equal(roi & elemento_estruturante, elemento_estruturante):
                imagem_saida[i, j] = 255 #pinta de branco, se o pixel cabe no elemento_estruturante.
            else:
                imagem_saida[i, j] = 0 #pinta de preto, se o pixel não cabe no elemento_estruturante.

    return imagem_saida

def abertura(img, es):
    imagem_saida = dilatacao(erosao(img, es), es)
    return imagem_saida

def main():
    #imagem original
    ori = cv2.imread("02.jpg")

    #imagem em escala de cinza
    imagem = cv2.imread("02.jpg", cv2.IMREAD_GRAYSCALE)

    #imagem binária
    _, imagem_binaria = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)
    
    elemento_estruturante = np.array([[1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1]], dtype=np.uint8)

    #chama erosao
    #imagem_erodida = erosao(imagem_binaria, elemento_estruturante_erosao)

    imagem_aberta = abertura(imagem_binaria, elemento_estruturante)

    #show janelas.
    #cv2.imshow("Imagem Original", ori)
    cv2.imshow("Imagem Binaria", imagem_binaria)
    cv2.imshow("Imagem Aberta", imagem_aberta)
    
    #esc para fechar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()