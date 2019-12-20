from Bio import SeqIO
from glob import glob
dirList = glob(
    "/home/labs/binford/Assembled_Untranslated_Transcriptomes/*.fasta")
with open("combinedTranscriptomes.fasta", "w") as myFile:
    for dir in dirList:
        with open(dir, "rU") as handle:
            piece = dir.split("/")[-1].split("_")[0]
            print(piece)
            for record in SeqIO.parse(handle, "fasta"):
                sequence = str(record.seq)
                marker = str(record.id+"_"+piece)
                myFile.write(">"+marker+"\n"+sequence+"\n")
