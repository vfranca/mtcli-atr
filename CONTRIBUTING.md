Contribuindo para o mtcli-atr

Obrigado por considerar contribuir com este plugin! Aqui estão instruções para colaborar.

---

Instalação para desenvolvimento

bash
git clone https://github.com/seu-usuario/mtcli-atr.git
cd mtcli-atr
poetry install


---

Executando os testes

Execute todos os testes automatizados com:

bash
poetry run pytest


---

Estrutura do Projeto

- plugin.py: comando CLI com Click  
- atr.py: lógica do cálculo do ATR  
- conf.py: configuração do plugin (valores padrão, etc.)  
- tests/: testes automatizados com pytest  

---

Boas práticas

- Escreva testes para novas funcionalidades.  
- Use docstrings nas funções e módulos.  
- Mantenha commits claros e descritivos.  
- Siga o estilo de código do projeto para manter consistência.  

---

Publicação (mantenedores)

Para publicar nova versão no PyPI (caso você seja mantenedor):

bash
poetry build
poetry publish


Certifique-se de ajustar a versão no pyproject.toml.

---
Sinta-se à vontade para abrir issues ou enviar pull requests. Toda colaboração é muito bem‑vinda!
