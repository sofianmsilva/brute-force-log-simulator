import random
import time

from utils import gerar_tentativa_legitima, gerar_tentativa_ataque

for _ in range(10):
    tentativa = (
        gerar_tentativa_ataque()
        if random.random() < 0.1
        else gerar_tentativa_legitima()
    )

print(tentativa)
time.sleep(0.5)

