import json
import pandas as pd
import requests
import streamlit as st

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))

# ============ PRÉ-PROCESSAMENTO ============
# Resumo simples de gastos por categoria (iniciante-friendly)
gastos = transacoes[transacoes['tipo'] == 'saida']
resumo_gastos = gastos.groupby('categoria')['valor'].sum().reset_index()

# ============ MONTAR CONTEXTO ============
contexto = f"""
DADOS DO USUÁRIO:
- Nome: {perfil['nome']}
- Idade: {perfil['idade']}
- Profissão: {perfil['profissao']}
- Renda mensal: R$ {perfil['renda_mensal']}
- Perfil de investidor: {perfil['perfil_investidor']}
- Objetivo principal: {perfil['objetivo_principal']}
- Aceita risco: {"Sim" if perfil['aceita_risco'] else "Não"}

METAS FINANCEIRAS:
{json.dumps(perfil['metas'], indent=2, ensure_ascii=False)}

RESUMO DE GASTOS MENSAIS (SAÍDAS):
{resumo_gastos.to_string(index=False)}

HISTÓRICO DE ATENDIMENTO:
{historico[['data', 'tema', 'resumo']].to_string(index=False)}

BASE EDUCATIVA DE PRODUTOS (USO EXPLICATIVO):
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """
Você é o FinGuia, um agente financeiro inteligente focado em organização financeira para iniciantes.

OBJETIVO:
Ajudar o usuário a entender sua situação financeira, organizar gastos, acompanhar metas e aprender conceitos financeiros básicos de forma simples e segura.

REGRAS OBRIGATÓRIAS:
1. Utilize APENAS os dados fornecidos no contexto.
2. NÃO invente valores, produtos, rendimentos ou cenários.
3. NÃO recomende investimentos nem diga onde aplicar dinheiro.
4. Explique produtos financeiros apenas de forma educativa.
5. NÃO faça previsões financeiras ou promessas de retorno.
6. NÃO responda perguntas fora do escopo financeiro.
7. NÃO solicite nem processe dados sensíveis.
8. Quando faltar informação, admita claramente a limitação.
9. Linguagem simples, amigável e sem termos técnicos complexos.
10. Responda em até 3 parágrafos curtos.

EXEMPLOS DE COMPORTAMENTO ESPERADO:
- Se o usuário perguntar "Onde investir?", explique que não faz recomendações e ofereça ajuda com organização financeira.
- Se o usuário demonstrar confusão, simplifique e use exemplos do contexto dele.
- Se a pergunta sair do escopo, recuse educadamente e redirecione.
"""

# ============ CONFIGURAÇÃO OLLAMA ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"  # ajuste se necessário

# ============ FUNÇÃO DE PERGUNTA ============
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO USUÁRIO:
{contexto}

Pergunta do usuário:
{msg}
"""
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json().get("response", "Não consegui gerar uma resposta agora.")

# ============ INTERFACE STREAMLIT ============
st.title("💰 FinGuia — Seu Organizador Financeiro")

st.markdown(
    "Sou um assistente focado em **organização financeira e educação para iniciantes**. "
    "Posso te ajudar a entender gastos, metas e conceitos financeiros básicos."
)

if pergunta := st.chat_input("Digite sua dúvida sobre suas finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Analisando sua situação financeira..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
