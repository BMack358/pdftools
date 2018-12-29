import PyPDF2
# note PDFMiner does not support Python 3.x


def concat_pdf(file1, file2):

    input_files = [file1, file2]
    
    input_streams = []
    for inputfile in input_files:
        input_streams.append(open(inputfile, 'rb'))

    pdf_writer = PyPDF2.PdfFileWriter()

    for reader in map(PyPDF2.PdfFileReader, input_streams):
        for n in range(reader.getNumPages()):
            pdf_writer.addPage(reader.getPage(n))

    with open('new_concat.pdf', 'wb') as new_pdf_file:
            pdf_writer.write(new_pdf_file)

    for f in input_streams:
        f.close()


if __name__ == '__main__':
    #fname1 = 'Marriage_certificate2.pdf'
    fname1 = 'Petition for Divorce Part 3 of 3.pdf'
    fname2 = 'petition_consul.pdf'
    concat_pdf( fname1, fname2)
    print('Done')
