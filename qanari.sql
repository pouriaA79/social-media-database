-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 12, 2021 at 03:14 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qanari`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `aadd_hashtag` (IN `idd` INT, IN `mohtavaa` VARCHAR(256), IN `commentonavaaa` INT, IN `hashtagstrr` CHAR(6))  BEGIN
INSERT INTO ava(mohtava, user_id , commentonava) VALUES(mohtavaa,idd,commentonavaaa);
INSERT IGNORE INTO hashtag(hashtagstr)
VALUES
(
   CASE 
    WHEN hashtagstrr REGEXP '^[a-z , #]{6}$' 
    THEN 
    CASE  
    WHEN  hashtagstrr like '#%' 
    THEN hashtagstrr 
    else "" 
    END
    else ""
    
    END 
);
           
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `add_ava` (IN `idd` INT, IN `mohtavaa` VARCHAR(256))  BEGIN
INSERT INTO ava(mohtava, user_id ) VALUES(mohtavaa,idd);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `add_user` (IN `Fnamee` VARCHAR(20), IN `LNAMEE` VARCHAR(20), IN `Usernamee` VARCHAR(20), IN `passs` VARCHAR(128), IN `birthdayy` DATE, IN `biographyy` VARCHAR(256))  BEGIN
INSERT INTO user_qanari(FNAME, LNAME, USERNAME, PASS, 	birthdate, BIOGRAPHY) VALUES (Fnamee, LNAMEE, Usernamee, sha1(passs), birthdayy, biographyy);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `avahaye_hashtag` (IN `idd` INT, IN `idd_hashtagg` INT)  BEGIN
create TEMPORARY table block1 select blocker_id as col_id FROM block_user WHERE blocked_id=idd;
SELECT * from ava where id in ( select id from ava where id in  (SELECT id_ava from ava_hashtag where  id_hashtag=idd_hashtagg  )   and user_id not in (SELECT * from block1)  ) ;



END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `avahaye_portarafdar` (IN `idd` INT)  BEGIN
create TEMPORARY table block2 select blocked_id as col_id FROM block_user WHERE blocker_id in (select idd from ava )  ;

select ava_id , count(DISTINCT user_id) from ava_like WHERE (idd not in (SELECT * from block2)) GROUP by ava_id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `block` (IN `idd_user` INT, IN `id_bloc` INT)  BEGIN
insert IGNORE into block_user (blocked_id, blocker_id) VALUES(id_bloc,idd_user);
select * from block_user;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `daryaft_avaye_shakhsi` (IN `idd` INT)  BEGIN
select * from ava WHERE (user_id=idd) ORDER by post_date DESC;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `daryaft_comment` (IN `idd` INT, IN `id_avaa` INT)  BEGIN
create TEMPORARY table block3 select blocker_id as col_id FROM block_user WHERE blocked_id = idd;
select * from ava where commentonava=id_avaa and user_id not in( select * from block3)and ( SELECT user_id from ava where id=id_avaa) not in (select * from block3); 
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `daryaft_faaliat_donbal_shavandegan` (IN `idd` INT)  BEGIN
SELECT * from ava where user_id IN (select following_id from follow where follower_id=idd and following_id not in (select blocker_id FROM block_user WHERE  blocked_id =idd ) ) ORDER BY post_date DESC;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `donbal_kardan` (IN `idd_user` INT, IN `id_follow` INT)  BEGIN
	insert  into follow (follower_id, following_id) VALUES(idd_user,id_follow);
    SELECT * FROM follow;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `faaliat_karbaran` (IN `idd` INT, IN `idd_karbar` INT)  BEGIN
SELECT * from ava where user_id =idd_karbar and user_id not IN (select blocker_id FROM block_user WHERE blocker_id =idd_karbar and blocked_id =idd ) ORDER BY post_date DESC;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `like_ava` (IN `idd` INT, IN `id_avaa` INT)  BEGIN
create TEMPORARY table block5 select blocker_id as col_id FROM block_user WHERE blocked_id=idd;
insert IGNORE INTO ava_like (ava_id,user_id) select id_avaa,idd WHERE (select user_id FROM ava WHERE    id=id_avaa) not in (SELECT * from block5);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `list_ersal_konandegan_payam` (IN `idd` INT)  BEGIN
select  sender , mohtava , id_ava,date from message WHERE receiver= idd and id_ava not in (SELECT ava.id FROM block_user , ava where ava.user_id = block_user.blocker_id  and id_ava is NOT null and receiver=block_user.blocked_id)   ORDER BY date DESC;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `list_pasankonandegan` (IN `idd` INT, IN `avva_id` INT)  BEGIN
CREATE TEMPORARY TABLE num2 SELECT user_id as id from ava_like where ava_id =avva_id;
create TEMPORARY table block8 select blocked_id as col_id FROM block_user WHERE blocker_id in (select id  from user_qanari where id in (select user_id from ava where id=avva_id)) ;
create TEMPORARY table block7 select blocker_id as col_id FROM block_user WHERE blocked_id=idd;

select username from user_qanari where id IN (SELECT * FROM num2)  and idd not in (SELECT * from block8) and id not in( SELECT * from block7);

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `login` (IN `uname` VARCHAR(20), IN `passs` VARCHAR(128), OUT `idd` INT)  BEGIN
	INSERT INTO login(username) select USERNAME FROM user_qanari WHERE(USERNAME=uname AND PASS=SHA1(passs));
    SELECT id INTO idd FROM user_qanari WHERE USERNAME=uname AND PASS=SHA1(passs);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `logincheck` (IN `uname` VARCHAR(20))  BEGIN
	SELECT username,log_time 
 	FROM login
	WHERE username = uname ORDER by log_time limit 10;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `nazar_dadan` (IN `idd` INT, IN `id_avaa` INT, IN `moht` VARCHAR(128))  BEGIN
create TEMPORARY table avas select user_id as col_id FROM ava WHERE id=id_avaa;

INSERT ignore  INTO ava (mohtava, user_id,  commentonava) SELECT moht, idd,id_avaa WHERE (select * from avas ) not in (SELECT blocker_id from block_user where blocked_id=idd);
SELECT * FROM ava ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `num_like` (IN `idd` INT, IN `is_avva` INT)  BEGIN
CREATE TEMPORARY TABLE num2 SELECT user_id as id ,COUNT(user_id ) as numlike from ava_like where ava_id =is_avva;
create TEMPORARY table block9 select blocker_id as col_id FROM block_user WHERE blocker_id=idd;
select case when id in (select * from block9) THEN 0 ELSE numlike END FROM num2;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `payamhaye_daryafti_karbar` (IN `idd` INT, IN `sender_id` INT)  BEGIN
select  id_ava, mohtava , sender , date from message where (sender =sender_id and receiver=idd and receiver not in (SELECT block_user.blocked_id FROM block_user , ava where ava.user_id = block_user.blocker_id and  id_ava is NOT null)) ORDER BY date DESC;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `send_message` (IN `idd` INT, IN `datee` TIMESTAMP, IN `receiv` INT, IN `id_avaaa` INT, IN `choice` INT, IN `mohtavaa` VARCHAR(256))  BEGIN
case choice WHEN 1 then 
INSERT IGNORE INTO message (date,receiver,sender,id_ava) values (datee, (SELECT id from user_qanari where id=receiv and id  not in (select blocker_id  FROM block_user WHERE blocked_id=idd) and idd not in (SELECT block_user.blocked_id FROM block_user , ava where ava.user_id = block_user.blocker_id and ava.id=id_avaaa)),idd,id_avaaa);
WHEN 2 then 
INSERT INTO message (date,receiver,sender,mohtava) values (datee, (SELECT id  from user_qanari where id=receiv and id  not in (select blocker_id  FROM block_user WHERE blocked_id=idd)),idd,mohtavaa);
end case;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `tavaqof_donbal_kardan` (IN `idd_user` INT, IN `id_unfolow` INT)  BEGIN
	DELETE  from follow where follower_id=idd_user and following_id=id_unfolow;
    SELECT * FROM follow;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `unblock` (IN `idd_user` INT, IN `id_unblock` INT)  BEGIN
DELETE IGNORE from block_user where blocker_id=idd_user and blocked_id=id_unblock;
select * from block_user;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `ava`
--

CREATE TABLE `ava` (
  `id` int(10) UNSIGNED NOT NULL,
  `mohtava` varchar(256) DEFAULT NULL,
  `post_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `user_id` int(10) UNSIGNED NOT NULL,
  `commentonava` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ava`
--

INSERT INTO `ava` (`id`, `mohtava`, `post_date`, `user_id`, `commentonava`) VALUES
(1, 'slm 1', '2021-05-22 11:59:45', 1, NULL),
(2, 'slm 2 ', '2021-05-22 11:59:45', 3, NULL),
(3, 'slm 3', '2021-05-22 11:59:45', 7, NULL),
(4, 'slm 4', '2021-05-22 11:59:45', 1, NULL),
(5, 'slm 5', '2021-05-22 11:59:45', 11, NULL),
(6, 'chetori', '2021-05-22 11:59:45', 2, NULL),
(7, 'chetori', '2021-05-22 11:59:45', 3, NULL),
(8, 'chetori', '2021-05-22 11:59:45', 1, NULL),
(9, 'blabla', '2021-05-22 11:59:45', 1, NULL),
(10, 'slm 1', '2021-05-22 11:59:46', 11, NULL),
(16, 'mrc', '2021-05-23 05:45:14', 1, 3),
(19, 'mrc3', '2021-05-23 05:55:34', 3, 8),
(20, 'mrc', '2021-05-23 06:13:51', 10, 6),
(23, 'ajjb', '2021-06-24 14:04:24', 1, 3),
(26, 'what', '2021-06-24 14:14:07', 1, 3),
(27, 'arya', '2021-07-05 19:57:42', 1, NULL),
(35, 'slm proc', '2021-07-10 17:20:24', 1, 0),
(36, 'dsasdsad', '2021-07-10 17:21:33', 1, 0),
(37, 'a\'sd', '2021-07-10 17:24:10', 1, 0),
(38, 'a\'sd', '2021-07-10 17:24:28', 1, 0),
(39, 'a\'sd', '2021-07-10 17:24:29', 1, 0),
(41, 'lhfdljkdfsa', '2021-07-10 17:30:47', 1, 0),
(42, 'slm ', '2021-07-10 17:53:21', 1, 0),
(43, 'adassadsad', '2021-07-10 17:57:10', 1, 0);

--
-- Triggers `ava`
--
DELIMITER $$
CREATE TRIGGER `add_ava` AFTER INSERT ON `ava` FOR EACH ROW BEGIN

   INSERT INTO trigger_add_ava
   ( user_id,
     ava_id,
   date)
   VALUES
   (NEW.user_id,
     NEW.id,
  NEW.post_date );

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `ava_hashtag`
--

CREATE TABLE `ava_hashtag` (
  `id_ava` int(10) UNSIGNED NOT NULL,
  `id_hashtag` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ava_hashtag`
