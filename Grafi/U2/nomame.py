from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Datos del paciente
nombre_paciente = "Juan Pérez"
diagnostico = "infección gastrointestinal"
fecha_alta = "24 de noviembre de 2024"
control_recomendado = "1 de diciembre de 2024"

# Crear el objeto PDF
pdf_file = "/home/javp04/Documentos/nota_medica.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Título y texto de la nota médica
styles = getSampleStyleSheet()
style_normal = styles["Normal"]
c.setFont("Helvetica-Bold", 16)
c.drawString(50, 750, "Nota Médica")

# Contenido de la nota
c.setFont("Helvetica", 12)
text = [
    f"Fecha: {fecha_alta}",
    "",
    f"Se hace constar que el paciente, {nombre_paciente}, estuvo internado en el hospital desde la noche del viernes hasta el sábado debido a una {diagnostico}.",
    "Durante este período, el paciente recibió tratamiento adecuado bajo supervisión médica, con seguimiento de signos vitales y administración de medicamentos pertinentes para la infección.",
    "El paciente ha mostrado signos de mejora y se le ha dado de alta con recomendaciones médicas para el seguimiento adecuado de su condición.",
    f"Se recomienda continuar con el tratamiento prescrito y mantener el reposo adecuado para asegurar una recuperación total.",
    "",
    f"Se recomienda realizar un control médico en {control_recomendado} para evaluar la evolución del paciente.",
    "",
    "Firma:",
    "[Firma Digitalizada o Imagen]"
]

# Dibujar el texto en el PDF
y_position = 700
for line in text:
    c.drawString(50, y_position, line)
    y_position -= 14

# Agregar la imagen de la firma (si tienes una firma escaneada)
firma_imagen = "/home/javp04/Documentos/firma.png"  # Ruta de la imagen de la firma
c.drawImage(firma_imagen, 50, y_position - 50, width=2*inch, height=1*inch)  # Ajustar según el tamaño

# Guardar el archivo PDF
c.save()

print(f"Nota médica generada en: {pdf_file}")
