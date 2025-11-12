import sys
import mysql.connector
from mysql.connector import errorcode
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# Import konektor MySQL
from db_connector import connect_db

class DonaturForm(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Memuat Desain Form menggunakan QUiLoader ---
        filenya = QFile('donatur_form.ui')
        if not filenya.open(QFile.ReadOnly):
             QMessageBox.critical(self, "Error UI", "File 'donatur_form.ui' tidak dapat dibuka.")
             sys.exit(1)

        muatFile = QUiLoader()
        self.form = muatFile.load(filenya, self)
        filenya.close()

        self.setCentralWidget(self.form)
        self.resize(self.form.size())
        self.setWindowTitle("FORM DONATUR")

        # --- Koneksi Database ---
        self.conn = connect_db()
        if self.conn is None:
            QMessageBox.critical(self, "Koneksi Gagal", "Tidak dapat terhubung ke database MySQL.")
            sys.exit(1)

        # --- Menghubungkan Widget ke Fungsi ---
        # Perhatikan: Logika tombol dibalik agar sesuai dengan teks yang Anda atur di UI (HAPUS dan UBAH)
        self.form.simpanButton.clicked.connect(self.simpan_data)
        self.form.ubahButton.clicked.connect(self.hapus_data) # Nama objek: ubahButton, Teks: HAPUS
        self.form.hapusButton.clicked.connect(self.ubah_data) # Nama objek: hapusButton, Teks: UBAH

        # Jika Anda menambahkan QTableWidget bernama 'donaturTable' ke UI:
        # self.form.donaturTable.cellClicked.connect(self.load_data_to_form)
        # self.load_data_to_table()

    def get_form_data(self):
        """Mengambil data dari input form Donatur."""
        id_d = self.form.idDonaturInput.text()
        nama = self.form.namaInput.text()
        telp = self.form.telpInput.text()
        alamat = self.form.alamatInput.toPlainText() # QTextEdit menggunakan toPlainText()

        return id_d, nama, telp, alamat

    # --- FUNGSI CRUD DONATUR ---

    def simpan_data(self):
        id_d, nama, telp, alamat = self.get_form_data()

        if not id_d or not nama:
            QMessageBox.warning(self, "Peringatan", "ID Donatur dan Nama wajib diisi!")
            return

        cursor = self.conn.cursor()
        try:
            # INSERT data ke data_donatur (gunakan %s untuk MySQL)
            insert_query = "INSERT INTO data_donatur (id_donatur, nama, tlp, alamat) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (id_d, nama, telp, alamat))
            self.conn.commit()

            QMessageBox.information(self, "Sukses", "Data Donatur berhasil disimpan.")
            self.clear_form()
            # self.load_data_to_table()
        except mysql.connector.IntegrityError:
            QMessageBox.critical(self, "Error", "ID Donatur sudah ada.")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error Database", f"Gagal menyimpan data: {e}")
        finally:
            cursor.close()


    def ubah_data(self):
        """Fungsi untuk UPDATE data yang sudah ada."""
        id_d, nama, telp, alamat = self.get_form_data()

        if not id_d or not nama:
            QMessageBox.warning(self, "Peringatan", "Pilih data atau isi ID Donatur dan Nama yang akan diubah.")
            return

        cursor = self.conn.cursor()
        try:
            # UPDATE data_donatur (gunakan %s untuk MySQL)
            update_query = """
            UPDATE data_donatur SET
                nama=%s, tlp=%s, alamat=%s
            WHERE id_donatur=%s
            """
            cursor.execute(update_query, (nama, telp, alamat, id_d))
            self.conn.commit()

            if cursor.rowcount == 0:
                 QMessageBox.warning(self, "Peringatan", f"Data Donatur ID {id_d} tidak ditemukan.")
                 return

            QMessageBox.information(self, "Sukses", f"Data Donatur ID {id_d} berhasil diubah.")
            self.clear_form()
            # self.load_data_to_table()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error Database", f"Gagal mengubah data: {e}")
        finally:
            cursor.close()


    def hapus_data(self):
        """Fungsi untuk DELETE data."""
        id_d = self.form.idDonaturInput.text()

        if not id_d:
            QMessageBox.warning(self, "Peringatan", "Masukkan atau pilih ID Donatur yang ingin dihapus.")
            return

        reply = QMessageBox.question(self, 'Konfirmasi Hapus',
            f"Anda yakin ingin menghapus data Donatur ID {id_d}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            cursor = self.conn.cursor()
            try:
                cursor.execute("DELETE FROM data_donatur WHERE id_donatur = %s", (id_d,))
                self.conn.commit()

                if cursor.rowcount == 0:
                    QMessageBox.warning(self, "Peringatan", f"Data Donatur ID {id_d} tidak ditemukan.")
                    return

                QMessageBox.information(self, "Sukses", f"Data Donatur ID {id_d} berhasil dihapus.")
                self.clear_form()
                # self.load_data_to_table()
            except mysql.connector.Error as e:
                QMessageBox.critical(self, "Error Database", f"Gagal menghapus data: {e}")
            finally:
                cursor.close()

    # --- FUNGSI UTILITY ---

    # Anda perlu mengimplementasikan ini jika Anda menambahkan QTableWidget
    # def load_data_to_form(self, row, column):
    #     # ... (Logika untuk mengisi form dari QTableWidget)
    #     pass

    # def load_data_to_table(self):
    #     # ... (Logika untuk memuat data dari DB ke QTableWidget)
    #     pass

    def clear_form(self):
        """Membersihkan semua input form."""
        self.form.idDonaturInput.clear()
        self.form.namaInput.clear()
        self.form.telpInput.clear()
        self.form.alamatInput.clear()
        self.form.idDonaturInput.setEnabled(True)

    def closeEvent(self, event):
        """Menutup koneksi database saat jendela ditutup."""
        if self.conn:
            self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DonaturForm()
    window.show()
    sys.exit(app.exec())# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
