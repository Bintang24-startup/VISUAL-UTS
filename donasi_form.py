import sys
import mysql.connector
from mysql.connector import errorcode
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile, QDate
from PySide6.QtUiTools import QUiLoader

# Import konektor MySQL
from db_connector import connect_db

class DonasiForm(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Memuat Desain Form menggunakan QUiLoader ---
        filenya = QFile('donasi_form.ui')
        if not filenya.open(QFile.ReadOnly):
             QMessageBox.critical(self, "Error UI", "File 'donasi_form.ui' tidak dapat dibuka.")
             sys.exit(1)

        muatFile = QUiLoader()
        # Membuat instance QWidget/Form dari UI, lalu memuatnya ke jendela utama
        # Karena UI Anda <class>Form</class>, ini akan dimuat sebagai QWidget,
        # kita harus memuat semua elemennya
        self.form = muatFile.load(filenya, self)
        filenya.close()

        # Karena UI Anda adalah QWidget, kita menjadikannya central widget
        self.setCentralWidget(self.form)
        self.resize(self.form.size())
        self.setWindowTitle("FORM DONASI")

        # --- Koneksi Database ---
        self.conn = connect_db()
        if self.conn is None:
            QMessageBox.critical(self, "Koneksi Gagal", "Tidak dapat terhubung ke database MySQL.")
            sys.exit(1)

        # --- Menghubungkan Widget ke Fungsi ---
        # Menggunakan self.form.namaWidget
        self.form.simpanButton.clicked.connect(self.simpan_donasi)
        self.form.ubahButton.clicked.connect(self.hapus_donasi)    # <--- Menghubungkan ubahButton ke HAPUS (sesuai teks di UI)
        self.form.hapusButton.clicked.connect(self.ubah_donasi)    # <--- Menghubungkan hapusButton ke UBAH (sesuai teks di UI)

        # Event Tabel (Diasumsikan Anda menambahkan QTableWidget bernama 'donasiTable' di desain UI Anda,
        # Jika belum ada, fungsi load_donasi_to_table akan gagal!)
        # self.form.donasiTable.cellClicked.connect(self.load_donasi_to_form)

        # Inisialisasi
        self.form.tglMasukInput.setDisplayFormat("yyyy-MM-dd")
        self.form.tglMasukInput.setDate(QDate.currentDate())
        self.load_donatur_ids()
        # self.load_donasi_to_table() # Panggil setelah memastikan ada QTableWidget

    def load_donatur_ids(self):
        """Memuat ID Donatur dari tabel data_donatur ke QComboBox."""
        cursor = self.conn.cursor()
        self.form.idDonaturInput.clear()

        try:
            cursor.execute("SELECT id_donatur, nama FROM data_donatur")
            data = cursor.fetchall()

            for id_d, nama in data:
                # Menampilkan Nama Donatur, namun menyimpan ID Donatur sebagai data
                self.form.idDonaturInput.addItem(f"{id_d} - {nama}", id_d)

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error DB", f"Gagal memuat ID Donatur: {e}")
        finally:
            cursor.close()

    def get_form_data(self):
        """Mengambil data dari input form Donasi."""
        id_d = self.form.idDonasiInput.text()

        # Ambil ID Donatur dari data yang disimpan di QComboBox
        id_donatur = self.form.idDonaturInput.currentData()

        tgl_masuk = self.form.tglMasukInput.date().toString("yyyy-MM-dd")

        # Membersihkan dan konversi jumlah ke float
        try:
            jumlah = float(self.form.jumlahInput.text().replace(',', '').replace('.', ''))
        except ValueError:
            jumlah = 0.0

        return id_d, id_donatur, tgl_masuk, jumlah

    # --- FUNGSI CRUD DONASI ---
    def simpan_donasi(self):
        id_d, id_donatur, tgl_masuk, jumlah = self.get_form_data()

        if not id_d or not id_donatur or jumlah <= 0:
            QMessageBox.warning(self, "Peringatan", "Semua field wajib diisi dengan benar!")
            return

        cursor = self.conn.cursor()
        try:
            # Dapatkan data detail donatur dari ID terpilih
            cursor.execute("SELECT nama, tlp, alamat FROM data_donatur WHERE id_donatur = %s", (id_donatur,))
            donatur_data = cursor.fetchone()

            if donatur_data is None:
                QMessageBox.warning(self, "Peringatan", "ID Donatur tidak valid.")
                return

            nama_donatur, tlp_donatur, alamat_donatur = donatur_data

            # INSERT data ke data_donasi (gunakan %s)
            insert_query = """
            INSERT INTO data_donasi (id_donasi, nama, tlp, alamat, tgl_masuk, jumlah, id_donatur)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (id_d, nama_donatur, tlp_donatur, alamat_donatur, tgl_masuk, jumlah, id_donatur))
            self.conn.commit()

            QMessageBox.information(self, "Sukses", "Transaksi Donasi berhasil disimpan.")
            self.clear_form()
            # self.load_donasi_to_table() # Muat ulang tabel jika ada
        except mysql.connector.IntegrityError:
            QMessageBox.critical(self, "Error", "ID Donasi sudah ada atau Kunci Asing bermasalah.")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error Database", f"Gagal menyimpan data: {e}")
        finally:
            cursor.close()


    def ubah_donasi(self):
        """Fungsi untuk UPDATE data yang sudah ada."""
        id_d, id_donatur, tgl_masuk, jumlah = self.get_form_data()

        if not id_d or not id_donatur or jumlah <= 0:
            QMessageBox.warning(self, "Peringatan", "Pilih data dan pastikan semua field wajib terisi untuk diubah.")
            return

        cursor = self.conn.cursor()
        try:
            # Dapatkan data detail donatur dari ID terpilih
            cursor.execute("SELECT nama, tlp, alamat FROM data_donatur WHERE id_donatur = %s", (id_donatur,))
            donatur_data = cursor.fetchone()
            if donatur_data is None:
                QMessageBox.warning(self, "Peringatan", "ID Donatur tidak valid.")
                return
            nama_donatur, tlp_donatur, alamat_donatur = donatur_data

            update_query = """
            UPDATE data_donasi SET
                id_donatur=%s, nama=%s, tlp=%s, alamat=%s, tgl_masuk=%s, jumlah=%s
            WHERE id_donasi=%s
            """
            cursor.execute(update_query,
                           (id_donatur, nama_donatur, tlp_donatur, alamat_donatur, tgl_masuk, jumlah, id_d))
            self.conn.commit()

            QMessageBox.information(self, "Sukses", f"Transaksi Donasi ID {id_d} berhasil diubah.")
            self.clear_form()
            # self.load_donasi_to_table() # Muat ulang tabel jika ada
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error Database", f"Gagal mengubah data: {e}")
        finally:
            cursor.close()

    def hapus_donasi(self):
        """Fungsi untuk DELETE data."""
        id_d = self.form.idDonasiInput.text()

        if not id_d or self.form.idDonasiInput.isEnabled():
            QMessageBox.warning(self, "Peringatan", "Masukkan atau pilih ID Donasi yang ingin dihapus.")
            return

        reply = QMessageBox.question(self, 'Konfirmasi Hapus',
            f"Anda yakin ingin menghapus Transaksi Donasi ID {id_d}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            cursor = self.conn.cursor()
            try:
                cursor.execute("DELETE FROM data_donasi WHERE id_donasi = %s", (id_d,))
                self.conn.commit()

                QMessageBox.information(self, "Sukses", f"Transaksi Donasi ID {id_d} berhasil dihapus.")
                self.clear_form()
                # self.load_donasi_to_table() # Muat ulang tabel jika ada
            except mysql.connector.Error as e:
                QMessageBox.critical(self, "Error Database", f"Gagal menghapus data: {e}")
            finally:
                cursor.close()

    # --- FUNGSI UTILITY ---

    # Fungsi ini perlu disesuaikan jika Anda menambahkan QTableWidget di UI
    # def load_donasi_to_form(self, row, column):
    #     # ... (logika untuk memuat data dari tabel ke form)
    #     pass

    def clear_form(self):
        """Membersihkan semua input form."""
        self.form.idDonasiInput.clear()
        self.form.jumlahInput.clear()
        self.form.idDonasiInput.setEnabled(True)
        self.form.tglMasukInput.setDate(QDate.currentDate())
        self.form.idDonaturInput.setCurrentIndex(-1) # Pilih item kosong/default

    def closeEvent(self, event):
        """Menutup koneksi database saat jendela ditutup."""
        if self.conn:
            self.conn.close()
        event.accept()

# Jika Anda menjalankan file ini secara independen untuk tes
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DonasiForm()
    window.show()
    sys.exit(app.exec())# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
