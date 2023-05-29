import cv2
from matplotlib import pyplot as plt
from PIL import Image

def geraMatriz(imagem, altura, largura, alter_r, alter_g, alter_b):
    matriz_booleana = [[0 for _ in range(largura)] for _ in range(altura)]  # matriz booleana
    pixeis_encontrados = 0

    for y in range(altura):
        for x in range(largura):
            (r, g, b) = imagem[y, x]
            if r == alter_r and b == alter_b and g == alter_g:
                matriz_booleana[y][x] = 1
                pixeis_encontrados += 1
            else:
                matriz_booleana.append(0)

    return matriz_booleana

def salvarMatriz(matriz_booleana, altura, largura):
    with open('images/matriz_booleana.txt', 'w') as arquivo:
        linha_str = ''
        for y in range(altura):
            for x in range(largura):
                linha_str += ' ' + (str(matriz_booleana[y][x]))
            arquivo.write(linha_str + '\n')

        print(linha_str)

def removeSelecionado(altura, largura, matriz_booleana, caminho_imagem):
    imagemRemovida = Image.fromarray(cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2RGB))

    for y in range(altura):
        for x in range(largura):
            if matriz_booleana[y][x] == 1:
                imagemRemovida.putpixel((x, y), (0, 0, 0, 0))

    plt.imshow(imagemRemovida)
    plt.show()
    imagemRemovida.save('images/ImagemRemovida.png')

def removeEntorno(altura, largura, matriz_booleana, caminho_imagem):
    imagemSelecionada = Image.fromarray(cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2RGB))

    for y in range(altura):
        for x in range(largura):
            if matriz_booleana[y][x] == 0:
                imagemSelecionada.putpixel((x, y), (0, 0, 0, 0))

    plt.imshow(imagemSelecionada)
    plt.show()
    imagemSelecionada.save('images/EntornoRemovido.png')

def alteraSelecionado(altura, largura, matriz_booleana, caminho_imagem):
    imagemAlterada = Image.fromarray(cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2RGB))
    print('Digite os valores de R, G e B que desejar colorir. Respectivamente:')
    r = int(input('R: '))
    g = int(input('G: '))
    b = int(input('B: '))

    for y in range(altura):
        for x in range(largura):
            if matriz_booleana[y][x] == 1:
                imagemAlterada.putpixel((x, y), (r, g, b))

    plt.imshow(imagemAlterada)
    plt.show()
    imagemAlterada.save('images/ImagemColorida.png')

def alteraEntorno(altura, largura, matriz_booleana, caminho_imagem):
    imagemSelecionada = Image.fromarray(cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2RGB))
    print('Digite os valores de R, G e B que desejar colorir entorno. Respectivamente:')
    r = int(input('R: '))
    g = int(input('G: '))
    b = int(input('B: '))

    for y in range(altura):
        for x in range(largura):
            if matriz_booleana[y][x] == 0:
                imagemSelecionada.putpixel((x, y), (r, g, b))

    plt.imshow(imagemSelecionada)
    plt.show()
    imagemSelecionada.save('images/EntornoColorido.png')

def main():
    print(cv2.__version__)
    caminho_imagem = ""

    print('Escolha a imagem que deseja alterar: \n'
          '1- Católica Logo \n'
          '2- Fafic Logo')
    resposta = int(input('Digite 1 ou 2: '))

    if resposta == 1:
        caminho_imagem = "images/Catolica.png"
    elif resposta == 2:
        caminho_imagem = "images/Fafic.png"

    imagem = cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2RGB)
    altura, largura, canais = imagem.shape
    plt.imshow(imagem)
    plt.show()

    print('Digite os valores de R, G e B que deseja alterar. Respectivamente: ')
    r = int(input('R: '))
    g = int(input('G: '))
    b = int(input('B: '))
    (alter_r, alter_g, alter_b) = (r, g, b)

    matriz_booleana = geraMatriz(imagem, altura, largura, alter_r, alter_g, alter_b)
    salvarMatriz(matriz_booleana, altura, largura)

    removeSelecionado(altura, largura, matriz_booleana, caminho_imagem)
    removeEntorno(altura, largura, matriz_booleana, caminho_imagem)
    alteraSelecionado(altura, largura, matriz_booleana, caminho_imagem)
    alteraEntorno(altura, largura, matriz_booleana, caminho_imagem)

main()
