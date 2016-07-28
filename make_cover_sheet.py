#!/usr/bin/env python

import sys

from reportlab.graphics.barcode import code128
from reportlab.lib import pagesizes
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas

def main(args):
    if len(args) < 4:
        sys.stderr.write("usage: OUTFILE A_FILE_LOCATION A_NUM RECEIPT_NUM\n")
        return 1

    output_filename, a_file_location, a_number, receipt_number = args

    create_pdf(output_filename, a_file_location, a_number, receipt_number)

    return 0

WIDTH, HEIGHT = pagesizes.letter
POS_X = 2 * inch
POS_Y_LOC = 8 * inch
POS_Y_A_NUMBER = 6 * inch
POS_Y_RECEIPT_NUMBER = 4 * inch
BAR_WIDTH = 0.015 * inch # (default 0.0075")
BAR_HEIGHT = 0.75 * inch

def create_pdf(out_filename, a_file_location, a_number, receipt_number):
    c = canvas.Canvas(out_filename, pagesize=pagesizes.letter)

    c.setFont('Helvetica', 18)
    c.drawString(POS_X + 0.5, POS_Y_LOC, "A FILE LOCATION")
    c.setFont('Helvetica', 24)
    c.drawString(POS_X + 0.5, POS_Y_LOC - 0.5 * inch, a_file_location)

    c.setFont('Helvetica', 14)

    barcode_a_num = code128.Code128(a_number, barWidth=BAR_WIDTH,
                                    barHeight=BAR_HEIGHT)
    barcode_receipt_num = code128.Code128(receipt_number, barWidth=BAR_WIDTH,
                                          barHeight=BAR_HEIGHT)

    barcode_a_num.drawOn(c, POS_X, POS_Y_A_NUMBER)
    c.drawString(POS_X + 0.5 * inch,  POS_Y_A_NUMBER - 0.25 * inch, a_number)

    barcode_receipt_num.drawOn(c, POS_X, POS_Y_RECEIPT_NUMBER)
    c.drawString(POS_X + 0.5 * inch,  POS_Y_RECEIPT_NUMBER - 0.25 * inch, receipt_number)

    c.showPage()

    c.save()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
