import PyPDF2,os

#this can read most PDFs as its difficult to normally turn it into plaintext
#this cannot edit the text itself of pdf due to formatting

os.chdir('C:\\Users\\Manith Adikari\\Downloads')
CVfile = open('ManithCV.pdf', 'rb') #rb ensures it reads in binary 
reader = PyPDF2.PdfFileReader(CVfile)

nopages = reader.numPages
print(nopages)

page1 = reader.getPage(0)
print(page1.extractText())


#Merging two PDF files

pdf1file = open('part1.pdf', 'rb')
pdf2file = open('part2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1file) 
reader2 = PyPDF2.PdfFileReader(pdf2file) 
writer = PyPDF2.PdfFileWriter()

#get pages from first file and add
for page in range(reader1.numPages):
    pageinput = reader1.getPage(page)
    writer.addPage(pageinput)
#repeat for second file
for page in range(reader2.numPages):
    pageinput = reader2.getPage(page)
    writer.addPage(pageinput)

outputfile = open('combined.pdf','wb')
writer.write(outputfile)
outputfile.close()
pdf1file.close()
pdf2file.close()
