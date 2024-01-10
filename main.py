import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.pdfgen import canvas
import pdfkit
from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from email_module import send_email
from html_module import generate_html


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
#################################Login_Page####################################
def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
    elif(uname == "radeel" and password == "123"):
 
        messagebox.showinfo("","Login Success")
        root.filename=filedialog.askopenfilename(initialdir="C:/Users/HP/Desktop",title="sélectionner votre fichier CSV",filetypes=(("csv files","*.csv"),))
        root.destroy()
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")
 
 
root = Tk()
root.title("Login")
root.iconbitmap('C:/Users/HP/Desktop/Projet/radeelLogo.ico')
root.geometry("1062x700")
bg = PhotoImage(file="C:/Users/HP/Desktop/Projet/radeelCentre.png")
my_label = Label(root, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
global e1
global e2
 
Label(root, text="UserName").place(x=310, y=310)
Label(root, text="Password").place(x=310, y=340)
 
e1 = Entry(root)
e1.place(x=440, y=310)
 
e2 = Entry(root)
e2.place(x=440, y=340)
e2.config(show="*")
 
 
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=410, y=400)


 
root.mainloop()


####################################################################################



today=date.today()

with open(root.filename,'r')as csvfile:
    reader=csv.reader(csvfile,delimiter = ";")
    next(reader)
    for line in reader:
        print(line[6])
        MOI=numbers_to_strings(int(line[14]))
        



################generate the email
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
#################################################################################
        
        my_email = 'radeel.service@gmail.com'
        my_email_password = 'radeelservice1234'
        client_email =  line[8]

        message = MIMEMultipart()
        message['From'] = my_email
        message['To'] = client_email
        message['Subject'] = "Facture d'Eau et d'Életricité"
##################################################################################
        if not (line[21]=="0" and line[22]=="0" and line[23]=="0" and line[24]=="0"):
          totTR2="<tr> <td> tr2 </td> <td> "+str(line[21])+" </td> <td> "+str(line[22])+"</td> <td> "+str(line[23])+"</td> <td>  14%</td> <td> "+str(line[24])+" </td> </tr>"
        else:
          totTR2=""
        if not (line[25]=="0" and line[26]=="0" and line[27]=="0" and line[28]=="0"):
          totTR3="<tr> <td> tr2 </td> <td> "+str(line[25])+" </td> <td> "+str(line[26])+"</td> <td> "+str(line[27])+"</td> <td>  14%</td> <td> "+str(line[28])+" </td> </tr>"
        else:
          totTR3=""
        if not (line[29]=="0" and line[30]=="0" and line[31]=="0" and line[32]=="0"):
          totTR4="<tr> <td> tr2 </td> <td> "+str(line[29])+" </td> <td> "+str(line[30])+"</td> <td> "+str(line[31])+"</td> <td>  14%</td> <td> "+str(line[32])+" </td> </tr>"
        else:
          totTR4=""
        if not (line[33]=="0" and line[34]=="0" and line[35]=="0" and line[36]=="0"):
          totTR5="<tr> <td> tr2 </td> <td> "+str(line[33])+" </td> <td> "+str(line[34])+"</td> <td> "+str(line[35])+"</td> <td>  14%</td> <td> "+str(line[36])+" </td> </tr>"
        else:
          totTR5=""
        if not (line[37]=="0" and line[38]=="0" and line[39]=="0" and line[40]=="0"):
          totTR6="<tr> <td> tr2 </td> <td> "+str(line[37])+" </td> <td> "+str(line[38])+"</td> <td> "+str(line[39])+"</td> <td>  14%</td> <td> "+str(line[40])+" </td> </tr>"
        else:
          totTR6=""

