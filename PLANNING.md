# PLANEJAMENTO — Sistema de Gestão Financeira Pessoal

## 1. VISÃO GERAL

**Objetivo:** Criar um sistema web completo de gestão financeira pessoal que permita aos usuários cadastrar, editar, visualizar e gerenciar receitas e despesas de forma organizada e segura.

**Público-alvo:** Múltiplos usuários, cada um com seus dados isolados e privados.

**Escopo Inicial:** MVP (Mínimo Produto Viável) funcional com funcionalidades essenciais para demonstrar competência em desenvolvimento fullstack.

**Tecnologias:** Python + Flask (Backend), SQLite (Banco de Dados), HTML + CSS (Frontend), Git + GitHub (Versionamento).

---

## 2. USUÁRIOS E PAPÉIS

### Usuário Padrão
- Pode se cadastrar no sistema com email e senha
- Pode fazer login com suas credenciais
- Gerencia apenas suas próprias transações (receitas e despesas)
- Não tem permissão de visualizar dados de outros usuários
- Pode filtrar e consultar seu histórico financeiro
- Pode ver seu saldo atual no dashboard

---

## 3. CATEGORIAS FINANCEIRAS

### Categorias Padrão (Pré-definidas pelo Sistema)

**Receitas:**
- Salário
- Freelance
- Investimentos
- Bônus
- Outros

**Despesas:**
- Alimentação
- Transporte
- Lazer
- Contas de Consumo (Água, Luz, Internet)
- Saúde
- Compras
- Outros

### Notas sobre Categorias
- Categorias são pré-definidas (não há criação customizada no MVP)
- Cada usuário tem acesso às mesmas categorias padrão
- Futura feature: permitir que usuários criem categorias personalizadas

---

## 4. REQUISITOS FUNCIONAIS

### RF-001: Cadastro de Usuário

**Quem:** Visitante não autenticado

**O que:** Criar uma nova conta de usuário no sistema

**Por quê:** Permitir que novos usuários acessem o sistema com dados únicos

**Campos obrigatórios:**
- Nome completo
- Email (único no sistema)
- Senha
- Confirmação de Senha

**Validações:**
- Email deve ser válido (formato correto)
- Email não pode estar registrado anteriormente
- Senha deve ter mínimo 8 caracteres
- Senha deve conter: 1 maiúscula, 1 minúscula, 1 número, 1 caractere especial
- Senhas devem ser iguais (confirmação)
- Nome deve ter mínimo 3 caracteres

**Segurança:**
- Senha é armazenada com hash (bcrypt ou similar)
- Senha não é exibida em nenhum lugar

**Resultado esperado:**
- Usuário é criado no banco de dados
- Mensagem de sucesso é exibida
- Usuário é redirecionado automaticamente para fazer login
- Email de confirmação pode ser enviado (futura feature)

---

### RF-002: Login de Usuário

**Quem:** Visitante não autenticado

**O que:** Autenticar um usuário existente

**Por quê:** Permitir acesso seguro aos dados pessoais do usuário

**Campos obrigatórios:**
- Email
- Senha

**Validações:**
- Email deve existir no sistema
- Senha deve estar correta
- Credenciais inválidas geram mensagem de erro genérica (não revela se email existe)

**Segurança:**
- Sessão de usuário é criada após login bem-sucedido
- Sessão expira após período de inatividade (30 minutos sugerido)
- Usuário permanece logado ao fechar navegador (cookie seguro)

**Resultado esperado:**
- Sessão de usuário é estabelecida
- Usuário é redirecionado para o dashboard
- Seu nome aparece na navbar
- Opção de logout fica visível

---

### RF-003: Cadastrar Receita

**Quem:** Usuário autenticado

**O que:** Adicionar um novo lançamento de receita (entrada de dinheiro) ao sistema

**Por quê:** Registrar ganhos financeiros para acompanhar a renda

**Campos obrigatórios (preenchidos pelo usuário):**
- Descrição
- Valor
- Categoria

