# Kenzie Buster

Projeto realizado no quinto módulo do curso de Formação em Desenvolvimento Full Stack da Kenzie Academy Brasil.

O objetivo desse projeto era desenvolver um uma API que gerencia filmes e compras de filmes.

## Instalação dos pacotes de teste

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```

5. Vá até o arquivo `pytest.ini` e modifique o nome do projeto `my_project_name.settings` para o nome do **seu_projeto**.settings (onde se encontra o settings.py)

4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```
