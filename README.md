# leakheaders

Detecta vazamento de headers sensíveis (Server, X-Powered-By).

## O que faz

Esta ferramenta de **defensiva** contra alvos que voce possui ou tem autorizacao. Detecta vazamento de headers sensíveis (Server, X-Powered-By). O codigo e
testavel localmente (sem dependencias de rede para os testes unitarios).

> **Aviso etico:** uso exclusivo para fins educacionais e testes em ambientes
> que voce **possui** ou tem **autorizacao expressa** para auditar. Nunca a
> utilize contra sistemas de terceiros. O autor nao se responsabiliza por uso
> indevido.

## Instalacao

```bash
git clone https://github.com/Diogo-Damasceno/leakheaders.git
cd leakheaders
python3 -m venv .venv && . .venv/bin/activate
pip install -e .
```

## Uso

Identifique fingerprinting em suas respostas.

## Exemplos reais

```bash
$ header-leak headers.txt
# server-leak: 1
```

## Como funciona (resumo)

O modulo principal implementa a logica em funcoes puras e testaveis; a CLI e
apenas a casca de argumentos. Os testes em `tests/` (Python) ou `CoreTest.java`
(Java) cobrem os casos principais e rodam offline.

## O que NAO faz

- Nao executa ataques contra terceiros.
- Nao exfiltra dados.
- Nao substitui uma solucao comercial de seguranca.

## Licenca

MIT — ver `LICENSE`.