**Campos automáticos (gerados pelo sistema):**
- Data de criação (data e hora atual)
- Data de modificação (igual à data de criação no primeiro registro)

**Validações:**
- Valor deve ser maior que 0
- Descrição obrigatória (mínimo 5 caracteres, máximo 255)
- Categoria deve ser válida (pré-definida)

**Formatação:**
- Valor aceita 2 casas decimais (ex: 1250.50)
- Data e hora são armazenadas automaticamente pelo sistema

**Resultado esperado:**
- Receita é salva no banco de dados associada ao usuário
- `data_criacao` é registrada automaticamente
- Mensagem de sucesso é exibida
- Saldo total é atualizado automaticamente
- Usuário é redirecionado para a lista de receitas ou fica na mesma página (opcional)

---

### RF-004: Cadastrar Despesa

**Quem:** Usuário autenticado

**O que:** Adicionar um novo lançamento de despesa (saída de dinheiro) ao sistema

**Por quê:** Registrar gastos financeiros para acompanhar as despesas

**Campos obrigatórios (preenchidos pelo usuário):**
- Descrição
- Valor
- Categoria

**Campos automáticos (gerados pelo sistema):**
- Data de criação (data e hora atual)
- Data de modificação (igual à data de criação no primeiro registro)

**Validações:**
- Valor deve ser maior que 0
- Descrição obrigatória (mínimo 5 caracteres, máximo 255)
- Categoria deve ser válida (pré-definida)

**Formatação:**
- Valor aceita 2 casas decimais (ex: 89.99)
- Data e hora são armazenadas automaticamente pelo sistema

**Resultado esperado:**
- Despesa é salva no banco de dados associada ao usuário
- `data_criacao` é registrada automaticamente
- Mensagem de sucesso é exibida
- Saldo total é atualizado automaticamente (reduzido)
- Usuário é redirecionado para a lista de despesas ou fica na mesma página (opcional)

---

### RF-005: Editar Transação

**Quem:** Usuário autenticado (apenas dono da transação)

**O que:** Modificar os dados de uma receita ou despesa existente

**Por quê:** Corrigir erros ou atualizar informações de transações registradas

**Campos editáveis:**
- Descrição
- Valor
- Categoria

**Campos NÃO editáveis (Auditoria):**
- Data de criação (imutável — registra quando foi criado)
- Data de modificação (atualizada automaticamente pelo sistema)

**Validações:**
- Mesmas validações do cadastro (RF-003 e RF-004)
- Apenas o dono da transação pode editar

**Resultado esperado:**
- Transação é atualizada no banco de dados
- `data_modificacao` é atualizada automaticamente pelo sistema
- Saldo total é recalculado automaticamente
- Mensagem de sucesso é exibida
- Usuário permanece na página de edição ou é redirecionado para a lista
- Histórico mostra quando foi criada e quando foi modificada

---

### RF-006: Deletar Transação

**Quem:** Usuário autenticado (apenas dono da transação)

**O que:** Remover permanentemente uma receita ou despesa do sistema

**Por quê:** Eliminar lançamentos incorretos ou indesejados

**Segurança e Comportamento:**
- Apenas o dono da transação pode deletar
- Exclusão é permanente (hard delete) — não pode ser recuperada no MVP
- Confirmação de exclusão é solicitada antes de deletar
- Saldo total é recalculado automaticamente

**Resultado esperado:**
- Transação é removida do banco de dados
- Saldo total é atualizado
- Mensagem de confirmação é exibida
- Usuário é redirecionado para a lista de transações

---

### RF-007: Visualizar Saldo Total

**Quem:** Usuário autenticado

**O que:** Exibir o saldo financeiro atual do usuário

**Por quê:** Fornecer uma visão rápida da situação financeira

**Cálculo:**
- Saldo = Soma de todas as receitas - Soma de todas as despesas

