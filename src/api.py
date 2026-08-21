import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

# Carrega as senhas secretas do arquivo .env
load_dotenv()
CHAVE_SECRETA = os.getenv("API_KEY_SOMPO")

app = FastAPI(title="Sompo Seguros - Prevenção de Quebra", version="3.0")

# ==========================================
# 1. O NOSSO "ESTOQUE" (BANCO DE DADOS)
# ==========================================
def inicializar_banco():
    conexao = sqlite3.connect("sompo_telemetria_maquinas.db")
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico_equipamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            id_equipamento TEXT,
            idade_anos INTEGER,
            horas_uso_continuo REAL,
            rpm_medio REAL,
            temperatura_celsius REAL,
            alerta_quebra TEXT,
            probabilidade_quebra REAL
        )
    ''')
    conexao.commit()
    conexao.close()

inicializar_banco()

# ==========================================
# 2. O CONTRATO DE DADOS (Baseado no seu CSV)
# ==========================================
class TelemetriaMaquina(BaseModel):
    id_equipamento: str
    idade_anos: int
    horas_uso_continuo: float
    rpm_medio: float
    temperatura_celsius: float

# ==========================================
# 3. O "CÉREBRO" (Seu modelo da Sprint 2)
# ==========================================
def prever_quebra(idade, horas, rpm, temp):
    # Regra lógica simulando a descoberta estatística da Sprint 2
    if temp > 95 or rpm > 2800:
        return "CRÍTICO (Quebra Iminente)", 0.95
    elif temp > 85 or horas > 12 or idade >= 15:
        return "ALTO (Risco de Sobrecarga)", 0.70
    else:
        return "NORMAL", 0.10

# ==========================================
# 4. ROTA POST PROTEGIDA
# ==========================================
@app.post("/telemetria")
def receber_dados_maquina(dados: TelemetriaMaquina, x_api_key: str = Header(...)):
    
    # Trava de Segurança
    if x_api_key != CHAVE_SECRETA:
        raise HTTPException(status_code=401, detail="Acesso negado: Chave de API inválida.")
    
    # Avalia se haverá quebra
    status_alerta, probabilidade = prever_quebra(
        dados.idade_anos,
        dados.horas_uso_continuo,
        dados.rpm_medio,
        dados.temperatura_celsius
    )
    
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Salva no banco de dados
    conexao = sqlite3.connect("sompo_telemetria_maquinas.db")
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO historico_equipamentos 
        (data_hora, id_equipamento, idade_anos, horas_uso_continuo, rpm_medio, temperatura_celsius, alerta_quebra, probabilidade_quebra)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (data_atual, dados.id_equipamento, dados.idade_anos, 
          dados.horas_uso_continuo, dados.rpm_medio, dados.temperatura_celsius, 
          status_alerta, probabilidade))
    conexao.commit()
    conexao.close()
    
    return {
        "status": "sucesso",
        "mensagem": "Leitura mecânica gravada com sucesso",
        "alerta": status_alerta,
        "probabilidade_quebra": probabilidade
    }

# ==========================================
# 5. ROTA GET (LÊ O BANCO E MOSTRA NA TELA)
# ==========================================
@app.get("/historico")
def ver_historico_maquinas():
    conexao = sqlite3.connect("sompo_telemetria_maquinas.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM historico_equipamentos ORDER BY id DESC")
    registros = cursor.fetchall()
    conexao.close()

    historico = []
    for linha in registros:
        historico.append({
            "id_leitura": linha[0],
            "data_hora": linha[1],
            "equipamento": linha[2],
            "idade": linha[3],
            "horas_uso": linha[4],
            "rpm": linha[5],
            "temperatura": linha[6],
            "alerta": linha[7],
            "probabilidade": linha[8]
        })

    return {"total_leituras": len(historico), "dados": historico}