import pypdfium2 as pdfium
from PIL import Image

def render_pdf_page(pdf_path, page_num):
    pdf = pdfium.PdfDocument(pdf_path)
    page = pdf[page_num]
    bitmap = page.render(scale=2)
    pil_image = bitmap.to_pil()
    pil_image.show() 

if __name__ == "__main__":
    import sys
    render_pdf_page(sys.argv[1], 0)