**Visualização:**
- Exibido no dashboard de forma destacada
- Atualizado em tempo real após cada operação
- Formato: Moeda com 2 casas decimais (ex: R$ 1.234,56)

**Resultado esperado:**
- Saldo correto é exibido no dashboard
- Saldo é atualizado automaticamente após CRUD de transações
- Se negativo, pode ter formatação diferente (em vermelho, por exemplo)

---

### RF-008: Filtrar por Período

**Quem:** Usuário autenticado

**O que:** Exibir apenas transações dentro de um período de datas específico

**Por quê:** Analisar receitas e despesas de um mês, semestre, ano, etc.

**Opções de Filtro:**
- Data inicial e data final (seletor visual)
- Atalhos rápidos: Este mês, Mês passado, Últimos 3 meses, Este ano
- Sem filtro (padrão — mostra tudo)

**Validações:**
- Data inicial deve ser menor ou igual à data final
- Ambas as datas são obrigatórias quando filtro é ativado

**Resultado esperado:**
- Lista de transações é filtrada de acordo com o período
- Saldo é recalculado para o período (opcional — mostrar "saldo do período")
- Filtro ativo é indicado visualmente
- Botão para limpar filtro é disponibilizado

---

### RF-009: Filtrar por Categoria

**Quem:** Usuário autenticado

**O que:** Exibir apenas transações de uma categoria específica

**Por quê:** Analisar gastos/ganhos em categorias específicas

**Funcionalidade:**
- Dropdown/select com todas as categorias disponíveis
- Possibilidade de selecionar múltiplas categorias (opcional para MVP)
- Sem filtro (padrão — mostra tudo)

**Combinação com Filtro de Período:**
- Filtros de período e categoria podem ser usados juntos
- Se ambos ativados, transação deve atender ambas as condições

**Resultado esperado:**
- Lista de transações é filtrada de acordo com a categoria
- Saldo é recalculado para a categoria (opcional)
- Filtro ativo é indicado visualmente
- Botão para limpar filtro é disponibilizado

---

### RF-010: Ver Histórico de Transações

**Quem:** Usuário autenticado

**O que:** Exibir uma lista completa de todas as receitas e despesas do usuário

**Por quê:** Permitir visualização e análise do histórico financeiro

**Exibição:**
- Tabela ou lista com colunas: Descrição, Categoria, Valor, Tipo (Receita/Despesa), Data Criação, Data Modificação
- Ordenação padrão: Data Criação (mais recentes primeiro)
- Possibilidade de ordenar por: Data Criação, Data Modificação, Valor, Categoria
- Paginação (se houver muitos registros)

**Informações de Auditoria:**
- Data Criação: Quando a transação foi registrada (imutável)
- Data Modificação: Quando a transação foi editada pela última vez (atualizada automaticamente)
- Se Data Criação ≠ Data Modificação, indica que foi editada

**Cores/Indicadores:**
- Receitas em verde (ou símbolo +)
- Despesas em vermelho (ou símbolo -)

**Ações Disponíveis:**
- Botão editar para cada transação
- Botão deletar para cada transação
- Filtro por período
- Filtro por categoria

**Resultado esperado:**
- Lista completa e bem organizada de transações
- Fácil leitura e navegação com informações de auditoria
- Rápido acesso para editar ou deletar
- Usuário consegue ver quando cada transação foi criada e modificada

---

### RF-011: Dashboard

**Quem:** Usuário autenticado

**O que:** Exibir um resumo visual da situação financeira do usuário

**Por quê:** Fornecer uma visão geral rápida e intuitiva da saúde financeira

**Componentes do Dashboard:**

1. **Saldo Total**
   - Valor destacado (grande, visível)
   - Formato: Moeda com 2 casas decimais
   - Cor diferente se negativo

2. **Resumo do Mês Atual**
   - Total de receitas (mês atual)
   - Total de despesas (mês atual)
   - Saldo do mês (receitas - despesas)

