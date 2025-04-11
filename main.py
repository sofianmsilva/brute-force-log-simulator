import random
import time
import json
from utils import gerar_tentativa_legitima, gerar_tentativa_ataque

# Cria a lista de tentativas
tentativas = []

for _ in range(8):
    tentativa = gerar_tentativa_ataque() if random.random() < 0.5 else gerar_tentativa_legitima()
    tentativas.append(tentativa)
    print(tentativa)
    time.sleep(0.8)


# Salva em TXT estilo log
with open("logs.txt", "w", encoding="utf-8") as f:
    for tentativa in tentativas:
        f.write(str(tentativa) + "\n")

# Salva em JSON formatado
with open("logs.json", "w", encoding="utf-8") as f:
    json.dump([t.to_dict() for t in tentativas], f, ensure_ascii=False, indent=4)