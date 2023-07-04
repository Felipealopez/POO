from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QWidget, QComboBox, QVBoxLayout, QPushButton, QDateEdit, QLabel, QLineEdit, QMessageBox

class Eventos(QWidget): 

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eventos dark")
        self.setGeometry(150,150,400,300)

        self.layout = QVBoxLayout(self)

        self.eventobox = QComboBox()
        self.eventobox.addItem("Concierto")
        self.eventobox.addItem("Fiesta")
        self.eventobox.addItem("Conferencia")
        self.eventobox.currentIndexChanged.connect(self.eventoentradas)

        self.layout.addWidget(self.eventobox)

        self.fecha = QDateEdit()
        self.fecha.setCalendarPopup(True)
        self.layout.addWidget(self.fecha)

        self.valor = QLabel("Valor de la Entrada:")
        self.layout.addWidget(self.valor)

        self.editarparametro = QLineEdit()
        self.layout.addWidget(self.editarparametro)
        
        self.limiteEdad = QLabel("Límite de Edad:")
        self.layout.addWidget(self.limiteEdad)

        self.limiteEdadMod = QLineEdit()
        self.layout.addWidget(self.limiteEdadMod)

        agregarboton = QPushButton("Nuevo Evento")
        agregarboton.clicked.connect(self.nuevoevento)
        self.layout.addWidget(agregarboton)

        self.eventos = []

    def eventoentradas(self):
        eventoseleccionado = self.eventobox.currentText()

        if eventoseleccionado == "Concierto" or eventoseleccionado == "Fiesta":
            self.valor.show()
            self.editarparametro.show()
            self.limiteEdad.show()
            self.limiteEdadMod.show()
        else:
            self.valor.hide()
            self.editarparametro.hide()
            self.limiteEdad.hide()
            self.limiteEdadMod.hide()


    def nuevoevento(self):
        evento = self.eventobox.currentText()
        fecha = self.fecha.date().toString(Qt.ISODate)
        valor = self.editarparametro.text()
        limiteedad = self.limiteEdadMod.text()

        self.eventos.append((evento, fecha, valor, limiteedad))

        self.mensajeexito("Evento agregado", "El evento ha sido agregado correctamente.")

        self.eventobox.setCurrentIndex(0)
        self.fecha.setDate(QDate.currentDate())
        self.editarparametro.clear()
        self.limiteEdadMod.clear()

    def mensajeexito(self, exito, mensajes):
        mensaje = QMessageBox()
        mensaje.setWindowTitle(exito)
        mensaje.setText(mensajes)
        mensaje.exec()

