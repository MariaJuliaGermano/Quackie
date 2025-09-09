# 🦆 Quackie: A Rede Social que Faz Barulho!

Bem-vindo ao repositório oficial do **Quackie**! A rede social onde suas ideias podem voar livremente, desde que façam "quack". Inspirado nos tempos de ouro do antigo Twitter, o Quackie é um lugar para compartilhar pensamentos, piadas e, claro, muitos trocadilhos com patos.

Este projeto está no ninho, evoluindo de uma aplicação monolítica para uma arquitetura moderna de microserviços. Atualmente, este repositório contém o **backend (API)** do Quackie, construído com o poderoso framework Django.

## 📋 Índice

- [O que é o Quackie?](#o-que-é-o-quackie)
- [🚀 Começando](#-começando)
- [📋 Pré-requisitos](#-pré-requisitos)
- [⚙️ Rodando Localmente](#️-rodando-localmente)
- [🤝 Contribuindo](#-contribuindo)

## O que é o Quackie?

Quackie é mais do que uma plataforma, é um bando! Aqui, os posts são chamados de "Quacks" e o objetivo é criar um ambiente divertido e direto para a troca de ideias. Nossa filosofia é simples: menos caracteres, mais personalidade.

Este backend é o cérebro por trás da operação, responsável por gerenciar usuários, "Quacks", autenticação e tudo mais que faz nosso lago digital funcionar.

## 🚀 Começando

Para colocar o Quackie para voar na sua máquina local, você precisará de algumas ferramentas. Não se preocupe, é mais fácil do que ensinar um pato a nadar!

## 📋 Pré-requisitos

Antes de começar, garanta que você tenha os seguintes itens instalados no seu sistema:

- **Python 3.8+**: O coração da nossa aplicação. Você pode baixar em [python.org](https://www.python.org/downloads/).
  - Para verificar se você já tem, abra o terminal e digite:
    ```bash
    python --version
    ```

- **pip**: O gerenciador de pacotes do Python. Geralmente, ele já vem junto com o Python.

## ⚙️ Rodando Localmente

Com os pré-requisitos em ordem, siga estes passos para mergulhar no código:

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/Quackie.git](https://github.com/seu-usuario/Quackie.git)
    cd Quackie
    ```

2.  **Crie e ative um ambiente virtual (Virtual Environment):**
    É uma boa prática para não bagunçar as dependências do seu sistema!
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no Linux/Mac
    source venv/bin/activate
    ```
    *Seu terminal deve agora mostrar `(venv)` no início da linha.*

3.  **Instale as dependências:**
    Temos um arquivo `requirements.txt` que lista tudo que o Quackie precisa para funcionar. É bem magrinho por enquanto!
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    Isso irá preparar o banco de dados (SQLite por padrão) com as tabelas necessárias.
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (opcional, mas recomendado):**
    Para ter acesso ao painel de administração do Django.
    ```bash
    python manage.py createsuperuser
    ```
    *Siga as instruções para criar seu usuário e senha.*

6.  **Inicie o servidor de desenvolvimento:**
    A hora da verdade!
    ```bash
    python manage.py runserver
    ```

✨ **Pronto!** O servidor do Quackie estará rodando em `http://127.0.0.1:8000/`. Você já pode começar a testar os endpoints ou visitar a área de admin em `http://127.0.0.1:8000/admin/`.

## 🤝 Contribuindo

O Quackie está de asas abertas para contribuições! Se você tem uma ideia para um novo recurso ou encontrou um bug, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*. Vamos juntos fazer deste o melhor lago da internet!

---
Feito com ❤️ e muitos quacks!