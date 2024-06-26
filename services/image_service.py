from PIL import Image
import pytesseract

def extract_table_structure_from_image(image: Image.Image) -> str:
    text = pytesseract.image_to_string(image)
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]

    if len(lines) < 2:
        return None

    headers = lines[0].split()
    rows = [line.split() for line in lines[1:]]

    def guess_data_type(values):
        for value in values:
            if not value.isdigit():
                return "VARCHAR(255)"
        return "INT"

    column_defs = []
    for header in headers:
        values = [row[headers.index(header)] for row in rows if len(row) > headers.index(header)]
        data_type = guess_data_type(values)
        column_defs.append(f"{header} {data_type}")

    table_structure = ", ".join(column_defs)
    return table_structure
