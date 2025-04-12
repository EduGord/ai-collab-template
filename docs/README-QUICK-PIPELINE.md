
# 🚀 Guia de Reentrada Rápida na Pipeline

Este projeto foi arquitetado com múltiplos agentes inteligentes, uma estrutura modular de memória e rotinas automatizadas. Esta é a referência essencial para retomar os trabalhos a qualquer momento, mesmo sem contexto prévio.

---

## 🧠 Como se orientar no projeto

- Veja o `memory-bank/00-memory-core.md` → resumo estratégico, agentes e estrutura
- Consulte `00-core-agent-map.json` para entender quem faz o quê
- Use `90-task-pending-list.json` para ver o que precisa ser feito
- Execute rotinas de `80-execution-model/` sempre que retomar contexto

---

## ✅ Principais pastas e funções

| Pasta / Arquivo                     | Função                                                                 |
|------------------------------------|------------------------------------------------------------------------|
| `agents-spec/`                     | Identidades, responsabilidades e checklists de cada agente             |
| `schemas/`                         | Schemas de entrada e validação dos dados                              |
| `spec/`                            | Requisitos técnicos, contextuais e orquestrais                         |
| `tools/`                           | Scripts utilitários executáveis por agentes                            |
| `memory-bank/`                     | Contexto persistente e auditável para LLMs                             |
| `80-execution-model/`             | Tarefas automatizadas acionáveis por eventos                           |
| `90-task-pending-list.json`        | Lista de pendências priorizadas                                        |

---

## 🤖 Se você é uma IA (modelo generalista)

1. Comece lendo `spec/context-spec.md` e `memory-bank/00-memory-core.json`
2. Navegue o `00-core-agent-map.json` para entender a orquestração
3. Verifique pendências e contribua com atualizações e sugestões

---

## 🧭 Dúvidas?

Fale com o `orchestrator-agent`. Ele organiza toda a operação do sistema.

## 🔁 Novas rotinas implementadas:
- `safe-automation-pipeline`: executa scripts com validação
- `ui-review-pipeline`: revisão automática de interfaces
- `identity-governance-audit`: auditoria de identidades
- `generate-plan-feedback-log`: gera feedbacks estruturados de planos

---

This document is currently under construction.

🛠️ To be filled with guidance, structure, and examples for:  
- readme quick pipeline