##################################################################################
        

        bill_Cont = """\
        <HTML>
           <HEAD>
           
                 <TITLE> Facture</TITLE>
                 
                 <link rel="stylesheet"  href="style.css">
           </HEAD>
                 <BODY> 
                 
                 <p>
                  <img src="radeelLogo.png" alt="photo du logo de LARADEEL" style="float: left;" />
                  <img src="radeelLogo.png" alt="photo du logo de LARADEEL" style="float: right;" />
                  </p>
                  <br/><br/><br/><br/><br/>
                  <table class="centerHeader" >
                        <tr>
                          <td>Facture N°</td>
                          <td>:  test</td>
                        </tr>
                        <tr>
                          <td>Editee le</td>
                          <td>:  {today}</td>
                        </tr>
                        <tr>
                          <td> Periode de facturation</td>
                          <td>:  {MOI}-{ANN}</td>
                        </tr>
                    </table>
                      <br/><br/><br/><br/>
                      <table class="content-table" style="float: left;">
                      <thead>
                        <tr>
                          <td>Usage</td>
                          <th colspan="2" >{USAGE}</th>
                          
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>Ancien Index</td>
                          <td>Nouvel Index</td>
                          <td>Consommation</td>
                        </tr>      
                        <tr>
                          <td>{INDEX1}</td>
                          <td>{INDEX2_VALIDER}</td>
                          <td>{CONSOMMATION_TOTAL}</td>
                        </tr>
                        <tr>
                          <td>Date ancien index</td>
                          <td>Date Nouvel index</td>
                          <td>Nbre jours</td>
                        </tr>
                        <tr>
                          <td>{DATE_INDEX_1}</td>
                          <td>{DATE_INDEX2}</td>
                          <td>{NBJ}</td>
                        </tr>

                  
                      </tbody>
                    </table>  
                     <table class="content-table" style="float: right;" >
                      <thead>
                        <tr>
                          <th>Tournee</th>
                          <th> {NUM_LOC}/{NUM_SEC}/{NUM_TRN}/{NUM_ORD}</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>Client</td>
                          <td> {NOM}</td>
                        </tr>
                        <tr>
                          <td>Adresse</td>
                          <td>{ADRESSE_CONSOMMATION}</td>
                        </tr>
                        <tr>
                          <td>N* de Centrat</td>
                          <td>{NUM_POL}</td>
                        </tr>
                      </tbody>
                    </table>
                     <br/>          
                  <table class="content-table center" >
                      <thead>
                       <tr>
                        <td></td>
                        <td></td>
                        <td> Désignation </td>
                        <td></td>
                        <td></td>
                        <td></td>
                       </tr>
                       </thead>
                       <tbody>
                       <tr>
                       <td> Eléments detail </td>
                       <td> Consomation </td>
                       <td>Prix unitaire </td>
                       <td>Montant ht </td>
                       <td>TVA taux</td>
                       <td>TVA mantant</td>
                       </tr>
                       <tr>
                       <th colspan="6"> Redevaces de la consommation </th>
                       </tr>
                       <tr>
                       <td> tr1 </td>
                       <td> {TR1} </td>
                       <td> {PR1}</td>
                       <td> {MT1}</td>
                       <td>  14%</td>
                       <td> {TVA1} </td>
                       </tr>
                       {totTR2}
                       {totTR3}
                       {totTR4}
                       {totTR5}
                       {totTR6}
                        <tr>
                       <th colspan="6"> Redevaces fixes</th>
                       </tr>
                      <tr>
                       <td colspan="3"> Taxes Entretiens </td>
                       <td> {MONTANT_TEC}</td>
                       <td> 20% </td>
                       <td> {TVA_TEC} </td>
                       </tr>
                      <tr>
                       <td colspan="3"> Taxes Locations </td>
                       <td>  {MONTANT_TLC} </td>
                       <td>   7% </td>
                       <td> {TVA_TLC} </td>
                      </tr>
                      
                      <tr>
                        <th>   </th>
                        <td colspan="2">Total HT (en DH) </td>
                        <td>    {MONTANT_FACTURE_HT}   </td>
                       <td colspan="2"> </td>
                     </tr>
                     <tr>
                        <th>   </th>
                        <td colspan="2">Total TVA (en DH) </td>
                        <td>    {TVA}   </td>
                       <td colspan="2"> </td>
                     </tr> 
                     <tr>
                        <th>   </th>
                        <td colspan="2">TPPAN (en DH) </td>
                        <td>    {TPPAN}   </td>
                       <td colspan="2"> </td>
                     </tr> 
                     <tr>
                        <th>   </th>
                        <td colspan="2">Timbre fiscal (en DH) </td>
                        <td>    {TF}   </td>
                       <td colspan="2"> </td>
                     </tr> 
                     <tr>
                        <th>   </th>
                        <th colspan="2">Montant a payer(en DH)</th>
                        <th>    {NET}   </th>
                       <td colspan="2"> </td>
                     </tr> 
                     </tbody>
                    
                  </BODY>
        </HTML>
        """.format(totTR2=totTR2,totTR3=totTR3,totTR4=totTR4,totTR5=totTR5,totTR6=totTR6,NUM_LOC=line[0],NUM_SEC=line[1],NUM_TRN=line[2],NUM_ORD=line[3],NUM_POL=line[4],CAT=line[5],NOM=line[6],ADRESSE_CONSOMMATION=line[7],ADRESSE_MAIL=line[8],USAGE=line[9],NUMERO_COMPTEUR=line[10],COD_BANQUE=line[11],INDEX1=line[12],INDEX2_VALIDER=line[13],MOI=line[14],ANN=line[15],CONSOMMATION_TOTAL=line[16],TR1=line[17],PR1=line[18],MT1=line[19],TVA1=line[20],TR2=line[21],PR2=line[22],MT2=line[23],TVA2=line[24],TR3=line[25],PR3=line[26],MT3=line[27],TVA3=line[28],TR4=line[29],PR4=line[30],MT4=line[31],TVA4=line[32],TR5=line[33],PR5=line[34],MT5=line[35],TVA5=line[36],TR6=line[37],PR6=line[38],MT6=line[39],TVA6=line[40],GUICH=line[41],MNT_CONS=line[42],TF=line[43],TPPAN=line[44],TVA=line[45],MONTANT_TEC=line[46],TVA_TEC=line[47],MONTANT_TLC=line[48],TVA_TLC=line[49],TAXES=line[50],TVA_TAXES=line[51],MONTANT_FACTURE_HT=line[52],NET=line[53],NBF=line[54],DAT_PAIE=line[55],AGENCE=line[56],BON=line[57],TVA_BON=line[58],DATE_INDEX_1=line[59],DATE_INDEX2=line[60],NBJ=line[61],today=today)


        pdfFileHtml=open("test1.html","w")
        pdfFileHtml.write(bill_Cont)
        pdfFileHtml.close()

        options = {
            'user-style-sheet': 'style.css',
            "enable-local-file-access": None
        }

        conf=pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
        pdfkit.from_file('test1.html','bill_Pdf.pdf',configuration=conf,options=options)
