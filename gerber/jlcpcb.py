import csv

f_out = open('Frost-ESP32-top-pos_jlc.csv', "w")

with open('Frost-ESP32-top-pos.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in spamreader:
        row[0] = row[0].replace('Ref','Designator')
        row[0] = row[0].replace("PosX","Mid X")
        row[0] = row[0].replace("PosY","Mid Y")
        row[0] = row[0].replace("Rot","Rotation")
        row[0] = row[0].replace("Side","Layer")
        f_out.writelines(', '.join(row) + '\n')


f_out.close()