3. **Últimas Transações**
   - Últimas 5-10 transações
   - Data, descrição, categoria, valor
   - Link para ver histórico completo

4. **Resumo por Categoria (Despesas)**
   - Top 3-5 categorias com mais gastos
   - Valor total por categoria
   - Percentual do total de despesas

5. **Botões de Ação Rápida**
   - "Adicionar Receita"
   - "Adicionar Despesa"
   - "Ver Histórico Completo"

**Responsividade:**
- Dashboard funciona bem em desktop e mobile
- Componentes se reorganizam em telas pequenas

**Resultado esperado:**
- Usuário tem visão completa da situação financeira ao fazer login
- Informações estão claras e bem organizadas
- Fácil acesso a ações principais
- Carrega rapidamente

---

### RF-012: Logout

**Quem:** Usuário autenticado

**O que:** Encerrar a sessão do usuário no sistema

**Por quê:** Garantir segurança ao sair da aplicação

**Comportamento:**
- Sessão é destruída
- Cookies de sessão são limpos
- Histórico de navegador não permite acessar dados privados

**Resultado esperado:**
- Usuário é redirecionado para página inicial (antes do login)
- Botão de logout não aparece mais
- Login é necessário para acessar a aplicação novamente

---

## 5. REQUISITOS NÃO-FUNCIONAIS

| Requisito | Descrição | Meta |
|---|---|---|
| **Segurança** | Senhas com hash (bcrypt) + caracteres especiais | 100% das senhas com 1 maiúsc, 1 minúsc, 1 num, 1 caractere especial |
| **Autenticação** | Cada usuário tem sessão isolada | Sessões expiram após 30 min de inatividade |
| **Isolamento de Dados** | Usuários só veem seus próprios dados | Validação em todas as operações |
| **Auditoria** | Rastreamento de criação e modificação | Todos os registros têm `data_criacao` e `data_modificacao` |
| **Imutabilidade** | Data de criação não pode ser editada | Apenas `data_modificacao` é atualizada automaticamente |
| **Performance** | Páginas carregam rapidamente | Menos de 2 segundos no desktop |
| **Compatibilidade** | Funciona em navegadores modernos | Chrome, Firefox, Safari, Edge (versões recentes) |
| **Responsividade** | Interface adapta a diferentes tamanhos | Mobile, tablet, desktop |
| **Disponibilidade** | Sistema online e acessível | 99% uptime após deploy |
| **Validação de Dados** | Todos os campos são validados | Frontend + Backend |
| **Feedback ao Usuário** | Mensagens de sucesso e erro claras | Feedback visual imediato |
| **Navegação** | Interface intuitiva e fácil | Novo usuário entende sem tutorial |

---

## 6. CASOS DE USO

### Caso 1: Novo usuário se cadastra e faz primeira transação

1. Visitante acessa a página inicial
2. Clica em "Cadastrar"
3. Preenche nome, email e senha (com 1 maiúsc, 1 minúsc, 1 num, 1 caractere especial)
4. Sistema valida os dados
5. Usuário é criado no banco de dados
6. Sistema redireciona para login automaticamente
7. Usuário faz login com suas credenciais
8. Dashboard é exibido (vazio, sem transações)
9. Usuário clica em "Adicionar Despesa"
10. Preenche: descrição, valor (50.00), categoria (Alimentação)
11. Sistema registra automaticamente: data_criacao (agora)
12. Sistema salva a despesa
13. Saldo total muda de 0 para -50.00
14. Dashboard é atualizado com a nova transação
15. Usuário vê sua despesa na lista de histórico (com data_criacao e data_modificacao iguais)

### Caso 2: Usuário lança múltiplas transações e filtra por período

