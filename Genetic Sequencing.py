

#                                   RNA Codon Translation
#               |||U|||             |||C|||             |||A|||             |||G|||
#           UUU - Phe    UCU - Ser    UAU - Tyr    UGU - Cys    |||U|||
# |||U|||   UUC - Phe    UCC - Ser    UAC - Tyr    UGC - Cys    |||C|||    
#           UUA - Leu    UCA - Ser    UAA - Stop   UGA - Trp    |||A|||
#           UUG - Leu    UCG - Ser    UAG - Stop  UGG - Trp    |||G|||
#
#           CUU - Leu     CCU - Pro    CAU - His    CGU - Arg    |||U|||
# |||C|||   CUC - Leu     CCC - Pro    CAC - His    CGC - Arg    |||C|||
#           CUA - Leu     CCA - Pro    CAA - Gin    CGA - Arg    |||A|||
#           CUG - Leu     CCG - Pro    CAG - Gin   CGG - Arg    |||G|||
#
#           AUU - Ile       ACU - Thr    AAU - Asn   AGU - Ser     |||U|||
# |||A|||   AUC - Ile       ACC - Thr    AAC - Asn   AGC - Ser     |||C|||
#           AUA - Met    ACA - Thr    AAA - Lys    AGA - Stop   |||A|||
#           AUG - Met    ACG - Thr    AAG - Lys   AGG - Stop   |||G|||
#
#           GUU - Val      GCU - Ala    GAU - Asp   GGU - Gly    |||U|||
# |||G|||   GUC - Val      GCC - Ala    GAX - Asp   GGC - Gly    |||C|||
#           GUA - Val      GCA - Ala    GAA - Glu    GGA - Gly    |||A|||
#           GUG - Val      GCG - Ala    GAG - Glu    GGG - Gly   |||G|||

from turtle import *

def geneticSequencingParser(Text_File):
    """Takes a fasta file with nucleotide sequencing and opens the file. Then it separates the title, location and genetic sequence that is given from the file."""
    Title = []
    Location = []
    Genetic_Sequence = []
    Trigger = False
    try:
        File = open(Text_File)
        Content = File.read()
        Split_Content = Content.replace(",", "").split("\n")
    except:
        print ("Invaid File Type")
    for item in Split_Content:
        if ">" in item:
            Title.append(item)
        else:
            Genetic_Sequence.append(item)
    Sequence = "".join(Genetic_Sequence)
    for item in Title:
        Split_Item = "".join(item).replace(":","").split(" ")
        if "country" in Split_Item:
            Index = Split_Item.index("country")
            Location.append(Split_Item[Index:])
            Title.append(Split_Item[:Index])
    return Genetic_Sequence, Location, Title
    
    
def RNA_Sequencing(Genetic_Sequence):
    """Uses a DNA sequence then finds and returns its RNA complement""" 
    RNA_Bases = []
    for base in Genetic_Sequence:
        if base == "A":
            RNA_Bases.append("U")
        elif base == "T":
            RNA_Bases.append("A")
        elif base == "C":
            RNA_Bases.append("G")
        elif base == "G":
            RNA_Bases.append("C")
    return RNA_Bases


def DNA_Graphics(RNA_Sequence, DNA_Sequence):
    """Creates a visual of DNA and RNA connection using Turtle module"""
    canvas = Screen()
    canvas.setup(1200 , 800)
#RNA
    RNA = Turtle()
    RNA.pensize(4)
    RNA.penup()
    RNA.speed("fastest")
    RNA.goto(- 750, -200)
    RNA.pendown()
    RNA.pencolor("blue")
    RNA.forward(1500)
    RNA_Base_Position = 1500/len(RNA_Sequence)
    RNA_Position = -750
    RNA.pensize(2)
    for base in RNA_Sequence:
        RNA_Position += RNA_Base_Position
        RNA.penup()
        RNA.goto(RNA_Position, -200)
        RNA.pendown()
        if base == "U":
            RNA.pencolor("purple")
            RNA.setheading(90)
            RNA.forward(300)
        elif base == "A":
            RNA.pencolor("Green")
            RNA.setheading(90)
            RNA.forward(150)
        elif base == "G":
            RNA.pencolor("red")
            RNA.setheading(90)
            RNA.forward(200)
        elif base == "C":
            RNA.pencolor("yellow")
            RNA.setheading(90)
            RNA.forward(350)
