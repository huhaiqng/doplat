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

 Date: 07/01/2022 15:00:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for authperm_l2menu
-- ----------------------------
DROP TABLE IF EXISTS `authperm_l2menu`;
CREATE TABLE `authperm_l2menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `component` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `order` int(11) NOT NULL,
  `parent_id` int(11) NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `authperm_l2menu_content_type_id_5c21dbc1_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `authperm_l2menu_parent_id_ade8d464_fk_authperm_l1menu_id`(`parent_id`) USING BTREE,
  CONSTRAINT `authperm_l2menu_content_type_id_5c21dbc1_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `authperm_l2menu_parent_id_ade8d464_fk_authperm_l1menu_id` FOREIGN KEY (`parent_id`) REFERENCES `authperm_l1menu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of authperm_l2menu
-- ----------------------------
INSERT INTO `authperm_l2menu` VALUES (3, '用户', 'user', '/authperm/user', 1, 2, NULL);
INSERT INTO `authperm_l2menu` VALUES (4, '组', 'group', '/authperm/group', 2, 2, NULL);
INSERT INTO `authperm_l2menu` VALUES (5, 'Gitlab 仓库', 'gitlabrepo', '/project/gitlabrepo', 10, 3, NULL);
INSERT INTO `authperm_l2menu` VALUES (6, 'Gainhon666', 'gainhon666', '/domain/gainhon666', 1, 4, NULL);
INSERT INTO `authperm_l2menu` VALUES (7, 'lingfannao', 'lingfannao', '/domain/lingfannao', 2, 4, NULL);
INSERT INTO `authperm_l2menu` VALUES (8, '定时任务', 'taskresult', '/project/task', 10, 5, NULL);
INSERT INTO `authperm_l2menu` VALUES (9, '主机', 'host', '/project/host', 1, 6, 9);
INSERT INTO `authperm_l2menu` VALUES (10, 'MySQL', 'mysql', '/project/mysql', 2, 6, 10);
INSERT INTO `authperm_l2menu` VALUES (11, '账号', 'index', '/account/index', 10, 7, 34);
INSERT INTO `authperm_l2menu` VALUES (12, '配置', 'config', '/project/config', 4, 8, 14);
INSERT INTO `authperm_l2menu` VALUES (13, '组对象权限', 'permission', '/authperm/groupobjperm', 3, 2, NULL);
INSERT INTO `authperm_l2menu` VALUES (14, '中间件', 'middleware', '/project/middleware', 3, 6, 35);
INSERT INTO `authperm_l2menu` VALUES (17, '项目', 'project', '/project/project', 1, 8, 11);
INSERT INTO `authperm_l2menu` VALUES (18, '模块', 'module', '/project/module', 2, 8, 13);
INSERT INTO `authperm_l2menu` VALUES (19, '地址', 'url', '/project/url', 3, 8, 12);
INSERT INTO `authperm_l2menu` VALUES (20, '一级菜单', 'l1menu', '/authperm/l1menu', 4, 2, NULL);
INSERT INTO `authperm_l2menu` VALUES (21, '二级菜单', 'l2menu', '/authperm/l2menu', 5, 2, 17);
INSERT INTO `authperm_l2menu` VALUES (22, 'Jenkins 任务', 'jenkinsjob', '/project/jenkinsjob', 5, 9, NULL);

SET FOREIGN_KEY_CHECKS = 1;
