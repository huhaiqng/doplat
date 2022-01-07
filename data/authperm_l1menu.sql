/*
 Navicat Premium Data Transfer

 Source Server         : YW-192.168.40.185
 Source Server Type    : MySQL
 Source Server Version : 50727
 Source Host           : 192.168.40.185:3306
 Source Schema         : doplat

 Target Server Type    : MySQL
 Target Server Version : 50727
 File Encoding         : 65001

 Date: 07/01/2022 14:59:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for authperm_l1menu
-- ----------------------------
DROP TABLE IF EXISTS `authperm_l1menu`;
CREATE TABLE `authperm_l1menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `redirect` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `icon` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  UNIQUE INDEX `path`(`path`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of authperm_l1menu
-- ----------------------------
INSERT INTO `authperm_l1menu` VALUES (2, 'AuthPermission', '认证权限', '/authperm', '/authperm/user', 'password', 100);
INSERT INTO `authperm_l1menu` VALUES (3, 'gitlab', 'Gitlab', '/gitlabrepo', '/project/gitlabrepo', 'example', 80);
INSERT INTO `authperm_l1menu` VALUES (4, 'domain', '域名', '/domain', '/domain/gainhon666', 'excel', 90);
INSERT INTO `authperm_l1menu` VALUES (5, 'schedule', '定时任务', '/schedule', '/schedule/taskresult', 'international', 60);
INSERT INTO `authperm_l1menu` VALUES (6, 'resource', '资源管理', '/resource', '/resource/host', 'component', 50);
INSERT INTO `authperm_l1menu` VALUES (7, 'account', '账号管理', '/account', '/account/index', 'peoples', 99);
INSERT INTO `authperm_l1menu` VALUES (8, 'project', '项目管理', '/project', '/project/project', 'table', 51);
INSERT INTO `authperm_l1menu` VALUES (9, 'jenkinsjob', 'Jenkins 任务', '/jenkinsjob', '/project/jenkinsjob', 'link', 70);

SET FOREIGN_KEY_CHECKS = 1;
