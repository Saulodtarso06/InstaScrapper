# InstaScrapper

Um script em **Python** que permite baixar todas as fotos de um perfil público do Instagram de forma simples, utilizando a biblioteca [Instaloader](https://instaloader.github.io/).

## Funcionalidades
- Baixar todas as fotos de um perfil do Instagram.
- Organizar as fotos em uma pasta com o nome do perfil.
- Suporte a login para acessar perfis privados (necessário usuário e senha válidos).
- Fácil de usar e expandir.

## Tecnologias
- [Python 3.x](https://www.python.org/)
- [Instaloader](https://instaloader.github.io/)

## Instalação
Clone este repositório:
```bash
git clone https://github.com/seu-usuario/InstaPhotoDownloader.git

cd InstaPhotoDownloader
```
---

## Instale as dependências:
```
pip install instaloader
```
---

## Como Usar

Execute o script:
```
python baixar_fotos.py
```
```
Digite o nome do usuário (sem o @):
```
```
Digite o @ do perfil (sem o @): nasa
```

As fotos serão baixadas em uma pasta com o nome do usuário (/nasa neste exemplo).

## 🔐 Perfis Privados

Se você tiver acesso a um perfil privado:

1 - Descomente a linha de login no código:
```
# loader.login("seu_usuario", "sua_senha")
```

2 - Substitua seu_usuario e sua_senha pelas suas credenciais.

## ⚠️ Aviso Legal Importante !!!

Este projeto foi criado apenas para fins educacionais.
Respeite sempre os direitos autorais e a privacidade dos usuários.

O uso deste script é de total responsabilidade do usuário.

## 👨‍💻 Desenvolvido por Saulo de Tarso - FullStack Dev.