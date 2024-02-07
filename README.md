# nlw_python
Projeto da NLW da Rocketseat (trilha python)

# Config do ambiente
Configurações iniciais do ambiente de desenvolvimento

1. Instalar o virtualenv
   setar como comandos
   2. python3 -m venv .venv
   3. . .venv/bin/activate

2. Instalar pylint
   1. pip3 install pylint
   2. ativar a extensão da MS pylint
   3. pylint
      1. snake_case -> Funções, Variáveis, Métodos
      2. PascalCase -> Classes
   4. pylint --generate-rcfile > .pylintrc
   5. colocar as seguinte exceções:
      1. disable=
          C0114, # missing-module-docstring
          C0115, # missing-class-docstring
          C0116, # missing-function-docstring
          W0703, # Catching too general exception Exception

3. Instalar o pre-commit
   1. fazer as configs do pre-commit

4. Gerar o requirements.txt
   1. .venv/bin/pip3 freeze > requirements.txt
5. Instalar Flask
6. Instalar python-barcode
7. Instalar pillow

Após isso, gerar o arquivo de requirements novamente para atualizar com as novas instalações

# Vamos codar!
Os passos acima fazem parte da aula 1 mas vou dividir o projeto em si por aulas

## Aula 1
Criar e subir o server usando Flask.
Usar o barcode para receber o código e gerar o uma imagem do código de barras.

## Aula 2
Começamos a aula separando o único arquivo 'run_raw.py' que foi criado na primeira aula em uma estrutura de pastas seguindo a filosofia de arquitetura para facilitar a manutenção além de seguir as boas práticas da programação.

No arquivo 'run.py' rodamos o servidor e a opção de debug=True é um "equivalente" ao nodemon. Essa opção "ligada" fica monitorando nossos arquivos para renovar o servidor sempre que os arquivos forem alterados.

Posteriormente, implementamos tipagem http para deixar encapsulado como serão tratadas as requests e responses. E fizemos alguns testes para garantir que estava tudo funcionando.







temas:
bearded theme
atom one light theme