####################################################################################

        message.attach(MIMEText(mail_content, 'html'))
        my_bill_file = 'C:/Users/HP/Desktop/Projet/bill_Pdf.pdf'
        my_bill_file_bn = open(my_bill_file, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name="Facture.pdf")
        payload.set_payload((my_bill_file_bn).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment')
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(my_email, my_email_password)
        text = message.as_string()
        session.sendmail(my_email, client_email, text)
        session.quit()
        print('Mail Sent')


root = Tk()
root.title("Login")
root.iconbitmap('C:/Users/HP/Desktop/Projet/radeelLogo.ico')
root.geometry("1062x700")

messagebox.showinfo("","Emails Sent")

root.mainloop()

"""import csv
from datetime import date
from tkinter import Tk, Entry, Label, Button, PhotoImage, messagebox, filedialog
from email_module import send_email
from html_module import generate_html

def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
    elif(uname == "radeel" and password == "123"):
 
        messagebox.showinfo("","Login Success")
        root.filename=filedialog.askopenfilename(initialdir="C:/Users/HP/Desktop",title="sélectionner votre fichier CSV",filetypes=(("csv files","*.csv"),))
        root.destroy()
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")
 
 


if __name__ == "__main__":
    # Tkinter GUI code

    root = Tk()
    root.title("Login")
    root.iconbitmap('C:/Users/HP/Desktop/Projet/radeelLogo.ico')
    root.geometry("1062x700")
    bg = PhotoImage(file="C:/Users/HP/Desktop/Projet/radeelCentre.png")
    my_label = Label(root, image=bg)
    my_label.place(x=0,y=0,relwidth=1,relheight=1)
    global e1
    global e2
    
    Label(root, text="UserName").place(x=310, y=310)
    Label(root, text="Password").place(x=310, y=340)
    
    e1 = Entry(root)
    e1.place(x=440, y=310)
    
    e2 = Entry(root)
    e2.place(x=440, y=340)
    e2.config(show="*")
    
    
    Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=410, y=400)


    
    root.mainloop()"""
       

        
