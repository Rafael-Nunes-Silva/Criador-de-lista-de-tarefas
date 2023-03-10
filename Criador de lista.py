import os
import glob

address = input("Insira o nome da pasta em que se encontram os exercicios: ")

outputContent = ""

for fileAddress in glob.glob(f"{address}/*.py"):
    fileName = fileAddress[len(address)+1: len(fileAddress)-3]
    fileContent = open(fileAddress, "r").read()
    outputContent += f"{fileName}:\n{fileContent}\n\n"

outputFile = open(f"{address}.txt", "w")
outputFile.write(outputContent)
outputFile.close()
