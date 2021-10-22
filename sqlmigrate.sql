--
-- Change Meta options on middleware
--
--
-- Add field alias to url
--
ALTER TABLE `project_url` ADD COLUMN `alias` varchar(200) NULL;
--
-- Add field deploy_dir to url
--
ALTER TABLE `project_url` ADD COLUMN `deploy_dir` varchar(200) NULL;
--
-- Add field hosts to url
--
CREATE TABLE `project_url_hosts` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `url_id` integer NOT NULL, `host_id` integer NOT NULL);
ALTER TABLE `project_url_hosts` ADD CONSTRAINT `project_url_hosts_url_id_host_id_7ccbdf4d_uniq` UNIQUE (`url_id`, `host_id`);
ALTER TABLE `project_url_hosts` ADD CONSTRAINT `project_url_hosts_url_id_3467774b_fk_project_url_id` FOREIGN KEY (`url_id`) REFERENCES `project_url` (`id`);
ALTER TABLE `project_url_hosts` ADD CONSTRAINT `project_url_hosts_host_id_df11cbfb_fk_project_host_id` FOREIGN KEY (`host_id`) REFERENCES `project_host` (`id`);

--
-- Add field public_ip to url
--
ALTER TABLE `project_url` ADD COLUMN `public_ip` char(39) NULL;


-- 20211022
-- Add field project to mysql
--
CREATE TABLE `project_mysql_project` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `mysql_id` integer NOT NULL, `project_id` integer NOT NULL);
ALTER TABLE `project_mysql_project` ADD CONSTRAINT `project_mysql_project_mysql_id_project_id_54c46a1f_uniq` UNIQUE (`mysql_id`, `project_id`);
ALTER TABLE `project_mysql_project` ADD CONSTRAINT `project_mysql_project_mysql_id_4f70643b_fk_project_mysql_id` FOREIGN KEY (`mysql_id`) REFERENCES `project_mysql` (`id`);
ALTER TABLE `project_mysql_project` ADD CONSTRAINT `project_mysql_project_project_id_e09143f8_fk_project_project_id` FOREIGN KEY (`project_id`) REFERENCES `project_project` (`id`);
