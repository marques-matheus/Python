from docx import Document
from docx.shared import Pt

arquivo = Document('C:\\Users\\Win\\Documents\\GitHub\\Python\\Word\\Certificado1.docx')

estilo = arquivo.styles['Normal']

for p in arquivo.paragraphs:
    if "@nome" in p.text:
        p.text = 'Matheus Marques'
        fonte = estilo.font
        fonte.name = 'Calibri (Corpo)'
        fonte.size = Pt(24)
      

arquivo.save('Matheus.docx')
