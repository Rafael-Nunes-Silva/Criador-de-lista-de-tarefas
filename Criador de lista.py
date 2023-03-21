import glob
import re

def SortFiles(files):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(files, key=alphanum_key)

address = input("Insira o caminho da pasta em que se encontram os exercicios('lista 1' ou 'minhas listas/lista 2'): ")
extension = input("Insira a extensão dos arquivos de exercicios(py): ")
exceptions = input("Insira os nomes(sem extensão) dos arquivos que devem ser ignorados(separados por ','): ").split(",")

outputContent = ""

for fileAddress in SortFiles(glob.glob(f"{address}/*{extension}")):
    fileName = fileAddress[len(address)+1: len(fileAddress)-(len(extension)+1)]
    if fileName in exceptions:
        continue
    fileContent = open(fileAddress, "r").read()
    outputContent += f"{fileName}:\n{fileContent}\n\n"

outputFile = open(f"{address}.txt", "w")
outputFile.write(outputContent)
outputFile.close()
