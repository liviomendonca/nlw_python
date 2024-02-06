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


temas:
bearded theme
atom one light theme