CREATE DATABASE assignment;
USE assignment;

CREATE TABLE `users`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `firstname` VARCHAR(255) NOT NULL,
    `lastname` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL
);



CREATE TABLE `auction_items`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `start_time` TIMESTAMP NOT NULL,
    `end_time` TIMESTAMP NOT NULL
);
CREATE TABLE `images`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `url` VARCHAR(255) NOT NULL,
    `auction_item` INT UNSIGNED NOT NULL
);
CREATE TABLE `bids`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `auction_item` INT UNSIGNED NOT NULL,
    `price` DOUBLE(8, 2) NOT NULL,
    `time` DATETIME NOT NULL,
    `user` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `bids` ADD CONSTRAINT `bids_user_foreign` FOREIGN KEY(`user`) REFERENCES `users`(`id`);
ALTER TABLE
    `bids` ADD CONSTRAINT `bids_auction_item_foreign` FOREIGN KEY(`auction_item`) REFERENCES `auction_items`(`id`);
ALTER TABLE
    `images` ADD CONSTRAINT `images_auction_item_foreign` FOREIGN KEY(`auction_item`) REFERENCES `auction_items`(`id`);
    

insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (1, "alice",	"persson", "alice@mymail.com", "alice1");
insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (2, "bob", "svensson","bob@mymail.com","bob2");
insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (3, "caroline", "petterson", "caroline@mymail.com", "caroline3");
insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (4, "daniel", "ericsson", "daniel@mymail.com", "daniel4");
insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (5, "eric", "johnsson", "eric@mymail.com", "eric5");
insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (6, "fredrik", "carlsson", "fredrik@mymail.com", "fredrik6");
insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (7, "george", "bertilsson", "george@mymail.com", "george7");
insert into `users` (`id`,  `firstname`, `lastname`,`email`, `password`) values (8, "henrik", "nilsson",	"henrik@mymail.com", "henrik8");

insert into `auction_items` (`id`, `name`, `description`, `start_time`, `end_time`) values (1, "BMW", "5års nybilsgaranti eller 10 000mil., Aktiv filhållningsassistans, Apple CarPlay & Android Auto", "2021-01-23 00:00:00", "2021-12-28 00:00:00" );
insert into `auction_items` (`id`, `name`, `description`, `start_time`, `end_time`) values (2, "iphone", "model year 2011, 64GB, änvandad men bra skick", "2021-12-20 00:00:00", "2022-12-24 00:00:00");
insert into `auction_items` (`id`, `name`, `description`, `start_time`, `end_time`) values (3, "samsung s21", "model year 2021, 128GB", "2022-01-16 00:00:00", "2022-05-25 00:00:00" );
insert into `auction_items` (`id`, `name`, `description`, `start_time`, `end_time`) values (4, "lenovo laptop", "yoga slim pro 7, immersive entertainment,16:10display", "2020-06-16 00:00:00", "2021-08-29 00:00:00");
insert into `auction_items` (`id`, `name`, `description`, `start_time`, `end_time`) values (5, "Honda","white color car with latest technologies", "2021-07-17 00:00:00", "2022-09-18 00:00:00");

insert into `images` (`id`, `url`, `auction_item`) values (1, "https://www.carwale.com/used/bmw-cars-in-hyderabad/#car=1&city=105&pc=105&sc=-1&so=-1&pn=1", 1);
insert into `images` (`id`, `url`, `auction_item`) values (2, "https://www.olx.in/en-in/mobile-phones_c1453/q-samsung-21", 3);
insert into `images` (`id`, `url`, `auction_item`) values (3, "https://www.cardekho.com/used-honda+cars+in+hyderabad" , 5);
insert into `images` (`id`, `url`, `auction_item`) values (4, "https://couponorg.com/store/lenovo-india/?gclid=Cj0KCQiA-oqdBhDfARIsAO0TrGHWWDtoKnj7bDUxsTX3FhPuoCFeex6aob09JHjosba-MbieckC9q_caAkc2EALw_wcB" , 4);  
insert into `images` (`id`, `url`, `auction_item`) values (5, "https://www.quikr.com/mobiles-tablets/Apple+Mobile-Phones+Hyderabad+w737fd", 2);  

insert into `bids` (`id`, `auction_item`, `price`, `time`, `user`) values (1, 2, 12345,"2021-12-11 00:00:00", 1);
insert into `bids` (`id`, `auction_item`, `price`, `time`, `user`) values (2, 1, 7000,"2021-12-21 00:00:00", 8);
insert into `bids` (`id`, `auction_item`, `price`, `time`, `user`) values (3, 4, 200000,"2020-11-11 00:00:00", 2);
insert into `bids` (`id`, `auction_item`, `price`, `time`, `user`) values (4, 5, 16000,"2021-07-22 00:00:00", 5);
insert into `bids` (`id`, `auction_item`, `price`, `time`, `user`) values (5, 3, 7040,"2022-03-03 00:00:00", 7);

