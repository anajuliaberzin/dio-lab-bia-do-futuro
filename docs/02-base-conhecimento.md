# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Fornecer contexto sobre interações anteriores do usuário, temas já abordados e nível de maturidade financeira |
| `perfil_investidor.json` | JSON | Identificar perfil, renda, objetivos financeiros e restrições de risco do usuário |
| `produtos_financeiros.json` | JSON | Base informativa para explicar produtos financeiros de forma educativa (sem recomendação direta) |
| `transacoes.csv` | CSV | Analisar entradas e saídas para apoiar organização financeira básica e controle de gastos |

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram utilizados como mock data, representando um cenário realista de um usuário iniciante a moderado em organização financeira.
Não houve inclusão de dados sensíveis nem acesso a informações externas.

As adaptações ocorreram no nível lógico:

Simplificação da leitura das transações (agregação por categoria)

Uso do histórico de atendimento apenas para contextualização, não para tomada de decisão

Produtos financeiros tratados como conteúdo educativo, não como recomendação de investimento

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos CSV e JSON são carregados no início da execução do agente e mantidos em memória durante a sessão.
Esses dados compõem o contexto utilizado pelo agente para interpretar mensagens do usuário e manter continuidade nas interações.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Informações do perfil_investidor.json e regras de comportamento do agente são incluídas no system prompt para definir limites e tom das respostas.

Dados de historico_atendimento.csv e transacoes.csv são consultados dinamicamente a cada interação, permitindo respostas contextualizadas.

O arquivo produtos_financeiros.json é usado apenas para explicação conceitual quando o usuário pergunta sobre produtos financeiros.

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Usuário:
- Nome: João Silva
- Idade: 32
- Profissão: Analista de Sistemas
- Renda mensal: R$ 5.000
- Perfil de investidor: Moderado
- Objetivo principal: Construir reserva de emergência
- Aceita risco: Não

Metas financeiras:
- Completar reserva de emergência (R$ 15.000 até 06/2026)
- Entrada do apartamento (R$ 50.000 até 12/2027)

Resumo de transações recentes:
- Receita: Salário - R$ 5.000
- Moradia: Aluguel e conta de luz - R$ 1.380
- Alimentação: Supermercado e restaurante - R$ 570
- Transporte: Uber e combustível - R$ 295
- Saúde: Farmácia e academia - R$ 188
- Lazer: Streaming - R$ 55,90

Histórico de atendimentos relevantes:
- Explicação sobre Tesouro Selic
- Acompanhamento de metas financeiras
- Dúvidas sobre CDB e reserva de emergência
```
