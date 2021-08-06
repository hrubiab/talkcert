#!/usr/bin/python3.8

# Talkcert (2021) Carlos Henrique Rubia Barbosa <carlos.h.barbosa@edu.ufes.br>
#
# Agradecimentos a Nicolas Walcker de Miranda e Kethlen Correia de Jesus pelos
#   modelos, HTML/CSS e imagens.

import argparse
import os
import sys
import json

from talkcert import certify

# cria o parser para o CLI
parser = argparse.ArgumentParser(description = 'Gerador simples de certificados do Comptalk')

# adiciona argumentos posicionais
parser.add_argument('Arquivo', metavar = '<arquivo>', type = str,
                    help = 'Arquivo com dados dos certificados')

# obtém os valores dos argumentos posicionais
args = parser.parse_args()
arg_arquivo = args.Arquivo

# lê as configurações para a geração dos certificados
if not os.path.isfile('config.json'):
    exit("*** Configuração não encontrada.  Copie config.example.json para config.json.")

with open('config.json', 'r') as jsonfile:
    appcfg = json.load(jsonfile)

# verifica se arquivo de dados especificado existe
if not os.path.isfile(arg_arquivo):
    sys.exit('Arquivo não encontrado.')

# obtém lista de participantes no evento
# formato: matricula horas categoria nome_completo
# exemplo: 2021201122 11 ouvinte Maria Marques
with open(arg_arquivo) as file:
    people = file.readlines()

# remove elementos em branco
people = list(filter(lambda x: x != "\n", people))

# gera PDFs dos certificados
certify(appcfg, people)