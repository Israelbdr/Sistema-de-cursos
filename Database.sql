CREATE DATABASE  IF NOT EXISTS `siscursos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `siscursos`;
-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: siscursos
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `alunos` (
  `cpd` int(5) NOT NULL,
  `nome_do_aluno` varchar(45) DEFAULT NULL,
  `telefone` int(9) DEFAULT NULL,
  `endereco` varchar(128) DEFAULT NULL,
  `cep` int(9) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `codigo_do_curso` int(3) DEFAULT NULL,
  PRIMARY KEY (`cpd`),
  KEY `codigo_do_curso` (`codigo_do_curso`),
  CONSTRAINT `alunos_ibfk_1` FOREIGN KEY (`codigo_do_curso`) REFERENCES `cursos` (`codigo_do_curso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES (12345,'Jose Maria',981231232,'R. Alternada',65032123,'zemaria@hotmail.com',100),(21231,'João Tadeu',981113312,'Av. Alternada',65000000,'jaotadeu@hotmail.com',200),(23421,'João Maria',999112391,'Al. Alternada',65111111,'jaomaria@hotmail.com',200),(32154,'Jose Tadeu',981235432,'R. Projetada',65012321,'zetadeu@hotmail.com',100),(53421,'José José',988119933,'Av. Projetada',65060600,'zeze@hotmail.com',100),(65000,'Maria do Socorro',988121232,'Al. Principal',65033333,'mariahelp@hotmail.com',300),(65233,'Maria do Carmo',988331233,'Al. Projetada',65222222,'mariadanovela@hotmail.com',300);
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cursos` (
  `codigo_do_curso` int(3) NOT NULL,
  `nome_do_curso` varchar(45) DEFAULT NULL,
  `carga_horaria` varchar(30) DEFAULT NULL,
  `data_de_cadastro` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`codigo_do_curso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (100,'Medicina','2000 Horas','12/01/2018'),(200,'Direito','1000 Horas','25/01/2018'),(300,'Administração','700 Horas','13/02/2018');
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-16 20:44:26
