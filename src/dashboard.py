import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Dashboard Sompo - Manutenção", layout="wide")

st.title("Sompo Seguros - Prevenção de Quebra de Maquinário")
st.write("Monitoramento de sobrecarga e risco de quebra em tempo real (Sprint 3).")


def carregar_dados():
    conexao = sqlite3.connect("sompo_telemetria_maquinas.db")
    query = "SELECT * FROM historico_equipamentos ORDER BY id DESC"
    try:
        df = pd.read_sql(query, conexao)
    except:
        df = pd.DataFrame()  # Retorna vazio se o banco ainda não existir
    conexao.close()
    return df


df = carregar_dados()

if df.empty:
    st.info("Nenhum dado mecânico recebido. Use a API para enviar testes de temperatura e RPM.")
else:
    st.subheader("Visão Geral da Frota")

    total_leituras = len(df)
    maquinas_criticas = len(df[df['alerta_quebra'].str.contains('CRÍTICO')])

    col1, col2 = st.columns(2)
    col1.metric("Total de Leituras Recebidas", total_leituras)
    col2.metric("🚨 Alertas CRÍTICOS (Parada Iminente)", maquinas_criticas)

    st.divider()

    st.subheader("📋 Histórico de Telemetria e Alertas")

    # Filtra e renomeia colunas para o painel ficar elegante
    tabela_visual = df[['data_hora', 'id_equipamento', 'horas_uso_continuo',
                        'rpm_medio', 'temperatura_celsius', 'alerta_quebra', 'probabilidade_quebra']]

    # Destaca os dados na tela
    st.dataframe(tabela_visual, width='stretch')
