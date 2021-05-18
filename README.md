# webscraping_python

# Web Scraping

* 1. Pegar o conteúdo HTLM a partir da URL
* 2. Parsear o conteudo HTML por meio do BeaultifulSoup
* 3. Estruturar o conteúdo em um Data Frame - Pandas
* 4. Transformar os dados em um dicionário de dados proprio
* 5. Converter e salvar em um arquivo JSON

```
Existem algumas coisas que você precisa considerar a seguir:

Ao usar o Selenium para automação, o uso time.sleep(secs)sem nenhuma condição específica para alcançar derrota o propósito de automação e deve ser evitado a qualquer custo. Conforme a documentação:
time.sleep(secs)suspende a execução do thread atual por um determinado número de segundos. O argumento pode ser um número de ponto flutuante para indicar um tempo de sono mais preciso. O tempo de suspensão real pode ser menor do que o solicitado porque qualquer sinal capturado encerrará o sleep () após a execução da rotina de captura desse sinal. Além disso, o tempo de suspensão pode ser maior do que o solicitado por um valor arbitrário devido ao agendamento de outra atividade no sistema.

https://docs.python.org/2/library/time.html#time.sleep

```