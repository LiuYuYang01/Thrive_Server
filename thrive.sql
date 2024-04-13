-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: thrive_d
-- ------------------------------------------------------
-- Server version	8.0.35

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


create database thrive;
use thrive;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `title` varchar(100) NOT NULL COMMENT '文章标题',
  `description` varchar(200) DEFAULT NULL COMMENT '文章介绍',
  `content` text NOT NULL COMMENT '文章主要内容',
  `cover` varchar(300) DEFAULT NULL COMMENT '文章封面',
  `view` int DEFAULT NULL COMMENT '文章浏览量',
  `cids` varchar(255) DEFAULT NULL COMMENT '该文章所绑定的分类ID',
  `tag` varchar(100) DEFAULT NULL COMMENT '文章标签',
  `create_time` datetime DEFAULT NULL COMMENT '文章创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'Vue.js 3.0新特性介绍','本文介绍了Vue.js 3.0的新特性，包括Composition API、Teleport、Suspense等','# Vue.js 3.0新特性介绍\r\n\r\nVue.js是一款流行的JavaScript框架，用于构建用户界面。它在3.0版本中引入了一些令人兴奋的新特性，使得开发者能够更加高效地构建现代化的Web应用程序。本文将介绍Vue.js 3.0的一些重要特性。\r\n\r\n## Composition API\r\n\r\nVue.js 3.0引入了Composition API，这是一个全新的API风格，旨在提供更灵活、更可组合的代码复用方式。相比于以往的Options API，Composition API允许开发者通过函数的形式组织代码逻辑，使得代码更易于理解和维护。开发者可以根据需要将相关的逻辑组合在一起，而不需要按照生命周期钩子将它们分散在不同的选项中。\r\n\r\n下面是一个使用Composition API的示例：\r\n\r\n```javascript\r\nimport { ref, reactive, computed } from \'vue\';\r\n\r\nexport default {\r\n  setup() {\r\n    const count = ref(0);\r\n    const state = reactive({\r\n      message: \'Hello, Vue.js 3.0!\',\r\n    });\r\n\r\n    const doubleCount = computed(() => count.value * 2);\r\n\r\n    function increment() {\r\n      count.value++;\r\n    }\r\n\r\n    return {\r\n      count,\r\n      state,\r\n      doubleCount,\r\n      increment,\r\n    };\r\n  },\r\n};\r\n```\r\n\r\n## 更好的性能\r\n\r\nVue.js 3.0在性能方面进行了一系列的优化，使得应用程序的渲染速度更快、内存占用更少。其中最显著的改进是使用了Proxy对象来替代Object.defineProperty，这使得Vue.js能够更高效地追踪数据的变化。此外，Vue.js 3.0还引入了静态树提升（Static Tree Hoisting）和基于模板的优化（Template-based Optimization）等技术，进一步提升了应用程序的性能。\r\n\r\n## 更好的TypeScript支持\r\n\r\nVue.js 3.0对TypeScript的支持也得到了改进。新版本中的TypeScript声明文件提供了更准确的类型推断和类型检查，使得开发者能够更轻松地编写类型安全的Vue.js应用程序。此外，Vue.js 3.0还引入了一些新的TypeScript API，如`defineComponent`和`defineProps`，以提供更好的类型支持。\r\n\r\n下面是一个使用TypeScript的示例：\r\n\r\n```typescript\r\nimport { defineComponent, defineProps } from \'vue\';\r\n\r\ninterface Props {\r\n  name: string;\r\n}\r\n\r\nexport default defineComponent({\r\n  props: defineProps<Props>(),\r\n  setup(props) {\r\n    return {\r\n      greet: `Hello, ${props.name}!`,\r\n    };\r\n  },\r\n});\r\n```\r\n\r\n## 更小的包体积\r\n\r\nVue.js 3.0还对包体积进行了优化。由于使用了Tree-shaking技术，新版本中的Vue.js只包含了实际使用到的代码，减少了不必要的代码体积。此外，Vue.js 3.0还支持按需加载，使得开发者可以只引入需要的功能模块，进一步减小了包体积。\r\n\r\n下面是一个按需加载的示例：\r\n\r\n```javascript\r\nimport { createApp } from \'vue\';\r\nimport { Button, Input } from \'ant-design-vue\';\r\n\r\nconst app = createApp();\r\n\r\napp.use(Button);\r\napp.use(Input);\r\n\r\napp.mount(\'#app\');\r\n```\r\n\r\n## 更好的开发者工具\r\n\r\nVue.js 3.0提供了一系列新的开发者工具，使得开发者能够更轻松地调试和优化应用程序。新版本中的Devtools提供了更多的功能，如组件树的可视化、性能分析、事件追踪等。此外，Vue.js 3.0还引入了新的警告系统，使得开发者能够更容易地发现和修复潜在的问题。\r\n\r\n总结\r\n\r\nVue.js 3.0引入了许多令人兴奋的新特性，包括Composition API、更好的性能、更好的TypeScript支持、更小的包体积和更好的开发者工具。这些特性使得开发者能够更加高效地构建现代化的Web应用程序。如果你还没有尝试Vue.js 3.0，现在是时候开始了！','http://code.liuyuyang.net/usr/uploads/2023/09/1813156470.png',44,'2','Nodejs','2023-10-25 04:00:00'),(2,'Java 15新特性详解','本文介绍了Java 15的新特性，包括ZGC、Records、Text Blocks等','# Java 15新特性详解\nJava 15是Java语言的最新版本，它带来了一些非常实用的新特性。其中最重要的特性是ZGC，它是一种高效的垃圾回收器，可以大大提高Java应用程序的性能和可靠性。此外，Records和Text Blocks也是非常有用的新特性，它们可以帮助我们更好地处理数据和字符串。','http://code.liuyuyang.net/usr/uploads/2023/09/192808003.jpg',17,'4,5,7,9','Java','2023-10-23 10:00:00'),(3,'Python爬虫实战教程','本文介绍了Python爬虫的基本原理和实战技巧','Python是一种非常流行的编程语言，它在数据处理和网络爬虫方面有着广泛的应用。本文将介绍Python爬虫的基本原理和实战技巧，包括如何使用Python的requests和beautifulsoup库来爬取网页数据，如何处理JSON和XML格式的数据，以及如何使用selenium库模拟用户行为。','http://code.liuyuyang.net/usr/uploads/2023/09/2620013322.jpeg',1,'4','Python','2023-10-22 08:00:00'),(4,'前端性能优化的10个技巧','本文介绍了前端性能优化的10个实用技巧，包括减少HTTP请求、使用CDN、优化图片等','前端性能优化是Web开发中非常重要的一环，它可以提高网站的加载速度和用户体验。本文将介绍10个实用的前端性能优化技巧，包括减少HTTP请求、使用CDN、优化图片、使用缓存、压缩代码等。这些技巧可以帮助开发者更好地优化自己的网站，提高用户满意度。','',0,'4','性能优化','2023-10-21 14:00:00'),(5,'使用Docker部署Java应用程序','本文介绍了如何使用Docker来部署Java应用程序','Docker是一种非常流行的容器化技术，它可以帮助开发者更好地管理和部署应用程序。本文将介绍如何使用Docker来部署Java应用程序，包括如何编写Dockerfile、如何构建和运行Docker镜像、如何使用Docker Compose来管理多个容器等。这些技巧可以帮助开发者更好地管理自己的Java应用程序，提高开发效率。','',0,'4','Java','2023-10-20 16:00:00'),(6,'前端开发入门指南','本文介绍了前端开发的基本概念和技术栈，适合初学者入门。','前端开发是指利用HTML、CSS和JavaScript等技术，开发网站的用户界面部分。它负责将网站的设计和用户交互变成可视化的界面，为用户提供优秀的用户体验。','',0,'4','入门','2023-01-01 10:00:00'),(7,'Vue.js实战教程','本文通过实例演示了如何使用Vue.js构建现代化的Web应用程序。','Vue.js是一个用于构建用户界面的渐进式JavaScript框架。它易于学习、灵活且高效，被广泛应用于前端开发领域。本文从基础概念到高级特性，详细介绍了Vue.js的使用方法。','http://code.liuyuyang.net/usr/uploads/2023/09/1813156470.png',0,'4','Vue.js','2023-02-01 14:00:00'),(8,'Java入门指南','本文介绍了Java编程语言的基本概念和语法，适合初学者入门。','Java是一种通用的高级编程语言，具有跨平台、面向对象和安全性等特点。它被广泛应用于企业级应用开发、移动应用开发和大数据处理等领域。本文从安装到编写简单程序，全面讲解了Java的入门知识。','http://code.liuyuyang.net/usr/uploads/2023/09/192808003.jpg',0,'4','入门','2023-03-01 12:00:00'),(9,'Python数据分析实战','本文介绍了使用Python进行数据分析的基本方法和常用工具，适合数据分析初学者。','Python是一种简单易学且功能强大的编程语言，被广泛应用于数据科学和机器学习领域。本文通过实例演示了如何使用Python进行数据清洗、数据可视化和机器学习建模等任务。','http://code.liuyuyang.net/usr/uploads/2023/09/2620013322.jpeg',0,'4','数据分析','2023-04-01 16:00:00'),(10,'深入理解MySQL数据库','本文深入介绍了MySQL数据库的架构、优化和高级特性，适合有一定数据库基础的开发人员。','MySQL是一种常用的关系型数据库管理系统，被广泛应用于Web应用程序和企业级系统。本文从数据库设计到性能优化，详细讲解了MySQL的各个方面，帮助读者更好地理解和使用MySQL。','',7,'4','MySQL','2023-05-01 18:00:00');
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cate`
--

DROP TABLE IF EXISTS `cate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL COMMENT '分类名称',
  `icon` varchar(100) DEFAULT NULL COMMENT '分类图标',
  `url` varchar(255) DEFAULT NULL COMMENT '分类链接',
  `mark` varchar(100) NOT NULL COMMENT '分类标识',
  `level` int DEFAULT NULL COMMENT '分类级别',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE,
  UNIQUE KEY `cate_pk` (`mark`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cate`
--

LOCK TABLES `cate` WRITE;
/*!40000 ALTER TABLE `cate` DISABLE KEYS */;
INSERT INTO `cate` VALUES (1,'开发笔记','🎉','/','kfbj',0),(2,'生活随笔','✍️','/','shsb',0),(4,'大前端','🎉','http://127.0.0.1:5000','dqd',0),(5,'前端','?','/','qd',4),(7,'Java','?','/','java',4),(9,'Python','?','/','python',4);
/*!40000 ALTER TABLE `cate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room` int NOT NULL,
  `data` json NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `chat_pk_2` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (18,10001,'{\"date\": \"2023-05-25\", \"name\": \"宇阳\", \"avatar\": \"https://api.dicebear.com/7.x/fun-emoji/svg?seed=Lilly\", \"content\": \"Hello! 有什么要对我说的吗?\"}'),(19,10003,'{\"date\": \"2023-05-25\", \"name\": \"神秘人\", \"avatar\": \"https://api.dicebear.com/7.x/fun-emoji/svg?seed=Lilly\", \"content\": \"大家可以在这里提交你的需求以及宝贵的建议\"}'),(20,10004,'{\"date\": \"2023-05-25\", \"name\": \"神秘人\", \"avatar\": \"https://api.dicebear.com/7.x/fun-emoji/svg?seed=Lilly\", \"content\": \"抢沙发\"}'),(21,10002,'{\"date\": \"2023-05-25\", \"name\": \"神秘人\", \"avatar\": \"https://api.dicebear.com/7.x/fun-emoji/svg?seed=Lilly\", \"content\": \"占楼\"}');
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `avatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `aid` int NOT NULL,
  `rid` int NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `audit` int DEFAULT '0' COMMENT '是否审核',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (36,'神秘人','https://q1.qlogo.cn/g?b=qq&nk=3311118881&s=640','测试评论','3311118881@qq.com','http://127.0.0.1:5173/',1,0,'2023-11-24 08:13:59',1),(37,'神秘人2号','https://q1.qlogo.cn/g?b=qq&nk=2518848232&s=640','测试回复评论','2518848232@qq.com','http://127.0.0.1:5173/',0,36,'2023-11-24 08:14:22',1),(38,'神秘人2号','https://q1.qlogo.cn/g?b=qq&nk=2518848232&s=640','第二条评论','2518848232@qq.com','http://127.0.0.1:5173/',1,0,'2023-11-24 08:14:32',1),(50,'神秘人3号','https://q1.qlogo.cn/g?b=qq&nk=754443568&s=640','三级','754443568@qq.com','http://127.0.0.1:5173/',0,37,'2023-11-24 09:27:37',0),(55,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,0,'2024-03-26 02:31:18',1),(56,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,55,'2024-03-26 02:31:18',1),(57,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,56,'2024-03-26 02:31:18',1),(58,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,55,'2024-03-26 02:31:18',1),(59,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,56,'2024-03-26 02:31:18',1),(60,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,56,'2024-03-26 02:31:18',1),(61,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,56,'2024-03-26 02:31:18',1),(62,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,0,'2024-03-26 02:31:18',1),(63,'刘宇阳','https://liuyuyang.net/avatar.jpg','123','liuyuyang1024@163.com','',1,0,'2024-03-26 02:31:18',1),(64,'神秘人','','写的不错','liuyuyang1024@163.com','',1,0,'2024-03-26 09:47:03',1),(65,'神秘人','https://q1.qlogo.cn/g?b=qq&nk=liuyuyang1024&s=640','123','liuyuyang1024@163.com','',1,0,'2024-03-26 09:51:58',0);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `link`
--

DROP TABLE IF EXISTS `link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `link` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `type` int NOT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `link`
--

LOCK TABLES `link` WRITE;
/*!40000 ALTER TABLE `link` DISABLE KEYS */;
INSERT INTO `link` VALUES (6,'Thrive','记录一个架构师的崛起','3311118881@qq.com','https://q1.qlogo.cn/g?b=qq&nk=3311118881&s=640','/',2,'2023-10-02 18:54:44'),(7,'张洪Heo','分享设计与科技生活','3311118881@qq.com','https://bu.dusays.com/2022/12/28/63ac2812183aa.png','https://blog.zhheo.com/',1,'2023-10-02 18:54:44'),(8,'友人C','友人C的个人空间','3311118881@qq.com','https://s1.ax1x.com/2023/06/02/p9zTn0O.png','http://space.eyescode.top',2,'2023-10-02 18:54:44'),(9,'秦枫鸢梦','花有重开日，人无再少年','3311118881@qq.com','https://blog.zwying.com/avatar.jpg','https://blog.zwying.com',1,'2023-10-02 18:54:44'),(10,'生活倒影','这是一个 Vue2 Vue3 与 SpringBoot 结合的产物','3311118881@qq.com','https://s1.ax1x.com/2022/11/10/z9E7X4.jpg','https://poetize.cn/',1,'2023-10-02 18:54:44'),(11,'心月云','须知少时凌云志，曾许人间第一流','3311118881@qq.com','https://wch666.com/head.png','https://wch666.com',1,'2023-10-02 18:54:44'),(12,'一克猫','一只微不足道的猫','3311118881@qq.com','https://cravatar.cn/avatar/7adbfaef92d9d082be5dec39f3fe3d02?s=200','https://www.1gcat.com',2,'2023-10-02 18:54:44'),(13,'频率','风卷过的起点','3311118881@qq.com','https://cravatar.cn/avatar/cc763511474fe24ffcc80257fb7cb970?s=256','https://pinlyu.com/',1,'2023-10-02 18:54:44'),(14,'青灯暮雨','再渺小的星光，也有属于它的光芒','3311118881@qq.com','https://www.blatr.cn/images/adminAvatar.jpg','https://www.blatr.cn',1,'2023-10-02 18:54:44'),(15,'相左','心有山海，静而不争','3311118881@qq.com','https://qiniu.ztyang.com/img/wechatavatar.jpg','https://www.ztyang.com',1,'2023-10-02 18:54:44'),(16,'Echo’s blog','韶华不为少年留 恨悠悠 几时休','3311118881@qq.com','https://yy.liveout.cn/photo/photo2.jpg','https://www.liveout.cn/index/',1,'2023-10-02 18:54:44'),(17,'奇异纬度','不曾与你分享的时间，我在进步','3311118881@qq.com','https://blog.isww.cn/logo.head.jpg','https://blog.isww.cn/',1,'2023-10-02 18:54:44'),(18,'正物博客','一场凡梦，一份追求','3311118881@qq.com','https://www.zwbo.com/tx.png','https://www.zwbo.com/',2,'2023-10-02 18:54:44'),(19,'HONG的小站','或许是个二次元','3311118881@qq.com','https://blog.zwying.com/usr/uploads/sina/63adb58e798d4.jpg','https://hongweblog.com/',1,'2023-10-02 18:54:44'),(26,'11','22','3311118881@qq.com','44','66',2,'2024-02-07 13:21:55');
/*!40000 ALTER TABLE `link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swiper`
--

DROP TABLE IF EXISTS `swiper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `swiper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swiper`
--

LOCK TABLES `swiper` WRITE;
/*!40000 ALTER TABLE `swiper` DISABLE KEYS */;
INSERT INTO `swiper` VALUES (1,'半山腰的风景很美，然而我还是更想到山顶看看','The scenery halfway up the mountain is beautiful, but I still prefer to see the mountaintop','https://bu.dusays.com/2023/11/10/654e2cf6055b0.jpg','/'),(14,'ces','ces','https://bu.dusays.com/2023/11/05/65473822495c8.jpg','/');
/*!40000 ALTER TABLE `swiper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (3,'Nodejs'),(4,'Python'),(5,'Java'),(6,'Element ui'),(7,'Vue3'),(8,'React'),(10,'Django'),(11,'Flask'),(12,'JavaScript'),(13,'HTML'),(14,'CSS'),(15,'Ajax'),(16,'axios'),(17,'全栈开发'),(54,'大前端'),(63,'123'),(65,'88'),(66,'生活随笔'),(67,'Mybatis');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL COMMENT '类型名称',
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_pk_2` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='网站类型';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'生活类'),(2,'技术类');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL COMMENT '用户名',
  `password` varchar(50) DEFAULT NULL COMMENT '密码',
  `name` varchar(50) NOT NULL COMMENT '用户名称',
  `email` varchar(100) NOT NULL COMMENT '用户邮箱',
  `avatar` varchar(255) NOT NULL COMMENT '用户头像',
  `info` varchar(255) NOT NULL COMMENT '用户介绍',
  `role` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `create_time` datetime DEFAULT NULL COMMENT '用户创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `user_pk` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'liuyuyang','4297f44b13955235245b2497399d7a93','宇阳','3311118881@qq.com','https://liuyuyang.net/avatar.jpg','再渺小的星光，也有属于他的光芒!','admin','2024-01-22 18:32:30');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-08 14:59:27
