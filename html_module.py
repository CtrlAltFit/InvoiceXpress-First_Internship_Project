from datetime import date
import pdfkit

def numbers_to_strings(argument):
    switcher = {
        1: "Janvier",       
        2: "Février",
        3: "Mars",
        4: "Avril",
        5: "Mai",
        6: "Juin",
        7: "Juillet",
        8: "Août",
        9: "Septembre",
        10: "Octobre",
        11: "Novembre",
        12: "Décembre"
    }
  
    return switcher.get(argument)

def generate_html(line, today):
        
    mail_content = """\
        <html>
          <head></head>
          <body>
            <p>Bonjour {NOM},
            </p>
            <ul>
              <li><strong>
              Vous trouverez ci-joint votre facture de votre comteur n° {NUMERO_COMPTEUR} du mois {MOI} {ANN}
              </strong></li> 
            </ul>
            <p>
        N'hésitez pas de nous contacter en cas de probleme sur :<br>
            </p>
        ✉️ email : <strong>radeel.service@gmail.com</strong><br> 
        📞 phone: <strong>+212.539.52.09.25</strong>
            <p>
        Nous vous en souhaitons bonne réception.<br>
            </p>
          </body>
        </html>
    """.format(NOM=line[6],NUMERO_COMPTEUR=line[10],MOI=MOI,ANN=line[15])

    pdfFileHtml = open("test1.html", "w")
    pdfFileHtml.write(bill_content)
    pdfFileHtml.close()

    options = {
        'user-style-sheet': 'style.css',
        "enable-local-file-access": None
    }

    conf = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
    pdfkit.from_file('test1.html', 'bill_Pdf.pdf', configuration=conf, options=options)

    return bill_content

today=date.today()

with open(root.filename,'r')as csvfile:
    reader=csv.reader(csvfile,delimiter = ";")
    next(reader)
    for line in reader:
        print(line[6])
        MOI=numbers_to_strings(int(line[14]))
