# Antes de inicializar o codigo por favor realizar o (pip install pyautogui) no terminal

import pyautogui
import time

# Exibe um alerta para o usuário
pyautogui.alert(text='Apartir de agora não mexa em nada, por favor espere o bot finalizar o trabalho', title='Iniciando o bot', button='OK')
try:
    # Abrir o Google Chrome pressionando a tecla Windows (ou Command no Mac) e digitando "chrome" e Enter
    pyautogui.hotkey('win', 'r')  # Abre a caixa de execução do Windows
    pyautogui.write('chrome')     # Digita "chrome"
    pyautogui.press('enter')      # Pressiona Enter             
    time.sleep(5)                 # Aguarda um tempo para o Chrome abrir

    with pyautogui.hold('win'):   # Maximiza a janela do Chrome
            pyautogui.press(['up'])

    tela = pyautogui.size()       # Obtém a resolução da tela

    tela_x, tela_y = tela


    # Define as coordenadas do clique com base na resolução da tela
    if tela_x == 1280 and tela_y == 720:
        x_click,y_click = 510,485
    elif tela_x == 1366 and tela_y == 768:
        x_click,y_click = 553,486
    elif tela_x == 1360 and tela_y == 768:
        x_click,y_click = 549,486
    elif tela_x == 1280 and tela_y == 768:
        x_click,y_click = 510,486
    elif tela_x == 1280 and tela_y == 600:
        x_click,y_click = 510,486
    elif tela_x == 1024 and tela_y == 768:
        x_click,y_click = 381,486
    elif tela_x == 800 and tela_y == 600:
        x_click,y_click = 270,486
    else:
        recebe = pyautogui.alert(text='''
                                O bot detectou que o seu computador está com uma resolução que ele ainda não aceita,
                                então é necessario alterar a resolução do seu computador para essas opções:
                                (1280;720),(1360;768),(1024;768) ou (800;600)
                                   ''', title='Teste', buttons=['Ok irei mudar'])
        

    
    # Digitar o link na barra de pesquisa e pressionar Enter
    pyautogui.write('https://conta.olx.com.br/acesso')
    pyautogui.press('enter')

    time.sleep(3)     

    # Pressiona a tecla Tab duas vezes para ir para o campo de email
    pyautogui.press('tab', presses=2)
    pyautogui.write('') #Seu email

    time.sleep(3)     

    # Pressiona a tecla Tab para ir pro campo de senha
    pyautogui.press('tab')
    pyautogui.write('') #senha

    # Aguarda um tempo para a página carregar completamente
    time.sleep(2)     

    # Clica no botão do captcha
    pyautogui.click(x=x_click, y=y_click)  

    # Aguarda o captcha finalizar de carregar
    time.sleep(10)     

    # Pressiona a tecla Tab quatro vezes para ir para o botão de Login e acessar
    pyautogui.press('tab', presses=4)
    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.alert(text='O bot conseguiu realizar o serviço', title='Finalizado', button='OK')

except:
    pyautogui.alert(text='Infelizmente ocorreu um erro com o bot, por favor reinicie', title='Erro', button='OK')