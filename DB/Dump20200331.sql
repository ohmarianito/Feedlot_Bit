CREATE DATABASE  IF NOT EXISTS `feedlot` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `feedlot`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: feedlot
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `animal`
--

DROP TABLE IF EXISTS `animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal` (
  `animalId` int NOT NULL AUTO_INCREMENT,
  `tipoAnimalId` int NOT NULL,
  `animalIdInt` varchar(45) NOT NULL,
  PRIMARY KEY (`animalId`),
  KEY `tipoAnimalId_idx` (`tipoAnimalId`),
  CONSTRAINT `tipoAnimalId` FOREIGN KEY (`tipoAnimalId`) REFERENCES `tipoanimal` (`tipoAnimalId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal`
--

LOCK TABLES `animal` WRITE;
/*!40000 ALTER TABLE `animal` DISABLE KEYS */;
INSERT INTO `animal` VALUES (1,1,'12324gdsag'),(2,2,'BHSDGS3215145');
/*!40000 ALTER TABLE `animal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `animalhistoria`
--

DROP TABLE IF EXISTS `animalhistoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animalhistoria` (
  `animalId` int NOT NULL,
  `animalHistoriaId` int NOT NULL,
  PRIMARY KEY (`animalHistoriaId`,`animalId`),
  KEY `animalId_idx` (`animalId`),
  CONSTRAINT `animalId` FOREIGN KEY (`animalId`) REFERENCES `animal` (`animalId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animalhistoria`
--

LOCK TABLES `animalhistoria` WRITE;
/*!40000 ALTER TABLE `animalhistoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `animalhistoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `compraId` int NOT NULL AUTO_INCREMENT,
  `compraFecha` date NOT NULL,
  `animalId` int NOT NULL,
  `compraPrecio` double NOT NULL,
  PRIMARY KEY (`compraId`),
  KEY `animalId_idx` (`animalId`),
  CONSTRAINT `FKcompraanimalId` FOREIGN KEY (`animalId`) REFERENCES `animal` (`animalId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (1,'2020-03-31',1,123);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `corral`
--

DROP TABLE IF EXISTS `corral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `corral` (
  `corralId` int NOT NULL AUTO_INCREMENT,
  `corralNom` varchar(45) NOT NULL,
  `corralCap` int NOT NULL,
  `corralUbi` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`corralId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corral`
--

LOCK TABLES `corral` WRITE;
/*!40000 ALTER TABLE `corral` DISABLE KEYS */;
INSERT INTO `corral` VALUES (2,'Corral 1',10,'Ubicación 1'),(3,'Corral 2',20,'Ubicación 2');
/*!40000 ALTER TABLE `corral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `corralanimal`
--

DROP TABLE IF EXISTS `corralanimal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `corralanimal` (
  `corralId` int NOT NULL,
  `animalId` int NOT NULL,
  PRIMARY KEY (`corralId`,`animalId`),
  KEY `corralId_idx` (`corralId`),
  KEY `animalId_idx` (`animalId`),
  CONSTRAINT `FKanimalId` FOREIGN KEY (`animalId`) REFERENCES `animal` (`animalId`),
  CONSTRAINT `FKcorralId` FOREIGN KEY (`corralId`) REFERENCES `corral` (`corralId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corralanimal`
--

LOCK TABLES `corralanimal` WRITE;
/*!40000 ALTER TABLE `corralanimal` DISABLE KEYS */;
/*!40000 ALTER TABLE `corralanimal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engorde`
--

DROP TABLE IF EXISTS `engorde`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engorde` (
  `engordeId` int NOT NULL AUTO_INCREMENT,
  `animalId` int DEFAULT NULL,
  `tipoRacionId` int DEFAULT NULL,
  `corralId` int DEFAULT NULL,
  PRIMARY KEY (`engordeId`),
  KEY `animalId_idx` (`animalId`),
  KEY `tipoRacionId_idx` (`tipoRacionId`),
  KEY `corralId_idx` (`corralId`),
  CONSTRAINT `FKengordeAnimalId` FOREIGN KEY (`animalId`) REFERENCES `animal` (`animalId`),
  CONSTRAINT `FKengordeCorralId` FOREIGN KEY (`corralId`) REFERENCES `corral` (`corralId`),
  CONSTRAINT `FKengordeTipoRacionId` FOREIGN KEY (`tipoRacionId`) REFERENCES `tiporacion` (`tipoRacionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engorde`
--

LOCK TABLES `engorde` WRITE;
/*!40000 ALTER TABLE `engorde` DISABLE KEYS */;
/*!40000 ALTER TABLE `engorde` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frigorifico`
--

DROP TABLE IF EXISTS `frigorifico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `frigorifico` (
  `frigorificoId` int NOT NULL AUTO_INCREMENT,
  `frigorificoNom` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`frigorificoId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frigorifico`
--

LOCK TABLES `frigorifico` WRITE;
/*!40000 ALTER TABLE `frigorifico` DISABLE KEYS */;
INSERT INTO `frigorifico` VALUES (1,'Frigorífico 11'),(2,'Frigorífico 2');
/*!40000 ALTER TABLE `frigorifico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parametro`
--

DROP TABLE IF EXISTS `parametro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parametro` (
  `parametroId` int NOT NULL AUTO_INCREMENT,
  `parametroNom` varchar(45) DEFAULT NULL,
  `parametroValor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`parametroId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parametro`
--

LOCK TABLES `parametro` WRITE;
/*!40000 ALTER TABLE `parametro` DISABLE KEYS */;
INSERT INTO `parametro` VALUES (1,'','');
/*!40000 ALTER TABLE `parametro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `precioreferencia`
--

DROP TABLE IF EXISTS `precioreferencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `precioreferencia` (
  `precioReferenciaId` int NOT NULL AUTO_INCREMENT,
  `precioReferenciaFecha` date NOT NULL,
  `precioReferenciaPrecio` double DEFAULT NULL,
  PRIMARY KEY (`precioReferenciaId`,`precioReferenciaFecha`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `precioreferencia`
--

LOCK TABLES `precioreferencia` WRITE;
/*!40000 ALTER TABLE `precioreferencia` DISABLE KEYS */;
INSERT INTO `precioreferencia` VALUES (1,'2020-03-14',100);
/*!40000 ALTER TABLE `precioreferencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipoanimal`
--

DROP TABLE IF EXISTS `tipoanimal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipoanimal` (
  `tipoAnimalId` int NOT NULL AUTO_INCREMENT,
  `tipoAnimalNom` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`tipoAnimalId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipoanimal`
--

LOCK TABLES `tipoanimal` WRITE;
/*!40000 ALTER TABLE `tipoanimal` DISABLE KEYS */;
INSERT INTO `tipoanimal` VALUES (1,'Vaca'),(2,'Vaca 2');
/*!40000 ALTER TABLE `tipoanimal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiporacion`
--

DROP TABLE IF EXISTS `tiporacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tiporacion` (
  `tipoRacionId` int NOT NULL AUTO_INCREMENT,
  `tipoRacionNom` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`tipoRacionId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiporacion`
--

LOCK TABLES `tiporacion` WRITE;
/*!40000 ALTER TABLE `tiporacion` DISABLE KEYS */;
INSERT INTO `tiporacion` VALUES (1,'Ración 1');
/*!40000 ALTER TABLE `tiporacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `usuarioEmail` varchar(100) NOT NULL,
  `usuarioPass` varchar(45) NOT NULL,
  `usuarioNom` varchar(45) NOT NULL,
  PRIMARY KEY (`usuarioEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES ('mebenavides@outlook.com','123','Martin');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `ventaId` int NOT NULL AUTO_INCREMENT,
  `ventaFecha` date NOT NULL,
  `animalId` int NOT NULL,
  `frigorificoId` int NOT NULL,
  `ventaPrecio` double NOT NULL,
  PRIMARY KEY (`ventaId`),
  KEY `animalId_idx` (`animalId`),
  KEY `frigorificoId_idx` (`frigorificoId`),
  CONSTRAINT `FKfrigorificoId` FOREIGN KEY (`frigorificoId`) REFERENCES `frigorifico` (`frigorificoId`),
  CONSTRAINT `FKventaanimalId` FOREIGN KEY (`animalId`) REFERENCES `animal` (`animalId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,'2020-03-31',1,2,1234),(2,'2020-03-31',2,1,1234),(3,'2020-03-31',2,2,555),(4,'2020-03-31',1,1,555);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-31 18:11:20
