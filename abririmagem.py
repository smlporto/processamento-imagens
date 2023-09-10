import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import os

filename = filedialog.askopenfilename(initialdir=os.getcwd())

#Leitura do arquivo de imagem
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title('Exemplo de Imagem')
plt.show()
