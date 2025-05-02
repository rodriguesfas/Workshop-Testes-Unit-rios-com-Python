# Aula: Testes Unitários com Python

Este repositório contém os exemplos utilizados na aula introdutória sobre testes unitários em Python. A aula abrange testes de funções, models, controllers e rotas com FastAPI.

## Estrutura

- `calculadora.py`: Funções simples
- `models.py`: Exemplo de model com classe `User`
- `controllers.py`: Exemplo de lógica de controle
- `app.py`: Aplicação FastAPI simples
- `test_*.py`: Arquivos de teste com `unittest` e `TestClient`

## Como executar os testes

```bash
# Testes com unittest
python test_calculadora.py
python test_models.py
python test_controllers.py

# Testes FastAPI
pip install fastapi uvicorn pytest
pytest test_app.py

# Cobertura de testes (opcional)
pip install coverage
coverage run -m unittest discover
coverage report
```