1. Usuário logado acessa dashboard
2. Adiciona receita: 3000.00 (Salário) — data_criacao 01/09 (automática)
3. Adiciona despesa: 500.00 (Aluguel) — data_criacao 05/09 (automática)
4. Adiciona despesa: 200.00 (Alimentação) — data_criacao 10/09 (automática)
5. Adiciona despesa: 100.00 (Transporte) — data_criacao 15/09 (automática)
6. Saldo total agora é 2200.00
7. Usuário clica em "Ver Histórico"
8. Vê todas as 4 transações com datas_criacao automáticas
9. Clica em filtro "Últimos 7 dias"
10. Sistema mostra apenas transações de 09/09 em diante (3 transações)
11. Saldo recalculado: 2300.00 (período)

### Caso 3: Usuário quer analisar gastos em uma categoria

1. Usuário logado acessa dashboard
2. Clica em filtro "Por Categoria"
3. Seleciona "Alimentação"
4. Sistema mostra apenas despesas com categoria Alimentação
5. Usuário vê: 200.00 + 150.00 + 75.00 = 425.00 total em Alimentação
6. Decide editar uma transação (aumentar valor de 75 para 100)
7. Clica no ícone de editar
8. Altera valor para 100.00
9. Nota que a `data_criacao` não pode ser editada (bloqueada)
10. Salva as alterações
11. Sistema atualiza `data_modificacao` automaticamente
12. Total de Alimentação agora é 450.00
13. Saldo total é recalculado
14. No histórico, agora aparece que `data_criacao` ≠ `data_modificacao` (transação foi editada)

### Caso 4: Usuário comete erro e precisa deletar transação

1. Usuário logado está vendo histórico
2. Percebe que registrou uma despesa duplicada
3. Clica no botão deletar de uma das transações
4. Sistema exibe confirmação: "Deseja deletar esta transação?"
5. Usuário confirma
6. Transação é removida permanentemente
7. Saldo total é recalculado
8. Mensagem de sucesso é exibida

---

## 7. FLUXO GERAL DA APLICAÇÃO

┌─────────────────────────────────────────────────────────────┐
│ PÁGINA INICIAL (/) │
│ [Não autenticado - Opções: Cadastro / Login] │
└─────────────────────────────────────────────────────────────┘
↓
┌───────────────────────────────────────┐
│ │
↓ ↓
[CADASTRO] [LOGIN]
(/cadastro) (/login)
│ │
│ (Validações) (Validações)
│ │
↓ ↓
(Email existe?) ──→ Erro (Email existe?) ──→ Erro
(Senhas iguais?) ──→ Erro (Senha correta?) ──→ Erro
(Senha forte?) ──→ Erro
│ │
↓ (Sucesso) ↓ (Sucesso)
Usuário criado Sessão criada
Redirecionado para Login │
└──────────────────────────────────────┘
↓
┌───────────────────────┐
│ DASHBOARD (/) │
│ [Autenticado] │
│ - Saldo total │
│ - Últimas transações │
│ - Botões de ação │
└───────────────────────┘
↓ ↓ ↓ ↓
┌───────────┼────┼────┼────┼──────────┐
│ │ │ │ │ │
↓ ↓ ↓ ↓ ↓ ↓
[ADD REC] [ADD DESP] [HISTÓRICO] [FILTROS] [LOGOUT]
(/receita/ (/despesa/ (/historico)
novo) novo)

HISTÓRICO permite:
- Editar transação (/transacao/<id>/editar)
- Deletar transação (DELETE /transacao/<id>)
- Filtrar por período
- Filtrar por categoria
- Ver data_criacao e data_modificacao
- Ordenar

LOGOUT destrói sessão → Volta para PÁGINA INICIAL

---

## 8. ESTRUTURA INICIAL DO PROJETO

