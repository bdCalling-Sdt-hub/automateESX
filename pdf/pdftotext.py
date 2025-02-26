import fitz
from config.prompt import prompt
from config.openAiClient import client
from PIL import Image, ImageEnhance, ImageFilter
import io
import json
import pytesseract

def force_ocr_on_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_text = ""

    for page_num in range(doc.page_count):
        # Render each page as an image at high DPI (e.g., 400)
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=400)
        img = Image.open(io.BytesIO(pix.tobytes()))

        # Perform OCR on the image
        ocr_text = pytesseract.image_to_string(img)
        extracted_text += ocr_text

    return extracted_text
def extract_text_from_pdf(text):
    # Extract text from all pages
    data = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt} {text}",
            }
        ],
        model="gpt-4o",
    )
  
    data = str(data.choices[0].message.content).replace("```", "").replace("json", "")
    data = json.loads(data)
    return data
