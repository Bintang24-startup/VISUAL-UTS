# This Python file uses the following encoding: utf-8
import mysql.connector
from mysql.connector import errorcode
import sys

# ==========================================================
# GANTI DETAIL KONEKSI INI SESUAI DENGAN SERVER MYSQL ANDA
# ==========================================================
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "" # <--- HARUS DIGANTI!
DATABASE_NAME = "aplikasi_keuangan_masjid"
# ==========================================================

def connect_db(database_exist=True):
    """
    Membuat koneksi ke database MySQL.
    Jika database_exist=False, koneksi dilakukan tanpa menentukan nama DB.
    """
    try:
        config = {
            'host': MYSQL_HOST,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD
        }
        if database_exist:
            config['database'] = DATABASE_NAME

        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Username atau password MySQL salah. Cek konfigurasi.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR and database_exist:
            # Jika DB belum ada, return None agar fungsi create_tables bisa memanggil create_database
            return None
        else:
            print(f"Error koneksi database: {err}")
        return None

def create_database():
    """Membuat database jika belum ada."""
    # Koneksi tanpa menentukan database_name
    conn = connect_db(database_exist=False)
    if conn is not None:
        cursor = conn.cursor()
        try:
            # Query untuk membuat database jika belum ada
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME} DEFAULT CHARACTER SET 'utf8'")
            print(f"Database {DATABASE_NAME} berhasil dibuat atau sudah ada.")
        except mysql.connector.Error as err:
            print(f"Gagal membuat database: {err}")
        finally:
            cursor.close()
            conn.close()

def create_tables():
    """Membuat tabel Donatur dan Donasi jika belum ada."""
    # Pastikan database tercipta dulu
    create_database()

    conn = connect_db(database_exist=True)

    if conn is not None:
        cursor = conn.cursor()

        # SQL untuk tabel data_donatur
        donatur_table = f"""
        CREATE TABLE IF NOT EXISTS data_donatur (
            id_donatur VARCHAR(10) PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            tlp VARCHAR(15),
            alamat VARCHAR(255)
        ) ENGINE=InnoDB;
        """

        # SQL untuk tabel data_donasi
        donasi_table = f"""
        CREATE TABLE IF NOT EXISTS data_donasi (
            id_donasi VARCHAR(10) PRIMARY KEY,
            nama VARCHAR(100),
            tlp VARCHAR(15),
            alamat VARCHAR(255),
            tgl_masuk DATE NOT NULL,
            jumlah DECIMAL(10, 2) NOT NULL,
            id_donatur VARCHAR(10),
            FOREIGN KEY (id_donatur) REFERENCES data_donatur(id_donatur)
                ON DELETE CASCADE ON UPDATE CASCADE
        ) ENGINE=InnoDB;
        """
        try:
            cursor.execute(donatur_table)
            cursor.execute(donasi_table)
            conn.commit()
            print("Tabel Donatur dan Donasi berhasil dibuat atau sudah ada.")
        except mysql.connector.Error as err:
            print(f"Error saat membuat tabel: {err}")
        finally:
            cursor.close()
            conn.close()

# --- BLOK UTAMA EKSEKUSI ---
if __name__ == '__main__':
    # Jalankan file ini secara langsung untuk inisialisasi awal
    create_tables()
    print("Database MySQL siap digunakan.")
