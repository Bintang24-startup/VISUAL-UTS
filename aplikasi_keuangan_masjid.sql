-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 10, 2025 at 04:28 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aplikasi_keuangan_masjid`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_donasi`
--

CREATE TABLE `data_donasi` (
  `id_donasi` varchar(10) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `tlp` varchar(15) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `tgl_masuk` date NOT NULL,
  `jumlah` decimal(10,2) NOT NULL,
  `id_donatur` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `data_donatur`
--

CREATE TABLE `data_donatur` (
  `id_donatur` varchar(10) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `tlp` varchar(15) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_donasi`
--
ALTER TABLE `data_donasi`
  ADD PRIMARY KEY (`id_donasi`),
  ADD KEY `id_donatur` (`id_donatur`);

--
-- Indexes for table `data_donatur`
--
ALTER TABLE `data_donatur`
  ADD PRIMARY KEY (`id_donatur`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `data_donasi`
--
ALTER TABLE `data_donasi`
  ADD CONSTRAINT `data_donasi_ibfk_1` FOREIGN KEY (`id_donatur`) REFERENCES `data_donatur` (`id_donatur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
