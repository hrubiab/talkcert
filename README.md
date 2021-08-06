# talkcert

O **talkcert** é uma ferramenta CLI simples para geração de certificados para o Comptalk, evento promovido por alunos extensionistas da Universidade Federal do Espírito Santo (UFES).

## Requisitos

* Python >=3.8
* wkhtmltopdf

## Instalação

Para rodar a ferramenta, você precisará instalar o wkhtmltopdf. Procure qual a melhor maneira de instalação do pacote no seu sistema operacional. No Ubuntu e Debian, o seguinte comando pode ser usado:

```bash
$ sudo apt install wkhtmltopdf
```

Instale as dependências necessárias para rodar a aplicação:

```bash
$ pip install -r requirements.txt
```

Configure a ferramenta de acordo com suas preferências no arquivo ```config.json```. Um exemplo está disponpivel em ```config.example.json```.

Rode a aplicação com:

```bash
$ python3.8 talkcert.py -h
```

Ou, se preferir:
```bash
$ sudo chmod +x talkcert.py
$ ./talkcert.py -h
```
## Uso
Crie um arquivo qualquer contendo uma lista de pessoas, uma por linha, para as quais devem ser emitidos os certificados. Na versão atual, o seguinte formato precisa ser seguido:

```<matricula> <horas> <categoria> <nome completo>```

Exemplo:
```
2021201122 10 ouvinte Marcos de Souza
2021201123 10 ouvinte Gabriela Marques
2021201124 10 ouvinte Junior Silva
2021201125 10 organizadora Luisa Albuquerque
```

Etc.

Será criado um arquivo PDF em ```cert/``` para cada uma das pessoas especificadas no arquivo, seguindo o nome da pessoa.

Para executar:
```bash
$ ./talkcert.py arquivo.txt
```

## Extensibilidade
A ferramenta irá gerar certificados utilizando o modelo em ```talkcert/templ/cert.html```. Todos os campos em ```config.json``` são acessíveis dentro do arquivo de modelo dos certificados usando chaves espaçadas (exemplo: ```{ data_inicio }```). Além dos campos da configuração, você também pode utilizar as seguintes variáveis de template:
* ```{ nome }``` - O nome da pessoa para quem o certificado será emitido.
* ```{ categoria }``` - A categoria em que a pessoa participou do evento (ex.: ouvinte, organizador(a)).
* ```{ matricula }``` - O número de matricula da pessoa sendo certificada.
* ```{ horas }``` - As horas contabilizadas no certificado.

## Autor
* Carlos Henrique Rubia Barbosa \<carlos.h.barbosa@edu.ufes.br>

## Agradecimentos & Créditos
* Kethlen Correia de Jesus \<kethlen.correia@edu.ufes.br> pelo modelo dos certificados e as artes utilizadas.
* Nicolas Walcker de Miranda \<nicolas.miranda@edu.ufes.br> pela estilização e conversão do modelo em template HTML e CSS.