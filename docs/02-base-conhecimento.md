# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_usuario.json` | JSON | Armazenar informações básicas do usuário (renda, objetivos, nível de conhecimento financeiro) |
| `gastos_basicos.csv` | CSV | Simular gastos mensais por categoria para análise simples |
| `conceitos_financeiros.json` | JSON | Base educativa com definições simples (reserva de emergência, orçamento, metas) |
| `regras_orientacao.json` | JSON | Regras básicas para sugerir próximos passos financeiros de forma segura |

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram adaptados para representar cenários comuns de usuários iniciantes.
Foram criados valores fictícios de renda e gastos, além de simplificações nos conceitos financeiros para garantir uma linguagem acessível.
As regras de orientação foram estruturadas de forma declarativa, evitando recomendações financeiras complexas ou específicas.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV são carregados no início da sessão do agente e armazenados em memória. Essas informações são utilizadas como contexto para orientar as respostas do modelo de IA durante a interação com o usuário.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados principais do usuário e as regras de orientação são incluídos no system prompt para definir os limites e o comportamento do agente.
As informações de gastos e objetivos são consultadas dinamicamente a cada interação, permitindo que o agente adapte suas respostas conforme o progresso do usuário.

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Usuário:
- Nome: Ana
- Nível de conhecimento financeiro: Iniciante
- Renda mensal: R$ 2.500
- Objetivo principal: Organizar gastos e criar reserva de emergência

Gastos mensais estimados:
- Aluguel: R$ 900
- Alimentação: R$ 600
- Transporte: R$ 250
- Lazer: R$ 300

Regras de orientação:
- Priorizar controle de gastos antes de sugerir metas de longo prazo
- Evitar termos técnicos sem explicação
- Não recomendar investimentos

...
```