--

INSERT INTO `ava_hashtag` (`id_ava`, `id_hashtag`) VALUES
(3, 1),
(4, 1),
(9, 1),
(41, 11),
(41, 12),
(42, 13),
(42, 14),
(42, 15),
(42, 16),
(43, 17);

-- --------------------------------------------------------

--
-- Table structure for table `ava_like`
--

CREATE TABLE `ava_like` (
  `ava_id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ava_like`
--

INSERT INTO `ava_like` (`ava_id`, `user_id`) VALUES
(9, 7),
(9, 11);

-- --------------------------------------------------------

--
-- Table structure for table `block_user`
--

CREATE TABLE `block_user` (
  `blocker_id` int(10) UNSIGNED NOT NULL,
  `blocked_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `block_user`
--

INSERT INTO `block_user` (`blocker_id`, `blocked_id`) VALUES
(2, 3),
(3, 7),
(8, 7),
(9, 8),
(11, 1),
(11, 10),
(12, 9),
(12, 10),
(12, 11);

-- --------------------------------------------------------

--
-- Table structure for table `follow`
--

CREATE TABLE `follow` (
  `follower_id` int(10) UNSIGNED NOT NULL,
  `following_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `follow`
--

INSERT INTO `follow` (`follower_id`, `following_id`) VALUES
(1, 2),
(1, 3),
(1, 11),
(2, 3),
(7, 2),
(8, 9),
(10, 11),
(11, 10);

-- --------------------------------------------------------

--
-- Table structure for table `hashtag`
--

CREATE TABLE `hashtag` (
  `id` int(10) UNSIGNED NOT NULL,
  `hashtagstr` char(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hashtag`
--

INSERT INTO `hashtag` (`id`, `hashtagstr`) VALUES
(1, '#ABSDF'),
(2, '#AB5DF'),
(3, '#AcSDs'),
(4, '#AcDsF'),
(11, ''),
(12, ''),
(13, ''),
(14, ''),
(15, ''),
(16, '#ABSDF'),
(17, '#ASDFG');

--
-- Triggers `hashtag`
--
DELIMITER $$
CREATE TRIGGER `add_hashtag` AFTER INSERT ON `hashtag` FOR EACH ROW BEGIN
        INSERT INTO ava_hashtag(id_ava, id_hashtag)
        VALUES((select id from ava ORDER BY id DESC LIMIT 1) , New.id);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `log_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `username`, `log_time`) VALUES
(2, 'hamidA', '2021-05-22 11:24:30'),
(3, 'majidA', '2021-05-22 11:24:30'),
(4, 'aliA', '2021-05-22 11:24:30'),
(5, 'amirA', '2021-05-22 11:24:30'),
(6, 'pouriaA', '2021-05-22 11:24:30'),
(7, 'pouriaA', '2021-05-22 11:24:30'),
(8, 'zahraA', '2021-05-22 11:24:30'),
(9, 'pouriaA', '2021-05-22 11:24:30'),
(10, 'nimaA', '2021-05-22 11:24:30'),
(11, 'pouriaA', '2021-05-22 11:24:30'),
(12, 'aliA', '2021-05-22 11:25:02'),
(13, 'amirA', '2021-05-22 11:25:02'),
(14, 'pouriaA', '2021-05-22 11:25:02'),
(15, 'pouriaA', '2021-05-22 11:25:02'),
(16, 'pouriaA', '2021-06-22 12:10:21'),
(17, 'pouriaA', '2021-06-22 12:15:53'),
(18, 'hamidA', '2021-06-22 12:17:38'),
(53, 'pouriaA', '2021-06-24 14:24:50'),
(54, 'amirA', '2021-06-24 14:50:11'),
(55, 'amirA', '2021-06-24 14:52:17'),
(56, 'pouriaA', '2021-07-04 15:43:23'),
(57, 'pouriaA', '2021-07-04 16:46:00'),
(58, 'pouriaA', '2021-07-04 16:47:23'),
(59, 'pouriaA', '2021-07-04 16:48:22'),
(60, 'pouriaA', '2021-07-04 17:19:35'),
(61, 'pouriaA', '2021-07-04 17:20:18'),
(62, 'majidA', '2021-07-04 19:52:02'),
(63, 'majidA', '2021-07-04 19:52:56'),
(64, 'aliA', '2021-07-04 19:56:36'),
(65, 'aliA', '2021-07-04 20:00:39'),
(66, 'hamidA', '2021-07-04 20:27:53'),
(67, 'akbarA', '2021-07-04 20:41:31'),
(68, 'akbarA', '2021-07-04 20:42:06'),
(69, 'pouriaA', '2021-07-04 23:02:52'),
(70, 'hamidA', '2021-07-04 23:08:33'),
(71, 'pouriaA', '2021-07-05 19:56:32'),
(72, 'pouriaA', '2021-07-05 19:57:37'),
(73, 'pouriaA', '2021-07-05 20:40:36'),
(74, 'pouriaA', '2021-07-05 20:41:25'),
(75, 'pouriaA', '2021-07-05 20:46:07'),
(76, 'pouriaA', '2021-07-07 06:51:55'),
(77, 'pouriaA', '2021-07-07 06:52:53'),
(78, 'pouriaA', '2021-07-07 06:53:28'),
(79, 'pouriaA', '2021-07-07 06:55:00'),
(80, 'pouriaA', '2021-07-07 06:55:37'),
(81, 'pouriaA', '2021-07-07 06:56:03'),
(82, 'aliA', '2021-07-07 06:56:41'),
(83, 'pouriaA', '2021-07-07 07:01:43'),
(84, 'pouriaA', '2021-07-07 07:02:21'),
(85, 'pouriaA', '2021-07-07 07:03:32'),
(86, 'pouriaA', '2021-07-07 07:03:54'),
(87, 'pouriaA', '2021-07-07 07:04:21'),
(88, 'pouriaA', '2021-07-07 07:06:52'),
(89, 'pouriaA', '2021-07-07 07:07:32'),
(90, 'pouriaA', '2021-07-07 07:14:22'),
(91, 'pouriaA', '2021-07-07 07:15:47'),
(92, 'pouriaA', '2021-07-07 07:16:35'),
(93, 'pouriaA', '2021-07-07 07:26:15'),
(94, 'pouriaA', '2021-07-07 07:27:08'),
(95, 'pouriaA', '2021-07-07 07:28:31'),
(99, 'pouriaA', '2021-07-07 08:37:25'),
(100, 'pouriaA', '2021-07-07 08:57:43'),
(101, 'pouriaA', '2021-07-07 08:58:13'),
(102, 'pouriaA', '2021-07-07 08:58:52'),
(103, 'pouriaA', '2021-07-07 08:59:16'),
(104, 'pouriaA', '2021-07-07 10:53:03'),
(105, 'pouriaA', '2021-07-07 10:54:55'),
(106, 'pouriaA', '2021-07-07 10:55:27'),
(107, 'pouriaA', '2021-07-07 11:05:11'),
(108, 'pouriaA', '2021-07-07 11:06:59'),
(109, 'pouriaA', '2021-07-07 11:07:25'),
(110, 'pouriaA', '2021-07-07 11:09:45'),
(111, 'pouriaA', '2021-07-07 11:10:36'),
(112, 'pouriaA', '2021-07-07 11:11:29'),
(113, 'pouriaA', '2021-07-07 11:12:08'),
(114, 'pouriaA', '2021-07-07 11:12:34'),
(115, 'pouriaA', '2021-07-07 11:17:33'),
(116, 'pouriaA', '2021-07-07 11:18:20'),
(117, 'pouriaA', '2021-07-07 11:21:44'),
(118, 'pouriaA', '2021-07-07 11:22:58'),
(119, 'pouriaA', '2021-07-07 11:23:24'),
(120, 'hamidA', '2021-07-07 11:29:41'),
(121, 'hamidA', '2021-07-07 11:34:39'),
(122, 'hamidA', '2021-07-07 11:35:43'),
(123, 'hamidA', '2021-07-07 11:37:52'),
(124, 'hamidA', '2021-07-07 11:39:53'),
(125, 'hamidA', '2021-07-07 11:41:30'),
(126, 'hamidA', '2021-07-07 11:43:02'),
(127, 'hamidA', '2021-07-07 11:45:14'),
(128, 'pouriaA', '2021-07-07 11:50:27'),
(129, 'pouriaA', '2021-07-07 11:50:41'),
(130, 'pouriaA', '2021-07-07 11:56:30'),
(131, 'pouriaA', '2021-07-07 11:57:52'),
(132, 'pouriaA', '2021-07-07 11:58:11'),
(133, 'pouriaA', '2021-07-07 11:59:03'),
(134, 'pouriaA', '2021-07-07 12:08:24'),
(135, 'pouriaA', '2021-07-07 12:12:46'),
(136, 'pouriaA', '2021-07-07 12:16:29'),
(137, 'akbarA', '2021-07-07 12:16:41'),
(138, 'akbarA', '2021-07-07 12:18:40'),
(139, 'akbarA', '2021-07-07 12:19:15'),
(140, 'pouriaA', '2021-07-07 13:40:38'),
(141, 'akbarA', '2021-07-07 13:44:42'),
(142, 'akbarA', '2021-07-07 13:46:29'),
(143, 'akbarA', '2021-07-07 13:47:26'),
(144, 'pouriaA', '2021-07-07 13:48:22'),
(145, 'pouriaA', '2021-07-07 13:51:22'),
(146, 'hamidA', '2021-07-07 13:51:43'),
(147, 'hamidA', '2021-07-07 13:52:24'),
(148, 'hamidA', '2021-07-07 13:57:16'),
(149, 'hamidA', '2021-07-07 14:04:50'),
(150, 'hamidA', '2021-07-07 14:06:43'),
(151, 'akbarA', '2021-07-07 14:08:56'),
(152, 'akbarA', '2021-07-07 14:09:49'),
(153, 'akbarA', '2021-07-07 14:15:46'),
(154, 'hamidA', '2021-07-07 14:20:07'),
(155, 'akbarA', '2021-07-07 14:20:41'),
(156, 'hamidA', '2021-07-07 14:21:18'),
(157, 'mehdiA', '2021-07-07 14:30:12'),
(158, 'mehdiA', '2021-07-07 14:34:02'),
(159, 'pouriaA', '2021-07-07 14:59:20'),
(160, 'aliA', '2021-07-07 15:01:20'),
(161, 'pouriaA', '2021-07-07 15:22:26'),
(162, 'pouriaA', '2021-07-07 15:24:18'),
(163, 'pouriaA', '2021-07-07 15:26:16'),
(164, 'pouriaA', '2021-07-07 15:27:19'),
(165, 'pouriaA', '2021-07-07 15:30:34'),
(166, 'pouriaA', '2021-07-07 15:31:11'),
(167, 'pouriaA', '2021-07-07 15:31:53'),
(168, 'aliA', '2021-07-07 15:34:04'),
(169, 'pouriaA', '2021-07-10 17:09:17'),
(170, 'aliA', '2021-07-10 17:12:26'),
(171, 'pouriaA', '2021-07-10 17:15:08'),
(172, 'pouriaA', '2021-07-10 17:16:46'),
(173, 'aliA', '2021-07-10 17:17:58'),
(174, 'pouriaA', '2021-07-10 17:18:38'),
(175, 'pouriaA', '2021-07-10 17:28:18'),
(176, 'pouriaA', '2021-07-10 17:30:35'),
(177, 'pouriaA', '2021-07-10 17:53:05'),
(178, 'pouriaA', '2021-07-10 17:57:02');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `id` int(10) UNSIGNED NOT NULL,
  `mohtava` varchar(256) NOT NULL,
  `sender` int(10) UNSIGNED NOT NULL,
  `receiver` int(10) UNSIGNED NOT NULL,
  `id_ava` int(10) UNSIGNED DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`id`, `mohtava`, `sender`, `receiver`, `id_ava`, `date`) VALUES
(8, 'slm chetorr?', 3, 7, NULL, '2020-06-08 19:30:00'),
(9, 'slm chetori?', 3, 8, NULL, '2002-05-08 19:30:00'),
(11, 'slm chetorr?', 3, 7, NULL, '2020-06-08 19:30:00'),
(12, 'slm chetori?', 3, 8, NULL, '2002-05-08 19:30:00'),
(14, 'slm chetorr?', 3, 7, NULL, '2020-06-08 19:30:00'),
(15, 'slm chetori?', 3, 8, NULL, '2002-05-08 19:30:00'),
(17, 'slm chetorr?', 3, 7, NULL, '2020-06-08 19:30:00'),
(18, 'slm chetori?', 3, 8, NULL, '2002-05-08 19:30:00'),
(19, 'slm chetori?', 2, 1, NULL, '2020-08-08 19:30:00'),
(20, 'slm chetori?', 2, 11, NULL, '2020-07-08 19:30:00'),
(21, '', 3, 9, 1, '2020-08-08 19:30:00'),
(22, '', 3, 9, 1, '2020-08-08 19:30:00'),
(25, 'slm chetori?', 3, 12, NULL, '2020-07-08 19:30:00'),
(26, '', 3, 12, 1, '2020-10-08 20:30:00'),
(27, '', 3, 9, 1, '2020-08-08 19:30:00'),
(28, '', 3, 9, 1, '2020-08-08 19:30:00'),
(29, '', 3, 9, 1, '2020-08-09 19:30:00'),
(30, '', 3, 9, 1, '2020-10-09 20:30:00'),
(31, 'python', 2, 1, NULL, '2020-11-10 20:30:00'),
(32, '', 1, 3, 9, '1999-12-11 20:30:00'),
(33, 'salam GUI', 1, 3, NULL, '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `trigger_add_ava`
--

CREATE TABLE `trigger_add_ava` (
  `USER_id` int(11) DEFAULT NULL,
  `ava_id` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trigger_add_ava`
--

INSERT INTO `trigger_add_ava` (`USER_id`, `ava_id`, `date`) VALUES
(1, 27, '2021-07-05 19:57:42'),
(1, 30, '2021-07-07 14:59:28'),
(1, 35, '2021-07-10 17:20:24'),
(1, 36, '2021-07-10 17:21:33'),
(1, 37, '2021-07-10 17:24:10'),
(1, 38, '2021-07-10 17:24:28'),
(1, 39, '2021-07-10 17:24:29'),
(1, 41, '2021-07-10 17:30:47'),
(1, 42, '2021-07-10 17:53:21'),
(1, 43, '2021-07-10 17:57:10');

-- --------------------------------------------------------

--
-- Table structure for table `trigger_add_user`
--

CREATE TABLE `trigger_add_user` (
  `USERname` varchar(20) NOT NULL,
  `regdate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trigger_add_user`
--

INSERT INTO `trigger_add_user` (`USERname`, `regdate`) VALUES
('3', '2021-07-07 15:26:34'),
('sda', '2021-07-07 14:54:15');

-- --------------------------------------------------------

--
-- Table structure for table `user_qanari`
--

CREATE TABLE `user_qanari` (
  `id` int(10) UNSIGNED NOT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  `pass` varchar(128) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `birthdate` date DEFAULT NULL,
  `biography` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_qanari`
--

INSERT INTO `user_qanari` (`id`, `fname`, `lname`, `username`, `pass`, `reg_date`, `birthdate`, `biography`) VALUES
(1, 'pouria', 'ahmadi', 'pouriaA', '50930cad463b9334ea3be34fdff2dfef620a5f22', '2021-05-22 11:19:21', '2001-05-15', 'new member'),
(2, 'ali', 'ahmadi', 'aliA', '66f4a5fdce45bed1b1b99474956e530c4671c3a7', '2021-05-22 11:19:21', '2002-05-15', 'new mwmber'),
(3, 'majid', 'ahmadi', 'majidA', 'b747cda10777471aa19a6f2771d9734e2319fbc0', '2021-05-22 11:19:21', '2003-05-15', 'new student'),
(7, 'hamid', 'ahmadi', 'hamidA', '813a7fa2d3316889307794346ed9a3ac669ff175', '2021-05-22 11:20:17', '2004-05-15', 'new student'),
(8, 'zahra', 'ahmadi', 'zahraA', '9e823d192e376d1a7a38661e3712bd2e2ace5959', '2021-05-22 11:20:17', '1999-05-15', 'new student'),
(9, 'nima', 'ahmadi', 'nimaA', '04855546b135ba23850cf7f68a54b166780c4936', '2021-05-22 11:20:17', '2001-06-15', 'new student'),
(10, 'mehdi', 'ahmadi', 'mehdiA', '56dc9fdb6fa1ab407d4817109f7eef6ed720349f', '2021-05-22 11:20:17', '2011-05-15', 'new student'),
(11, 'amir', 'ahmadi', 'amirA', 'a5f6684309aac0e065e78f559531c8c6bb62f605', '2021-05-22 11:20:17', '2001-05-25', 'new student'),
(12, 'akbar', 'ahmadi', 'akbarA', '7e22dda6fd68ac3c3035d3545c01723b46bf6b00', '2021-05-22 11:20:17', '2001-05-20', 'nothing to say');

--
-- Triggers `user_qanari`
--
DELIMITER $$
CREATE TRIGGER `add_user` AFTER INSERT ON `user_qanari` FOR EACH ROW BEGIN

   INSERT INTO trigger_add_user
   ( username,
     regdate)
   VALUES
   (NEW.username,
     NEW.reg_date );

END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ava`
--
ALTER TABLE `ava`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_avauser` (`user_id`);

--
-- Indexes for table `ava_hashtag`
--
ALTER TABLE `ava_hashtag`
  ADD PRIMARY KEY (`id_ava`,`id_hashtag`),
  ADD KEY `FK_hashtag` (`id_hashtag`);

--
-- Indexes for table `ava_like`
--
ALTER TABLE `ava_like`
  ADD PRIMARY KEY (`user_id`,`ava_id`),
  ADD KEY `FK_avalike` (`ava_id`);

--
-- Indexes for table `block_user`
--
ALTER TABLE `block_user`
  ADD PRIMARY KEY (`blocker_id`,`blocked_id`),
  ADD KEY `FK_blocked` (`blocked_id`);

--
-- Indexes for table `follow`
--
ALTER TABLE `follow`
  ADD PRIMARY KEY (`follower_id`,`following_id`),
  ADD KEY `FK_following` (`following_id`);

--
-- Indexes for table `hashtag`
--
ALTER TABLE `hashtag`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_username` (`username`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_senderuser` (`sender`),
  ADD KEY `FK_receiveruser` (`receiver`),
  ADD KEY `FK_avames` (`id_ava`);

--
-- Indexes for table `trigger_add_ava`
--
ALTER TABLE `trigger_add_ava`
  ADD PRIMARY KEY (`ava_id`);

--
-- Indexes for table `trigger_add_user`
--
ALTER TABLE `trigger_add_user`
  ADD PRIMARY KEY (`USERname`);

--
-- Indexes for table `user_qanari`
--
ALTER TABLE `user_qanari`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ava`
--
ALTER TABLE `ava`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `hashtag`
--
ALTER TABLE `hashtag`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=179;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `user_qanari`
--
ALTER TABLE `user_qanari`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ava`
--
ALTER TABLE `ava`
  ADD CONSTRAINT `FK_avauser` FOREIGN KEY (`user_id`) REFERENCES `user_qanari` (`id`);

--
-- Constraints for table `ava_hashtag`
--
ALTER TABLE `ava_hashtag`
  ADD CONSTRAINT `FK_ava` FOREIGN KEY (`id_ava`) REFERENCES `ava` (`id`),
  ADD CONSTRAINT `FK_hashtag` FOREIGN KEY (`id_hashtag`) REFERENCES `hashtag` (`id`);

--
-- Constraints for table `ava_like`
--
ALTER TABLE `ava_like`
  ADD CONSTRAINT `FK_avalike` FOREIGN KEY (`ava_id`) REFERENCES `ava` (`id`),
  ADD CONSTRAINT `FK_userlike` FOREIGN KEY (`user_id`) REFERENCES `user_qanari` (`id`);

--
-- Constraints for table `block_user`
--
ALTER TABLE `block_user`
  ADD CONSTRAINT `FK_blocked` FOREIGN KEY (`blocked_id`) REFERENCES `user_qanari` (`id`),
  ADD CONSTRAINT `FK_blocker` FOREIGN KEY (`blocker_id`) REFERENCES `user_qanari` (`id`);

--
-- Constraints for table `follow`
--
ALTER TABLE `follow`
  ADD CONSTRAINT `FK_follower` FOREIGN KEY (`follower_id`) REFERENCES `user_qanari` (`id`),
  ADD CONSTRAINT `FK_following` FOREIGN KEY (`following_id`) REFERENCES `user_qanari` (`id`);

--
-- Constraints for table `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `FK_username` FOREIGN KEY (`username`) REFERENCES `user_qanari` (`username`);

--
-- Constraints for table `message`
--
ALTER TABLE `message`
  ADD CONSTRAINT `FK_avames` FOREIGN KEY (`id_ava`) REFERENCES `ava` (`id`),
  ADD CONSTRAINT `FK_receiveruser` FOREIGN KEY (`receiver`) REFERENCES `user_qanari` (`id`),
  ADD CONSTRAINT `FK_senderuser` FOREIGN KEY (`sender`) REFERENCES `user_qanari` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
