import sys
import argparse
import random
from openpyxl import load_workbook


def subwords(inputfilename, sheetname):
    #loading the inputfile
    workbook = load_workbook(filename=inputfilename, read_only=True)

    #check the sheetname parameter
    if sheetname is not None:
        sheet = workbook.get_sheet_by_name(name=sheetname)
    else:
        sheet = workbook.active

    #list for the results
    results = list()
    #iterating through the rows expect the first row(it contains the category names)
    for row in sheet.iter_rows(row_offset=1):
        #iterating through each cell in the row
        for cell in row:
            if cell.value is None:
                # skip empty cells
                continue
            #calculate category
            category =  str(cell.column)
                    #ws.cell(cell.column + '1').value
                    #a)category
                    #b)type of subword
                    #c)number of subwords
                    #d)the correct full word
                    #e)the sub words
                    #example: a)/b)/c)/d)/e);
            word = cell.value
            for i in range(0,8):
                #check the length and the number of subwords, shorter words has lesser subwords
                if i == 4 and len(word) <= 7:
                    break;
                if i == 5 and len(word) <= 9:
                    break;
                if i == 6 and len(word) <= 11:
                    break;
                if i == 7 and len(word) <= 13:
                    break;
                #creating the subwords
                if i == 0:
                    subwords = "/" + word[:len(word)//2] + "/"  + word[len(word)//2:]
                elif i == 1:
                    if len(word) <= 3:
                        continue;
                    leng = len(word)//3
                    #all part of word are same long
                    if len(word) % 3 == 0:
                        subwords = "/" + word[0:leng] + "/"  + word[leng:leng*2] + "/"  + word[leng*2:]
                    #different long parts
                    else:
                        leng = round(len(word)/3.0)
                        shorterleng = len(word) - 2* leng
                        #place the shorter substring randomly
                        place = random.randint(1, 4)
                        if place == 1:
                            subwords = "/" + word[0:leng] + "/"  + word[leng:leng*2] + "/"  + word[leng*2:]
                        elif place == 2:
                            subwords = "/" + word[0:leng] + "/"  + word[leng:leng+shorterleng] + "/"  + word[leng+shorterleng:]
                        else:
                            subwords = "/" + word[0:shorterleng] + "/"  + word[shorterleng:leng+shorterleng] + "/"  + word[leng+shorterleng:]
                elif i == 2:
                    subs=list(word)
                    for j in range(0, len(subs)):
                        subwords = subwords + "/"  + subs[j]
                elif i == 3:
                    subs = [word[k:k+2] for k in range(0, len(word), 2)]
                    for j in range(0, len(subs)):
                        subwords = subwords + "/"  + subs[j]
                else:
                    count = 0
                    for k in range(0,i-1):
                        sep =random.randint(1, len(word)- i - count +k)
                        subwords = subwords + "/"  + word[count:count+sep]
                        count = count +sep
                    subwords = subwords + "/"  + word[count:]

                result = category + "/" + str(i+1) + "/" + str(sum(c=="/" for c in subwords)) + "/" + str(len(word)) + "/" + word + subwords + ";"
                subwords =  ""
                #add to result list
                results.append((result, int(category)))
    return results


def save_results(results, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        #sort by category, it would be easier if iterating through cells, not rows, but openpyxl has not iter_cell function
        results = sorted(results, key=lambda student: student[1])
        #save the results
        for i in range(0,len(results)):
            print(results[i][0], file=f)
    print('Creating subwords has finished. Saved result to {}'.format(filename))


parser = argparse.ArgumentParser(description='Generate subwords from input XLS sheet')
parser.add_argument('input', help='The XLSX file containing all the words')
parser.add_argument('--sheet', default=None, help='The name of the sheet within input file')
parser.add_argument('--out', default='results.txt', help='The name of the file where results are saved')

if __name__ == '__main__':

    args = parser.parse_args()
    results = subwords(args.input, args.sheet)
    save_results(results, args.out)
