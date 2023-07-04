import sys
from ventana import Eventos 
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    ventana = Eventos()
    ventana.show()
    
    sys.exit(app.exec())