import csv

allowoed = [
' ',     
'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z',
'\'',
'ä',
'ö',
'ü',
'á',
'à',
'é',
'è',
'?',
'I',
'!',
';',
':']

with open('C:\\Users\\freim\\Downloads\\ultra_fixed.csv', 'a', encoding="utf8", newline='') as the_file:
    csv_writer = csv.writer(the_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open("C:\\Users\\freim\\Downloads\\fixed.csv", encoding="utf8") as csv_file: 
        for row in csv.reader(csv_file, delimiter=','):
            col_num = 0
            for col in row:
                if (col_num == 2):
                    col_num = 0
                    write_line = False
                    for c in col:
                        try:
                            if c in allowoed:
                                write_line = True
                        except:
                            write_line = False
                        
                    if (write_line):
                        csv_writer.writerow(row)
                else:
                    col_num = col_num + 1