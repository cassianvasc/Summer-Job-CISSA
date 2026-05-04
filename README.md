# 🛡️ Aplicação Web para Denúncia de Ameaças Cibernéticas

Este projeto é uma **aplicação web desenvolvida com Django e Python**, voltada para o **recebimento, registro e tratamento de denúncias de ameaças cibernéticas**, com foco em segurança da informação, rastreabilidade e compartilhamento de inteligência, visando aumentar a confiabilidade na comunicação entre entidades nas plataformas digitais de CTI.

A aplicação permite que usuários realizem denúncias de forma estruturada, segura e anônima, integrando essas informações a tecnologias de **Blockchain (Hyperledger Fabric)** e **MISP (Malware Information Sharing Platform)**.

---

## 🎯 Objetivo do Projeto

Criar um sistema capaz de:

- Receber denúncias de ameaças digitais (malware, ransomware, etc.)
- Armazenar essas informações de forma organizada
- Garantir **integridade e rastreabilidade** dos dados por meio de Blockchain
- Compartilhar indicadores relevantes de ameaça com plataformas de **Cyber Threat Intelligence (CTI)**, como o MISP
- Apoiar processos de análise, investigação e resposta a incidentes

---

## 🧩 Arquitetura Geral

Usuário
↓
Frontend (HTML + CSS)
↓
Backend (Django / Python)
↓
Banco de Dados
↓
Blockchain (Hyperledger Fabric)
↓
CTI / MISP

---

## ⚙️ Tecnologias Utilizadas

### 🔹 Backend
- Python
- Django

### 🔹 Frontend
- HTML5
- CSS3
- -Javascript
- Templates Django

### 🔹 Segurança e Infraestrutura
- CSRF Protection
- Variáveis de ambiente (`.env`)
- Boas práticas de versionamento com Git

### 🔹 Integrações
- **Hyperledger Fabric** (Blockchain permissionada para integridade e auditoria)
- **MISP** (Compartilhamento de indicadores de ameaça)

---

## 🧠 Funcionalidades Principais

- 📥 Formulário de denúncia de ameaças cibernéticas
- 🔐 Denúncia anônima
- ⛓️ Encaminhamento dos dados para Blockchain (Hyperledger)
- 🌐 Integração com MISP para CTI

---

## 🚀 Como executar o projeto localmente

### 1. Clone o repositório:
git clone https://github.com/cassianvasc/Summer-Job-CISSA

### 2. Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

### 3. Instale as dependências:
pip install requirements.txt

### 4. Execute o servidor:
python manage.py runserver

### 5. Acesse:
http://127.0.0.1:8000/
