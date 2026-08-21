# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Sompo Predict - Prevenção de Quebra e Sobrecarga 

## Grupo 49

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/guilherme-monteiro-tech/">Guilherme Monteiro Bitencourt (RM: 574151)</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b/">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi</a>


## 📜 Descrição

O presente projeto foi desenvolvido no âmbito do Challenge da Sompo Seguros, com o objetivo de transformar a gestão de maquinário agrícola de um modelo reativo para uma atuação estritamente preventiva. O principal problema de negócio abordado é o alto índice de sinistralidade e prejuízos operacionais causados pela quebra repentina de máquinas (tratores, colheitadeiras) devido à sobrecarga mecânica e falhas não monitoradas.

Para mitigar esses riscos, foi desenvolvida uma solução de ponta a ponta na Sprint 3. O sistema atua recebendo dados reais ou simulados de telemetria das máquinas — com foco em indicadores de desgaste térmico e cinético, como Temperatura do Motor (Celsius), Rotações por Minuto (RPM), Idade do Equipamento e Horas de Uso Contínuo. 

O fluxo é orquestrado por um backend construído em Python (FastAPI), que aplica validações de contrato de dados e garante a segurança da informação exigindo autenticação via API Key (`x-api-key`). Ao receber as leituras, a API aciona o nosso Motor Preditivo de Machine Learning (desenvolvido na Sprint 2), que classifica o risco iminente de quebra e calcula a probabilidade de falha mecânica. 

Os dados recebidos e os alertas gerados são imediatamente persistidos em um banco de dados relacional (SQLite), garantindo a rastreabilidade histórica essencial para auditorias de sinistro. Para o usuário final, o sistema fornece um Dashboard interativo desenvolvido em Streamlit, onde o gestor de frota da Sompo Seguros pode monitorar os equipamentos em tempo real e visualizar alertas críticos de parada iminente, possibilitando a intervenção antes que a quebra catastrófica ocorra.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto (inclui o arquivo `.env` com chaves de segurança).

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das fases (contém o `api.py` e o `dashboard.py`).

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🔧 Como executar o código

### Pré-requisitos
- Python versão 3.10 ou superior instalada.
- IDE de desenvolvimento (ex: Visual Studio Code).
- Bibliotecas exigidas: `fastapi`, `uvicorn`, `pydantic`, `pandas`, `streamlit`, `python-dotenv`.

### Passo a passo para execução local

1. **Baixe ou clone o repositório** para a sua máquina.
2. **Abra o terminal** na pasta raiz do projeto.
3. **Instale todas as dependências** executando:
   ```bash
   pip install fastapi uvicorn pydantic pandas streamlit python-dotenv
4. Configure a Segurança (Variáveis de Ambiente):
Crie um arquivo chamado `.env` na raiz do projeto e insira a chave de acesso da API:
API_KEY_SOMPO=12345678!

Iniciando a Aplicação
O sistema possui duas camadas que precisam rodar simultaneamente:

1. O Backend Integrador (FastAPI)
Em um terminal, inicie o servidor:

Bash
uvicorn src.api:app --reload
(A interface interativa da API e o Swagger estarão em: http://localhost:8000/docs)

2. O Front-end Gerencial (Streamlit)
Em um segundo terminal, rode o dashboard:

Bash
streamlit run src/dashboard.py
(O painel abrirá automaticamente no navegador web em: http://localhost:8501)

## 🗃 Histórico de lançamentos

* 0.2.0 - 21/08/2026
* 0.1.0 - 02/06/2026
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

