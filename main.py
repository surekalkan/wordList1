import sys
from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow
from wordlist import load_words



if __name__ == '__main__':
    app = QApplication(sys.argv)

    words = load_words()

    main_window = MainWindow(words)
    main_window.show()

    sys.exit(app.exec())