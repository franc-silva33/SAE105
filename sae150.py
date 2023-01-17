import re
import csv

IP_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

ssh33= " "

with open("/Users/francisco/Desktop/tramess.txt", "r") as f:
    compteur_http = 0
    compteur_https = 0
    compteur_http_final = 0
    compteur_domaine = 0
    compteur_ssh = 0  
    compteur_icmp_request = 0
    compteur_icmp_reply = 0 
    compteur_trames = 0
    compteur_ip = 0
    compteur_flag_fin = 0
    compteur_flags_push = 0
    compteur_flags_connexion = 0
    compteur_flags_SynAcK = 0
    compteur_flags_NoFlag = 0
    compteur_aa = 1
    compteur = 0 
    tab = [0]*60


    for line in f:
        match2 = re.search(r"\d{1}x\d{1}", line)
        if match2:
            compteur_aa = compteur_aa + 1 
            if compteur_aa > 4:
                print("omg")
            if compteur_aa < 4:
                print("izak")
            if match:
                compteur_aa = 1
        match = re.search(r"\d{2}:\d{2}:\d{2}", line)
        if match:
            tab[int(line[6]+line[7])]+=1
            compteur_trames = compteur_trames + 1
            if 'http' in line:
                compteur_http = compteur_http + 1
                compteur_http_final = compteur_http - compteur_https 
            if '.domain' in line:
                compteur_domaine = compteur_domaine + 1
            if 'ssh' in line:
                compteur_ssh = compteur_ssh +1
            if 'https' in line:
                compteur_https = compteur_https + 1
            if 'ICMP echo request' in line:
                compteur_icmp_request = compteur_icmp_request + 1
            if 'ICMP echo reply' in line:
                compteur_icmp_reply = compteur_icmp_reply + 1 
            if 'Flags [S]' in line:
                compteur_flags_connexion = compteur_flags_connexion +1
            if 'Flags [S.]' in line:
                compteur_flags_SynAcK = compteur_flags_SynAcK +1
            if 'Flags [F.]' in line:
                compteur_flag_fin = compteur_flag_fin +1
            if 'Flags [P.]' in line:
                compteur_flags_push = compteur_flags_push +1
            if 'Flags [.]' in line:
                compteur_flags_NoFlag = compteur_flags_NoFlag +1
            for ip in IP_pattern.findall(line):
                #print(ip)
                compteur += 1
    print (tab)

with open("au.csv",mode="w") as csvfile:
    fieldnames = ["protocole","nombre de trames"]
    writer = csv.DictWriter(csvfile , delimiter = ";", fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"protocole": "ssh" ,"nombre de trames": compteur_ssh})
    writer.writerow({"protocole": "http" ,"nombre de trames":  compteur_http_final})
    writer.writerow({"protocole": "https" ,"nombre de trames": compteur_https})
    writer.writerow({"protocole": "dns" ,"nombre de trames": compteur_domaine})
    writer.writerow({"protocole": "icmp_request" ,"nombre de trames": compteur_icmp_request})
    writer.writerow({"protocole": "icmp_reply" ,"nombre de trames": compteur_icmp_reply})

    
    fieldnames2 = ["nombre total de trames"]
    writer2 = csv.DictWriter(csvfile ,  delimiter = ";", fieldnames=fieldnames2)
    writer2.writeheader()
    writer2.writerow({"nombre total de trames": compteur_trames})

    fieldnames4 = ["secondes","nb de trame"]
    writer =csv.DictWriter(csvfile, delimiter = ";", fieldnames=fieldnames4)
    writer.writeheader()
    for i in range(len(tab)):
        if tab[i] > 183:
            writer.writerow({"secondes" : i, "nb de trame": tab[i]})
    csvfile.close()

    #fieldnames3 = ["ip source"]
    #writer3 = csv.DictWriter(csvfile ,  delimiter = ";", fieldnames=fieldnames3)
    #writer3.writeheader()
    #writer3.writerow({"ip source": ip})

print("Le protocol et le nombre de trames associées:")
print('ssh:',compteur_ssh)
print("http:",str(compteur_http_final))
print("https:",compteur_https)
print("dns:",compteur_domaine)
print("icmp request:",compteur_icmp_request)
print("icmp reply:",compteur_icmp_reply)
print("Il y a au total:",compteur_trames,"trames")
print("Il y a au total:",compteur,"IPs sniffées")
print("Il y a ",compteur_flags_connexion,'demandes de connexion.')
print("Il y a ",compteur_flags_SynAcK,"demandes de SynAck")
print("Il y a",compteur_flags_NoFlag,"No Flag Set")
print("Il y a",compteur_flags_push,"flags pushs")
print("Il y a ",compteur_flag_fin,"demandes de fin de connexion.")
print("Il y a ",compteur_flags_connexion - compteur_flag_fin,"de différence entre connexions et fin.")
print(compteur_aa)