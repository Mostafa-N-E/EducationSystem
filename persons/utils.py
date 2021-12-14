import threading
from time import sleep

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
#
# canvas = canvas.Canvas('myfile.pdf', pagesize=letter)
# width, height = letter



class PdfThread(threading.Thread):
    def __init__(self, subject, content):
        self.subject = subject
        # self.recipient_list = recipient_list
        self.content = content
        threading.Thread.__init__(self)

    def run(self):
        sleep(10)

        doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
        # container for the 'Flowable' objects
        elements = []

        data = [self.content]
        t = Table(data)
        t.setStyle(TableStyle([('BACKGROUND', (1, 1), (-2, -2), colors.green),
                               ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))
        elements.append(t)
        # write the document to disk
        doc.build(elements)


def create_PDF(subject, content):
    PdfThread(subject, content).start()



# from django.contrib.gis.geos import io ###
# from reportlab.lib import colors
# from reportlab.pdfgen import canvas
# from reportlab.platypus import Table, TableStyle
#
#
# def Report(dict):
#     from reportlab.lib.utils import ImageReader
#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer)
#     textobject = p.beginText()
#     textobject.setTextOrigin(200, 680)
#     textobject.textLine('Title')
#     p.drawText(textobject)
#     logo = ImageReader('static/img/logo.png')
#     p.drawImage(logo, 100, 700 ,width = 400 ,height=100 ,mask = None)
#     data = [['00', '01', '02', '03', '04'],
#             ['10', '11', '12', '13', '14'],
#             ['20', '21', '22', '23', '24'],
#             ['30', '31', '32', '33', '34']]
#     f = Table(data)
#     f.setStyle(TableStyle([('BACKGROUND', (1, 1), (-2, -2),
#                             colors.green),
#                            ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))
#
#     p.showPage()
#     p.save()
#
#     buffer.seek(0)
#     return buffer
#
# width = 400
# height = 100
# x = 100
# y = 800
# f = Table(data)
# f.wrapOn(p, width, height)
# f.drawOn(p, x, y)
