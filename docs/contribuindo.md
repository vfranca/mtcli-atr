Contribuindo



Contribuições são bem-vindas! Siga as etapas abaixo:



1. Fork e clone o repositório



bash

git clone https://github.com/vfranca/mtcli-atr.git

cd mtcli-atr





2. Crie um ambiente virtual e instale as dependências



bash

python -m venv .venv

source .venv/bin/activate  # No Windows: .venvScriptsactivate

pip install -e .[dev]





3. Execute os testes



bash

pytest





4. Contribua com um novo plugin



Plugins são registrados via o sistema de entry points do mtcli. No `pyproject.toml`:



toml

[project.entry-points."mtcli.plugins"]

meu_plugin = "plugin_exemplo.plugin:plugin"





No arquivo Python:



python

def plugin():

&nbsp;   pass  # lógica do plugin





5. Envie um Pull Request



Abra um PR descrevendo claramente sua contribuição.



---



Obrigado por ajudar a melhorar este projeto!





