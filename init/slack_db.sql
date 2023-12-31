-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: slack_db
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `form_submissions`
--

DROP TABLE IF EXISTS `form_submissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `form_submissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  `answers` json NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `form_submissions`
--

LOCK TABLES `form_submissions` WRITE;
/*!40000 ALTER TABLE `form_submissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `form_submissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `form_templates`
--

DROP TABLE IF EXISTS `form_templates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `form_templates` (
  `type` varchar(50) NOT NULL,
  `template` json NOT NULL,
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `form_templates`
--

LOCK TABLES `form_templates` WRITE;
/*!40000 ALTER TABLE `form_templates` DISABLE KEYS */;
INSERT INTO `form_templates` VALUES ('amount form','[{\"type\": \"input\", \"label\": {\"text\": \"Registration ID\", \"type\": \"plain_text\", \"emoji\": true}, \"element\": {\"type\": \"plain_text_input\", \"action_id\": \"input\"}, \"block_id\": \"registration id\"}, {\"type\": \"input\", \"label\": {\"text\": \"Amount\", \"type\": \"plain_text\", \"emoji\": true}, \"element\": {\"type\": \"plain_text_input\", \"action_id\": \"input\", \"multiline\": true}, \"block_id\": \"amount\"}]'),('blank form','[{\"type\": \"input\", \"label\": {\"text\": \"Input\", \"type\": \"plain_text\", \"emoji\": true}, \"element\": {\"type\": \"plain_text_input\", \"action_id\": \"input\", \"multiline\": true}, \"block_id\": \"input\"}]'),('init','[{\"text\": {\"text\": \":wave:  Selamat Datang!\", \"type\": \"plain_text\", \"emoji\": true}, \"type\": \"header\", \"block_id\": \"front_header\"}, {\"text\": {\"text\": \" \", \"type\": \"plain_text\", \"emoji\": true}, \"type\": \"section\", \"block_id\": \"empty_line\"}, {\"text\": {\"text\": \"Segera buka *Form List* pada bagian kanan atas untuk memilih dan mulai mengisi _form_!  \", \"type\": \"mrkdwn\"}, \"type\": \"section\", \"accessory\": {\"type\": \"image\", \"alt_text\": \"form_image\", \"image_url\": \"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvectorified.com%2Fimages%2Ffill-form-icon-30.png&f=1&nofb=1&ipt=968c3ccb3f8ded999bd761585c7d0ddd86a1a10960f4a439fa7d5a2c2565acea&ipo=images\"}}, {\"type\": \"divider\"}, {\"type\": \"context\", \"elements\": [{\"text\": \"Developed by *Biznet Networks*\", \"type\": \"mrkdwn\"}]}]');
/*!40000 ALTER TABLE `form_templates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'slack_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-04 15:14:20
