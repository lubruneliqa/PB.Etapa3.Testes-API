## TESTE TÉCNICO PARTE 3 -- TESTE DE API

Esse repositório faz parte da etapa de avaliação para a vaga de QA e tem como objetivo avaliar os domínios em testes de API.
Os testes foram desenvolvidos utilizando a linguagem ```Python``` e o framework ```pytest```.

---

### Estrutura do projeto

O projeto conta com uma simples estrutura para rodar os testes.
- .env
- README.md
- verbs_HTTP_tests.py

A escolha por definir uma estrutura simples foi a necessidade de implementar os testes da maneira mais clara e sucinta.
O arquivo ```.env``` foi definido com a URL que todas as requisições irão realizadas, com isso, deixando a acessível e global para o projeto.
O arquivo ```README.md``` que o arquivo em questão.
O arquivos ```verbs_HTTP_tests.py``` conta com a suíte de testes para todos os verbos citados para avaliação. Nele cada teste é para um verbo com suas respectivas validações (```statusCode e JSON```).

---

### Execução do projeto

Para executar o projeto o usuário deve ter o ```python``` e suas bibliotecas atualizadas. Caso o usuário precise instalar as bibliotecas utilizadas para a execução desse projeto, segue a lista das mesmas com o comando ```pip```:

pip install os_sys
pip install pytest
pip install requests
pip install python-dotenv
pip install jsonschema

Com as bibliotecas instaladas, a execução do projeto é via terminal a partir do comando com o terminal na raiz da pasta:

pytest .\verbs_HTTP_tests.py

---