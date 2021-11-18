import csv

def callSearchOwners(media):
    fh = open('relations_medias_francais.tsv',encoding='utf-8')
    reader = csv.reader(fh, delimiter = '\t')
    owners = []
    owners = searchOwners(reader, media,1, owners)
    print(media, "est controllé par : ")
    for item in owners:
        print("\t", item[0], " à ", item[1], "%")

def searchOwners(reader, media, pourcentage, owners):
    fh = open('relations_medias_francais.tsv',encoding='utf-8')
    reader = csv.reader(fh, delimiter = '\t')
    for ligne in reader:
        if ligne[3] == media:
            if isIntValid(ligne[2]):
                newPourcentage = pourcentage * (int(ligne[2]) / 100)
            else:
                print("Donnée interdite")
                break
            fh = open('relations_medias_francais.tsv',encoding='utf-8')
            reader = csv.reader(fh, delimiter = '\t')
            hasOwner = False
            for item in reader:
                if ligne[1] == item[3]:
                    hasOwner = True
            if not hasOwner:
                owners.append([ligne[1], round(newPourcentage*100, 2)])
            searchOwners(reader, ligne[1], newPourcentage,  owners)
    return owners

def isIntValid(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
callSearchOwners("Télérama")
callSearchOwners("Vice.com")