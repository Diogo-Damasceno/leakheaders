# header-leak

Detecta vazamento de headers sensíveis (Server, X-Powered-By).

> **Aviso etico:** ferramenta exclusiva para fins educacionais e testes em
> ambientes que voce possui ou tem autorizacao para auditar. Categoria:
> Defensiva. Nunca a use contra terceiros.

## Instalacao

```bash
git clone https://github.com/Diogo-Damasceno/header-leak.git
cd header-leak
python3 -m venv .venv && . .venv/bin/activate
pip install -e .
```

## Uso

Identifique fingerprinting em suas respostas.

Exemplos reais:

```
  $ header-leak headers.txt
  server-leak: 1```

## Arquitetura

`src/header_leak/core.py` tem a logica pura (funcoes testaveis); `cli.py` e a
casca de argumentos. Testes em `tests/` cobrem os casos principais.
