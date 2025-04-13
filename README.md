# Simulador de Logs de Tentativas de Login

Projeto simples e útil que simula tentativas de login em um sistema — desde acessos legítimos até ataques maliciosos — gerando logs realistas em `.txt` e `.json`. Ideal pra quem estuda cibersegurança ou quer testar sistemas de monitoramento de eventos.

Esse projetos estará disponível com **mais detalhes** no meu [BLOG](https://sooftware.gitbook.io/soocsec/log-parser)

---

## Funcionalidades

-  Geração de tentativas legítimas e de ataque
-  Dados realistas usando a biblioteca Faker
-  Logs exportados em dois formatos: `.json` e `.txt`
-  Simulação de diferentes métodos HTTP, IPs e status
-  Ideal para treinar análise de logs e detecção de ataques

---

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/sofianmsilva/brute-force-log-simulator
   cd nome-da-pasta
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o simulador:
   ```bash
   python main.py
   ```

---

## Exemplo de saída

**Formato `.txt`**
```txt
[2025-04-11 13:48:12] User: Sofia Silva | IP: 10.100.29.4 | Password: soocsec | Sucesso: True | Method: POST | Rota: /login | Status: 200 OK | User-Agent: Mozilla/5.0...
```

**Formato `.json`**
```json
{
  "user": "Felipe Zepetto",
  "password": "123felipe",
  "ip": "10.100.29.15",
  "acesso": true,
  "metodo": "POST",
  "rota": "/login",
  "status": "200 OK",
  "user_agent": "Mozilla/5.0...",
  "time": "2025-04-11 13:48:12"
}
```

---

## Tecnologias usadas

- [Python 3.13.3](https://www.python.org/)
- [Faker](https://faker.readthedocs.io/en/master/)

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
