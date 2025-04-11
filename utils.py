import random
import ipaddress
from datetime import datetime 
from faker import Faker

fake = Faker('pt_BR')

#cria uma classe de tentativa de login para registrar no log
class TentativaLogin:
    def __init__(self, user, password, ip, acesso):
        self.user = user
        self.password = password
        self.ip = ip
        self.acesso = acesso
        self.timestamp = datetime.now()
#define a saida do log passando os objetos no corpo do log
    def __str__(self):
        return f"[{self.timestamp}] User: {self.user} | IP: {self.ip} | Password: {self.password} | Acesso: {self.acesso}"

def gerar_tentativa_legitima():
    return TentativaLogin(
        user="sofia",
        password="soocsec",
        ip="10.100.29.4",
        acesso=True
    )

def gerar_tentativa_ataque():
    
    user = fake.first_name()
    password = fake.password()
    ip = fake.ipv4_public()
    return TentativaLogin(user, password, ip, False)