-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: grupo11
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `canales`
--

DROP TABLE IF EXISTS `canales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canales` (
  `id_canal` smallint unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(128) DEFAULT NULL,
  `id_server` smallint unsigned NOT NULL,
  PRIMARY KEY (`id_canal`),
  KEY `id_server_idx` (`id_server`),
  CONSTRAINT `id_server` FOREIGN KEY (`id_server`) REFERENCES `servidor` (`id_server`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canales`
--

LOCK TABLES `canales` WRITE;
/*!40000 ALTER TABLE `canales` DISABLE KEYS */;
INSERT INTO `canales` VALUES (1,'Cocina Arabe','Recetas Faciles Cocina Arabe',2),(2,'Counter Stricke CSS','Mapas para Counter Stricke',1);
/*!40000 ALTER TABLE `canales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensajes`
--

DROP TABLE IF EXISTS `mensajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mensajes` (
  `id_mensaje` bigint unsigned NOT NULL,
  `cuerpo` varchar(500) NOT NULL,
  `f_envio` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `id_user` smallint unsigned NOT NULL,
  `id_canal` smallint unsigned NOT NULL,
  `visible` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_mensaje`),
  UNIQUE KEY `id_mensaje_UNIQUE` (`id_mensaje`),
  KEY `id_user_idx` (`id_user`),
  KEY `id_canal_idx` (`id_canal`),
  CONSTRAINT `id_canal` FOREIGN KEY (`id_canal`) REFERENCES `canales` (`id_canal`),
  CONSTRAINT `id_user` FOREIGN KEY (`id_user`) REFERENCES `usuarios` (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensajes`
--

LOCK TABLES `mensajes` WRITE;
/*!40000 ALTER TABLE `mensajes` DISABLE KEYS */;
/*!40000 ALTER TABLE `mensajes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servidor`
--

DROP TABLE IF EXISTS `servidor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidor` (
  `id_server` smallint unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(128) DEFAULT NULL,
  `f_creacion` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `activo` tinyint DEFAULT '1',
  `icono` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_server`),
  UNIQUE KEY `id_server_UNIQUE` (`id_server`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidor`
--

LOCK TABLES `servidor` WRITE;
/*!40000 ALTER TABLE `servidor` DISABLE KEYS */;
INSERT INTO `servidor` VALUES (1,'Gamer 1','Servidor de Video juegos','2023-09-26 04:01:07',1,NULL),(2,'Cocina Gourmet','Recetas de cocinas gourmet','2023-09-28 22:10:03',1,NULL),(3,'Computacion 1',NULL,'2023-09-29 04:18:20',1,NULL),(4,'Juegos de Mesa',NULL,'2023-09-29 04:29:01',1,NULL),(5,'Juegos de Mesa','Servidor Juegos de Mesa varios','2023-09-29 04:36:44',1,NULL),(6,'Juegos de Mesa','Servidor Juegos de Mesa varios','2023-09-29 04:37:37',1,NULL),(7,'Truco','Servidor Juegos de Mesa varios','2023-09-29 04:41:34',1,NULL),(8,'vsd','sdvsdv','2023-09-29 04:47:44',1,NULL);
/*!40000 ALTER TABLE `servidor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_server`
--

DROP TABLE IF EXISTS `user_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_server` (
  `id_user_server` smallint unsigned NOT NULL AUTO_INCREMENT,
  `propietario` tinyint unsigned NOT NULL DEFAULT '0',
  `id_user` smallint unsigned NOT NULL,
  `id_server` smallint unsigned NOT NULL,
  `f_union` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_user_server`),
  UNIQUE KEY `id_user_server_UNIQUE` (`id_user_server`),
  KEY `id_user_idx` (`id_user`),
  KEY `id_server_idx` (`id_server`),
  CONSTRAINT `id_servidor` FOREIGN KEY (`id_server`) REFERENCES `servidor` (`id_server`),
  CONSTRAINT `id_usuario` FOREIGN KEY (`id_user`) REFERENCES `usuarios` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_server`
--

LOCK TABLES `user_server` WRITE;
/*!40000 ALTER TABLE `user_server` DISABLE KEYS */;
INSERT INTO `user_server` VALUES (1,1,1,1,'2023-09-26 04:02:36'),(2,1,1,2,'2023-09-28 22:10:55'),(3,1,1,3,'2023-09-29 04:18:20'),(4,1,1,4,'2023-09-29 04:29:01'),(5,1,12,5,'2023-09-29 04:36:44'),(6,1,3,6,'2023-09-29 04:37:37'),(7,1,2,7,'2023-09-29 04:41:34');
/*!40000 ALTER TABLE `user_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_user` smallint unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `user` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `f_nac` date DEFAULT NULL,
  `avatar` varchar(45) DEFAULT NULL,
  `preg_secret` varchar(60) NOT NULL,
  `respuesta` varchar(45) NOT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `id_user_UNIQUE` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Nelson','Solano','nelsol@hotmail.com','rafucho','nelson562','1984-11-20',NULL,'Cual es tu comida preferida?','pizza'),(2,'Tobias','Solano',NULL,'tobito','tobito123',NULL,NULL,'Cual es tu pelicula favorita','rocky'),(3,'Guada','Rioja','guadita@gmail.com','guadirio','123456',NULL,NULL,'Nombre de tu mascota','Ela'),(9,'Sebastian','Moreno','miguelcancinos@hotmail.com','SebaMoreno23','sebita2023','1980-05-18',NULL,'Cual es tu pelicula favorita','Tiburon'),(11,'Miguel','Cancinos','miguelcancinos@hotmail.com','Migue22','miguelito2023',NULL,NULL,'Cual es tu pelicula favorita','Tiburon'),(12,'afadsf','asfasf','asfasf','asfasf','asfasf',NULL,NULL,'asfasf','asfasf'),(13,'Nelson','Solano','asfasf@hotmail.com','ZXCZXCZXC','asdasd',NULL,NULL,'comida','asfdasdas'),(14,'Conita','Sola','conita@gmail.com','conitadance','123456','2011-09-29',NULL,'pregunta_4','rojo'),(15,'PATRICIA','asasf','asasd','asdarrr','asarrr','2023-05-10',NULL,'Pelicula Favorita','rocky');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  6:27:12
