import openpyxl
import pandas as pd
import pyautogui
import time
import pyperclip

# Alerta
pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")
pyautogui.PAUSE = 0.5

# abrir o Chrome
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)

df = pd.read_excel('auxiliar/articles.xlsx')
# loop para fazer download para todas as URLs
for i in range(0,len(df)):
    # ler a planilha Excel
    df = pd.read_excel('auxiliar/articles.xlsx')

    # copiar a URL da linha atual
    url = df.loc[i, 'url']
    pyperclip.copy(url)

    # cola url na barra de pesquisa do Chrome
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    # clicar no botão de download
    time.sleep(5)
    pyautogui.click(x=100, y=290)
    time.sleep(17)
    pyautogui.press('enter')  #salva o arquivo, se o download for direto
    time.sleep(3)

   # verificar a página aberta após clicar no botão de download
    if pyautogui.locateOnScreen('auxiliar/download_success.png',confidence=.9):
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'w')  #fecha a pagina
    elif pyautogui.locateOnScreen('auxiliar/view_abstract.png',confidence=.9):
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'w')  #fecha a pagina
    elif pyautogui.locateOnScreen('auxiliar/check_publisher_site.png',confidence=.5):
        time.sleep(5)
        pyautogui.click(x=1088, y=326)  #clicar em 'Check publisher site'
        time.sleep(5)
        if pyautogui.locateOnScreen('auxiliar/science_direct.png'):
            # clicar em "View PDF"
            pyautogui.click(x=417, y=219)
            # esperar e clicar no icone de download
            time.sleep(5)
            pyautogui.click(x=931, y=131)
            # esperar pelo download ser concluído e clicar em salvar
            time.sleep(5)
            pyautogui.click(x=1195, y=694)
            # Fechar três guias abertas
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
        elif pyautogui.locateOnScreen('auxiliar/eLife.png'):
            # clicar no icone de download
            pyautogui.click(x=1041, y=450)
            # clicar em "Article PDF"
            time.sleep(1)
            pyautogui.click(x=1038, y=541)
            # salvar
            time.sleep(1)
            pyautogui.press('enter')
            # fechar duas guias abertas
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
        else:
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'w')
    else:
        print("Algo diferente aconteceu")






# ALERTA
time.sleep(5)
pyautogui.alert("O código acabou de rodar. Pode usar o seu computador de novo")