personal-finance-system/
│
├── PLANNING.md ← Documentação do planejamento (este arquivo)
├── README.md ← Documentação para GitHub
├── .gitignore ← Arquivos a ignorar no Git
├── requirements.txt ← Dependências Python
├── main.py ← Arquivo principal (entrada da aplicação)
│
├── app/ ← Pacote principal da aplicação
│ ├── init.py ← Inicialização do Flask
│ ├── models.py ← Modelos de banco de dados (SQLAlchemy)
│ ├── forms.py ← Formulários (Flask-WTF)
│ ├── routes.py ← Rotas (URLs e lógica)
│ └── config.py ← Configurações (DB, segurança, etc)
│
├── templates/ ← Templates HTML (Jinja2)
│ ├── base.html ← Template base (navbar, footer, etc)
│ ├── index.html ← Página inicial
│ ├── cadastro.html ← Cadastro de usuário
│ ├── login.html ← Login
│ ├── dashboard.html ← Dashboard (após login)
│ ├── historico.html ← Histórico de transações
│ ├── transacao_form.html ← Formulário de receita/despesa
│ ├── transacao_editar.html ← Editar transação
│ └── erro.html ← Página de erro (404, 500, etc)
│
├── static/ ← Arquivos estáticos
│ ├── css/
│ │ └── style.css ← Estilos (CSS)
│ │
│ ├── js/
│ │ └── script.js ← JavaScript (validações, interatividade)
│ │
│ └── img/ ← Imagens
│ └── logo.png ← Logo (futura)
│
└── instance/ ← Instância da aplicação (gerada automaticamente)
└── database.db ← Banco de dados SQLite (gerado)


---

## 9. TECNOLOGIAS E FERRAMENTAS

| Categoria | Tecnologia | Propósito |
|---|---|---|
| **Linguagem** | Python 3.9+ | Backend e lógica |
| **Framework Web** | Flask | Microframework para web |
| **Banco de Dados** | SQLite | Persistência de dados (MVP) |
| **ORM** | SQLAlchemy | Abstração do banco de dados |
| **Autenticação** | Flask-Login | Gerenciamento de sessões |
| **Segurança** | Werkzeug | Hash de senhas |
| **Formulários** | Flask-WTF | Validação e geração de forms |
| **Frontend** | HTML5 + CSS3 | Interface do usuário |
| **JavaScript** | Vanilla JS | Interatividade (mínimo) |
| **Versionamento** | Git | Controle de versão |
| **Repositório** | GitHub | Hospedagem do código |
| **Hospedagem** | Render / Railway | Deploy online |

---

## 10. DECISÕES DE DESIGN

| Decisão | Escolha | Justificativa |
|---|---|---|
| **Categorias** | Pré-definidas | Simples no MVP, escalável depois |
| **Exclusão** | Hard Delete | Direto, sem complexidade de soft delete |
| **Isolamento** | Por Usuário | Essencial para segurança |
| **Sessão** | Flask-Login | Padrão, seguro, bem mantido |
| **Banco de Dados** | SQLite (MVP) | Sem servidor, perfeito para começar |
| **Deploy** | Render / Railway | Gratuito, simples, escalável |
| **Autenticação** | Email + Senha | Padrão do mercado |
| **Data de Registro** | Automática (sistema) | Evita erros do usuário, garante auditoria |
| **Auditoria** | data_criacao + data_modificacao | Profissional, rastreável, essencial para financeiro |
| **Imutabilidade** | data_criacao não editável | Mantém integridade do histórico |
| **Segurança de Senha** | 4 requisitos (maiúsc, minúsc, num, especial) | Protege contra brute force e senhas fracas |

---

## 11. PLANO DE DESENVOLVIMENTO

### Fase 1 — Planejamento ✅ (Concluída)
- [x] Definir requisitos funcionais
- [x] Definir requisitos não-funcionais
- [x] Estruturar casos de uso
- [x] Planejar arquitetura
- [x] Definir sistema de auditoria

### Fase 2 — Setup
- [ ] Criar repositório GitHub
- [ ] Criar ambiente virtual Python
- [ ] Instalar dependências
- [ ] Estruturar pastas do projeto

### Fase 3 — Banco de Dados
- [ ] Desenhar modelagem
- [ ] Criar modelos (SQLAlchemy) com auditoria
- [ ] Testar migrações

