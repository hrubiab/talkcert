# Talkcert (2021) Carlos Henrique Rubia Barbosa <carlos.h.barbosa@edu.ufes.br>
#
# Agradecimentos a Nicolas Walcker de Miranda e Kethlen Correia de Jesus pelos
#   modelos, HTML/CSS e imagens.

import pdfkit
import os

def makecert(appcfg, nome, matricula, categoria, horas, image):
    with open('talkcert/templ/cert.html') as file:
        model = file.read()
    
    for item in appcfg:
        if item == "organizadores":
            break
        model = model.replace("{ " + item + " }", appcfg[item])
    
    for item in appcfg['organizadores']:
        model = model.replace("{ " + item + " }", appcfg['organizadores'][item])

    model = model.replace("{ nome }", nome)
    model = model.replace("{ matricula }", matricula)
    model = model.replace("{ horas }", horas)
    model = model.replace("{ categoria }", categoria)
    model = model.replace("{ image }", image)

    return model

def certify(appcfg, people):
    for person in people:
        # parsing dos dados
        dados = person.split(' ')

        # informações do participante
        matricula = dados[0]
        horas = dados[1]
        categoria = dados[2].lower()
        nome = " ".join(dados[3::])
        nome_arquivo = "_".join(nome.split(' ')).rstrip()

        # opções de geração do PDF
        options = {
            "enable-local-file-access": None,
            'margin-top': '0in',
            'margin-right': '0in',
            'margin-bottom': '0in',
            'margin-left': '0in',
            'encoding': "UTF-8"
        }

        image = os.path.abspath('talkcert/templ/img/fundo_certificado.png')

        # geração de certificados PDF
        print("Gerando certificado para", " ".join(nome.split(' ')).rstrip() + "...")
        model = makecert(appcfg, nome, matricula, categoria, horas, image)
        pdfkit.from_string(model, "cert/" + nome_arquivo + '.pdf', options = options)