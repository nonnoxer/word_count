import docx
import re

def count_words(filename):
    doc = docx.Document('doc.docx')
    words = 0
    itc = '\([^()]*\, ?[0-9]*\)'

    for para in doc.paragraphs:
        if para.paragraph_format.first_line_indent is not None and para.paragraph_format.first_line_indent > 0:
            text = para.text
            cleantext = ''
            itcs = [(i.span()) for i in re.finditer(itc, text)]
            for i in itcs:
                words -= len(para.text[i[0]:i[1]].split(' '))
            words += len(para.text.split(' '))

    return words