# DNA
    DNA = Turtle()
    DNA.pensize(4)
    DNA.penup()
    DNA.speed("fastest")
    DNA.goto(-750, 200)
    DNA.pendown()
    DNA.pencolor("blue")
    DNA.forward(1500)
    DNA_Base_Position = 1500/len(DNA_Sequence)
    DNA_Position = -750
    DNA.pensize(2)
    for base in DNA_Sequence:
        DNA_Position += DNA_Base_Position
        DNA.penup()
        DNA.goto(DNA_Position, 200)
        DNA.pendown()
        if base == "T":
            DNA.pencolor("Gray")
            DNA.setheading(270)
            DNA.forward(250)
        elif base == "A":
            DNA.pencolor("Green")
            DNA.setheading(270)
            DNA.forward(100)
        elif base == "G":
            DNA.pencolor("red")
            DNA.setheading(270)
            DNA.forward(50)
        elif base == "C":
            DNA.pencolor("yellow")
            DNA.setheading(270)
            DNA.forward(200)
    print (canvas)


def Codon_Translation(RNA_Sequence):
    Codons = []
    count = 0
    Temp = []
    for base in RNA_Sequence:
        Temp.append(base)
        count += 1
        if count == 3 and "".join(Temp) == "UUU":
            Codons.append("PHE")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UUC":
            Codons.append("PHE")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UUA":
            Codons.append("LEU")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UUG":
            Codons.append("LEU")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "UCU":
            Codons.append("SER")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UCC":
            Codons.append("SER")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UCA":
            Codons.append("SER")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UCG":
            Codons.append("SER")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "UAU":
            Codons.append("TYR")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UAC":
            Codons.append("TYR")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UAA":
            Codons.append("STOP")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UAG":
            Codons.append("STOP")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "UGU":
            Codons.append("CYS")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UGC":
            Codons.append("CYS")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UGA":
            Codons.append("STOP")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "UGG":
            Codons.append("TRP")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "CUU":
            Codons.append("LEU")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CUC":
            Codons.append("LEU")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CUA":
            Codons.append("LEU")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CUG":
            Codons.append("LEU")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "CCU":
            Codons.append("PRO")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CCC":
            Codons.append("PRO")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CCA":
            Codons.append("PRO")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CCG":
            Codons.append("PRO")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "CAU":
            Codons.append("HIS")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CAC":
            Codons.append("HIS")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CAA":
            Codons.append("GLN")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CAG":
            Codons.append("GLN")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "CGU":
            Codons.append("ARG")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CGC":
            Codons.append("ARG")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CGA":
            Codons.append("ARG")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "CGG":
            Codons.append("ARG")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "AUU":
            Codons.append("ILE")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AUC":
            Codons.append("ILE")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AUA":
            Codons.append("ILE")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AUG":
            Codons.append("MET")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "ACU":
            Codons.append("THR")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "ACC":
            Codons.append("THR")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "ACA":
            Codons.append("THR")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "ACG":
            Codons.append("THR")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "AAU":
            Codons.append("ASN")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AAC":
            Codons.append("ASN")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AAA":
            Codons.append("LYS")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AAG":
            Codons.append("LYS")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "AGU":
            Codons.append("SER")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AGC":
            Codons.append("SER")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AGA":
            Codons.append("ARG")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "AGG":
            Codons.append("ARG")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "GUU":
            Codons.append("VAL")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GUC":
            Codons.append("VAL")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GUA":
            Codons.append("VAL")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GUG":
            Codons.append("VAL")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "GCU":
            Codons.append("ALA")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GCC":
            Codons.append("ALA")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GCA":
            Codons.append("ALA")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GCG":
            Codons.append("ALA")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "GAU":
            Codons.append("ASP")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GAC":
            Codons.append("ASP")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GAA":
            Codons.append("GLU")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GAG":
            Codons.append("GLU")
            del Temp[:]
            count = 0
            
        elif count == 3 and "".join(Temp) == "GGU":
            Codons.append("GLY")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GGC":
            Codons.append("GLY")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GGA":
            Codons.append("GLY")
            del Temp[:]
            count = 0
        elif count == 3 and "".join(Temp) == "GGG":
            Codons.append("GLY")
            del Temp[:]
            count = 0
    return Codons


def main():
    try:
        File = input("Enter File Name Here: ")
        Out_Put = geneticSequencingParser(File)
    except:
        print ("Invaild File Type or File Not Found")
    Genetic_Sequence = "".join(Out_Put[0]).replace(",","")
    RNA_Sequence = "".join(RNA_Sequencing(Genetic_Sequence))
    print ("This is DNA: {}".format(Genetic_Sequence))
    print ("This is RNA: {}".format(RNA_Sequence))
    DNA_Graphics(RNA_Sequence, Genetic_Sequence)
    #print (Codon_Translation(RNA_Sequence))









