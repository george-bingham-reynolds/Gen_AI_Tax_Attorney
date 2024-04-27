from pypdf import PdfReader

def extract_full_pdf_text(filename):

    reader = PdfReader(filename) # FULL PDF OBJECT
    full_text = '' # EMPTY STRING TO APPEND EACH PAGE'S TEXT TO
    
    for page in reader.pages:

        full_text += ' ' # NOT SURE HOW SPACING WORKS - WOULD RATHER HAVE DOUBLE SPACE THAN MASHED TOGETHER WORDS

        text = page.extract_text() # INDIVIDUAL PAGE'S TEXT

        full_text += text # APPEND
    
    return full_text # RETURN ALL CONTENT