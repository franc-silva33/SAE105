# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:43:20 2023

@author: IZAK LA MERDE
"""

import re
import csv

ssh33= " "

with open("/Users/francisco/Desktop/tramess.txt", "r") as f:
    compteur_http = 0
    compteur_https = 0
    compteur_domaine = 0
    compteur_ssh = 0  
    compteur_icmp = 0
    compteur = 0
    tab = [0]*60
    for line in f:
        match = re.search(r"\d{2}:\d{2}:\d{2}", line)
        if match:
            tab[int(line[6]+line[7])]+=1
            if 'http >' in line:
                compteur_http = compteur_http + 1
            if '.domain' in line:
                compteur_domaine = compteur_domaine + 1
            if 'ssh' in line:
                compteur_ssh = compteur_ssh +1
            if 'https' in line:
                compteur_https = compteur_https + 1
            if 'ICMP' in line:
                compteur_icmp = compteur_icmp + 1
    print (tab)

    
    evenement = ssh33+str(compteur_ssh)
    
    with open("izak.csv",'w') as file:
        fieldnames = ["secondes","nb de trame"]
        writer =csv.DictWriter(file, delimiter = ";", fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(tab)):
            if tab[i] > 183:
                writer.writerow({"secondes" : i, "nb de trame": tab[i]})
        file.close()
                    
    
    
    
    print("Le protocol et le nombre de trames associÃ©es:")
    print('ssh:',compteur_ssh)
    print("http:",compteur_http)
    print("https:",compteur_https)
    print("dns:",compteur_domaine)
    print("icmp:",compteur_icmp)