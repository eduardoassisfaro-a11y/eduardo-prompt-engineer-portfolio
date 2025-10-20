# Agente IA para Automação de Marketing

**Stack:** Python, LangChain, OpenAI API, Webhooks (Zapier/Make), ManyChat

## Funcionalidades
- Geração de funis (mensagens, ganchos, CTAs) para Instagram/WhatsApp
- Calendário editorial dinâmico com sazonalidade
- A/B test de prompts com métricas simples (CTR aproximado, resposta/retorno)
- Exportação para Markdown/CSV

## Como rodar
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=...
python src/main.py --briefing data/briefing_exemplo.yaml
```

## Estrutura
```
marketing-agent/
├── data/
│   └── briefing_exemplo.yaml
├── prompts/
│   └── system.md
├── src/
│   └── main.py
└── tests/
    └── test_sanity.py
```
