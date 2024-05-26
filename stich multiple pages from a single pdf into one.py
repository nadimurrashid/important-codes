
import os
from PyPDF2 import PdfReader, PdfWriter

def stitch_pdfs_overlapping(input_file, output_file, margin_mm=5):
    """Stitches all pages of a single PDF, overlapping cropped areas while managing content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path to the combined PDF file.
        margin_mm (int, optional): Fixed margin size in millimeters. Defaults to 5.

    Raises:
        ValueError: If the input file does not exist, is password-protected, or has only one page.
        IOError: If there are issues opening or saving files.
    """

    if not os.path.exists(input_file):
        raise ValueError(f"Input file '{input_file}' not found.")

    reader = PdfReader(input_file)

    if reader.is_encrypted:
        raise ValueError(f"Input file '{input_file}' is password-protected.")

    num_pages = len(reader.pages)

    if num_pages == 1:
        raise ValueError(f"Input file '{input_file}' already has only one page.")

    pdf_writer = PdfWriter()
    page_height_mm = reader.pages[0].mediabox.height * 10  # Use "height" attribute now
    margin_px = margin_mm * 72 / 25.4  # Convert mm to pixels
    prev_right = 0  # Track right edge of previous page

    def crop_page(page, margin_px):

        mediabox = page.mediabox
        left, bottom, right, top = mediabox
        x0, y0, x1, y1 = margin_px, margin_px, int(page_height_mm) - margin_px, int(page_height_mm) - margin_px
    for page in reader.pages:
        mediabox = page.mediabox  # Retrieve mediabox coordinates
        left, bottom, right, top = mediabox  # Unpack coordinates

        x0, y0, x1, y1 = margin_px, margin_px, int(page_height_mm) - margin_px, int(page_height_mm) - margin_px

        cropped_page = crop_page(page, margin_px)

        # Adjust left edge to avoid overlap with content from overlapping areas
        prev_content_area = [max(prev_right, left), bottom, min(right, prev_right + margin_px), top]
        cropped_page.mediabox = prev_content_area

        # Check for potential gaps due to inconsistent margins
        if prev_right + margin_px < left:
            # If gap, adjust both pages to minimize it
            gap = left - (prev_right + margin_px)
            prev_content_area[2] += gap // 2  # Increase right edge of previous page
            cropped_page.mediabox[0] -= gap // 2  # Decrease left edge of current page

        prev_right = cropped_page.mediabox[2]  # Update for next page

        pdf_writer.add_page(cropped_page)

    try:
        with open(output_file, 'wb') as f:
            pdf_writer.write(f)
    except IOError as e:
        raise IOError(f"Error saving combined PDF to '{output_file}': {e}")



if __name__ == '__main__':
    input_file = r'A:\taxcalc_paths\xhtml_test/Base_FFS_T.pdf'  # Replace with your actual file path
    output_file = 'single_page_overlapping.pdf'
    # Adjust margin_mm (5) if needed
    stitch_pdfs_overlapping(input_file, output_file)


