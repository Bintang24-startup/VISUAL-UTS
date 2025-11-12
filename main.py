import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# Import class form CRUD Anda
from donatur_form import DonaturForm
from donasi_form import DonasiForm

# Opsional: Impor untuk memastikan tabel sudah tercipta jika belum (MySQL/SQLite)
from db_connector import create_tables

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # --- Memuat file UI utama menggunakan QUiLoader ---
        filenya = QFile('form.ui')

        # Coba buka file. Jika gagal, tampilkan pesan error dan keluar.
        if not filenya.open(QFile.ReadOnly):
            # Mengganti 'mainwindow.ui' ke 'form.ui' di pesan error
            QMessageBox.critical(self, "Error UI", "File 'form.ui' tidak dapat dibuka. Pastikan form.ui ada di direktori kerja.")
            sys.exit(1)

        muatFile = QUiLoader()

        # PENTING: Muat UI TANPA PARENT (None) terlebih dahulu.
        # Ini mencegah objek C++ dihancurkan sebelum kita mengambil elemennya.
        self.temp_form_container = muatFile.load(filenya, None)
        filenya.close()

        if self.temp_form_container is None:
            QMessageBox.critical(self, "Error UI", "Gagal memuat konten UI dari form.ui.")
            sys.exit(1)

        # 1. Mengambil MenuBar dari container dan mengaturnya ke Jendela Utama (self)
        self.setMenuBar(self.temp_form_container.menuBar())

        # 2. Mengambil Central Widget dan mengaturnya ke Jendela Utama (self)
        self.setCentralWidget(self.temp_form_container.centralWidget())

        # Atur properti jendela
        self.resize(self.centralWidget().size()) # Ukuran berdasarkan central widget
        self.setWindowTitle("APLIKASI KEUANGAN MASJID")

        # Inisialisasi jendela form sebagai atribut
        self.donatur_window = None
        self.donasi_window = None

        # --- Menghubungkan Aksi Menu ke Fungsi (Slots) ---
        # Gunakan self.temp_form_container karena objek aksi (QAction) dimuat di dalamnya
        self.temp_form_container.actionDATA_DONATUR.triggered.connect(self.show_donatur_form)
        self.temp_form_container.actionDATA_DONASI.triggered.connect(self.show_donasi_form)


    def show_donatur_form(self):
        """Menampilkan jendela DonaturForm."""
        if self.donatur_window is None:
            self.donatur_window = DonaturForm()
        self.donatur_window.show()
        # Mengatur jendela ke depan dan aktif
        self.donatur_window.raise_()
        self.donatur_window.activateWindow()

    def show_donasi_form(self):
        """Menampilkan jendela DonasiForm."""
        if self.donasi_window is None:
            self.donasi_window = DonasiForm()
        self.donasi_window.show()
        # Mengatur jendela ke depan dan aktif
        self.donasi_window.raise_()
        self.donasi_window.activateWindow()

# --- Eksekusi Aplikasi ---
if __name__ == "__main__":
    # Pastikan database dan tabel tercipta (Ini sudah teratasi sebelumnya)
    create_tables()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
