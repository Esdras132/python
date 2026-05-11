import pyautogui
import time

# 1. Ver o tamanho da sua tela
largura, altura = pyautogui.size()
print(f"Sua tela tem {largura}x{altura}")

# 2. Pegar a posição atual do mouse (útil para mapear onde clicar)
print("Posicione o mouse onde deseja e aguarde 3 segundos...")
time.sleep(3)
x, y = pyautogui.position()
print(f"A posição atual é: {x}, {y}")

# 3. Mover o mouse para uma posição específica (x, y) em 1 segundo
pyautogui.moveTo(500, 500, duration=1)

# 4. Clicar em um lugar específico
pyautogui.click(x=600, y=400)

# 5. Arrastar (ex: para mover arquivos ou desenhar)
pyautogui.dragTo(800, 800, duration=1, button='left')