### Fase 4 — Backend Base
- [ ] Estruturar Flask
- [ ] Criar rotas (RF-001 e RF-002: Cadastro e Login)
- [ ] Implementar autenticação
- [ ] Validar força de senha

### Fase 5 — CRUD de Transações
- [ ] Implementar RF-003 a RF-006 (Cadastro, Edição, Exclusão)
- [ ] Validações backend
- [ ] Gerenciar data_criacao e data_modificacao

### Fase 6 — Dashboard e Filtros
- [ ] Implementar RF-007 a RF-011 (Saldo, Filtros, Dashboard)
- [ ] Cálculos de agregação

### Fase 7 — Frontend
- [ ] HTML de todas as páginas
- [ ] CSS responsivo
- [ ] JavaScript para validações e interatividade
- [ ] Exibir informações de auditoria

### Fase 8 — Testes
- [ ] Testes manuais
- [ ] Testes automatizados básicos

### Fase 9 — Refatoração
- [ ] Review de código
- [ ] Melhorias de segurança
- [ ] Otimizações

### Fase 10 — Deploy
- [ ] Preparar para produção
- [ ] Deploy em Render ou Railway
- [ ] Configurar domínio (opcional)

### Fase 11 — Documentação
- [ ] README.md completo
- [ ] Screenshots
- [ ] LinkedIn + GitHub

---

## 12. NOTAS IMPORTANTES

- **Segurança em primeiro lugar:** Sempre validar dados no backend
- **User Experience:** Mensagens de erro claras e feedback visual
- **Performance:** Otimizar queries do banco de dados
- **Escalabilidade:** Código modular para adicionar features depois
- **Documentação:** Manter código legível e bem comentado
- **Auditoria:** Sempre rastrear quando dados foram criados e modificados
- **Testes:** Testar funcionalidades essenciais
- **Deploy:** Preparar para ambiente de produção desde o início

---

## 13. GLOSSÁRIO

| Termo | Significado |
|---|---|
| **MVP** | Minimum Viable Product — versão mínima funcional |
| **RF** | Requisito Funcional — o que o sistema faz |
| **RNF** | Requisito Não-Funcional — como o sistema funciona |
| **CRUD** | Create, Read, Update, Delete — operações básicas |
| **ORM** | Object-Relational Mapping — abstração de banco de dados |
| **Hash** | Função criptográfica de sentido único |
| **Sessão** | Estado do usuário logado |
| **Soft Delete** | Marcar como deletado sem remover |
| **Hard Delete** | Remover permanentemente |
| **Responsivo** | Interface que adapta a diferentes telas |
| **Auditoria** | Rastreamento de criação e modificação de dados |
| **Imutável** | Que não pode ser alterado |
| **data_criacao** | Timestamp de quando o registro foi criado |
| **data_modificacao** | Timestamp de quando o registro foi modificado pela última vez |

---

**Data de Criação:** 2026-09-17  
**Data de Atualização:** 2026-09-17  
**Versão:** 1.1 (MVP com Auditoria)  
**Status:** Planejamento Completo

---

## HISTÓRICO DE ALTERAÇÕES

### Versão 1.1 (2026-09-17)
- ✅ Adicionado requisito de caractere especial na senha
- ✅ Data e hora passam a ser automáticas (não editáveis pelo usuário)
- ✅ Implementado sistema de auditoria (`data_criacao` e `data_modificacao`)
- ✅ Data de criação marcada como imutável
- ✅ Data de modificação atualizada automaticamente em edições
- ✅ Atualizado RF-003, RF-004, RF-005, RF-010
- ✅ Atualizados casos de uso 1 e 3
- ✅ Adicionadas colunas de auditoria no fluxo
- ✅ Atualizado plano de desenvolvimento

### Versão 1.0 (2026-09-17)
- Planejamento inicial completo
- Definição de requisitos funcionais e não-funcionais
- Definição de casos de uso
- Definição de arquitetura