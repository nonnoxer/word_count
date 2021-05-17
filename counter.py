import docx
import re

def count_words(filename, regex):
    doc = docx.Document(filename)
    words = 0

    for para in doc.paragraphs:
        print(para.style.name)
        if para.style.name.find('Normal') != -1:
            if not (para.paragraph_format.first_line_indent is not None and para.paragraph_format.first_line_indent < 0):
                text = para.text
                cleantext = ''
                itcs = [(i.span()) for i in re.finditer(regex, text)]
                for i in itcs:
                    words -= len(para.text[i[0]:i[1]].split(' '))
                words += len(para.text.split(' '))

    return words