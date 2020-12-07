import io
from PIL import Image
import pytesseract
from wand.image import Image as wi


pdf = wi(filename ="curriculumvitae.pdf", resolution = 300)
pdfImg = pdf.convert('jpeg')

imgBlobs = []

for img in pdfImg.sequence:
    page = wi(image = img)
    imgBlobs.append(page.make_blob['jpeg'])

extracted_text = []

for imgBlob in imgBlobs:
    im = Image.open[io.BytesIO[imgBlob]]
    text = pytesseract.image_to_string[img, lang = 'eng']
    extracted_text.append(text)

print(extracted_text[0])