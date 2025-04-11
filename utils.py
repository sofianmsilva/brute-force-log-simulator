import random
from faker import Faker

fake = Faker('pt_BR')

class TentativaLogin:
    def __init__(self, user, password, ip, acesso, time, metodo, rota="/login", status="200 OK", user_agent=None):
        self.user = user
        self.password = password
        self.ip = ip
        self.acesso = acesso
        self.metodo = metodo
        self.rota = rota
        self.status = status
        self.user_agent = user_agent or fake.user_agent()
        self.time = time

    def __str__(self):
        return f"[{self.time}] User: {self.user} | IP: {self.ip} | Password: {self.password} | Sucesso: {self.acesso} | Method: {self.metodo} | Rota: {self.rota} | Status: {self.status} | User-Agent: {self.user_agent}"
    
    def to_dict(self):
        return {
            "user": self.user,
            "password": self.password,
            "ip": self.ip,
            "acesso": self.acesso,
            "metodo": self.metodo,
            "rota": self.rota,
            "status": self.status,
            "user_agent": self.user_agent,
            "time": self.time.strftime("%Y-%m-%d %H:%M:%S"),
        }

legit_user = [
    {"user": "Sofia Silva", "password": "soocsec", "ip": "10.100.29.4"},
    {"user": "Felipe Zepetto", "password": "123felipe", "ip": "10.100.29.15"},
    {"user": "Carol Oliveira", "password": "carolzinha@", "ip": "10.100.29.26"},
    {"user": "Daniel Passos", "password": "Dan098712", "ip": "10.100.29.47"},
]

def gerar_metadados():
    return {
        "time": fake.date_time_between(start_date='-3d', end_date='now'),
        "metodo": random.choice(['GET', 'POST', 'PUT']),
        "rota": fake.uri_path(),
        "status": random.choice(["200 OK", "403 Forbidden", "401 Unauthorized"]),
        "user_agent": fake.user_agent()
    }

def gerar_tentativa_legitima():
    user = random.choice(legit_user)
    meta = gerar_metadados()
    return TentativaLogin(
        user=user["user"],
        password=user["password"],
        ip=user["ip"],
        acesso=True,
        **meta
    )

def gerar_tentativa_ataque():
    meta = gerar_metadados()
    return TentativaLogin(
        user=fake.name(),
        password=fake.password(),
        ip=fake.ipv4_public(),
        acesso=False,
        **meta
    )
