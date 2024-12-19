-- Kullanıcı oluşturma
INSERT INTO user_table (name)
VALUES ('Admin');


-- Intentler
INSERT INTO intent_table (name,description)
VALUES
('Hatırlatıcı', 'Kullanıcının aktiviteleri hatırlamasına yardımcı olur'),
('Seyehat', 'Kullanıcının seyahat planlarını yapmasına yardımcı olur');
-- Entityler
INSERT INTO entity_table (intent_id, entity_name)
VALUES
(1,'Market/Alışveriş'),
(1,'Okul/Ders'),
(1,'Spor'),
(1,'İş'),
(1,'Toplantı'),
(1, 'Uyku'),
(2,'Konak'),
(2,'Buca'),
(2,'Karşıyaka'),
(2,'Bornova'),
(2,'Okul'),
(2,'Ev');




-- Kontekst bilgisi
INSERT INTO context_table (user_id, previous_intent_id, previous_entity_id, context_data)
VALUES
(1, NULL, NULL, 'NULL');

-- Cevaplar

-- Hatırlatıcı
INSERT INTO response_pool (intent_id, entity_id, response, context_id, rating)
VALUES
(1,1,'Marketten alışveriş yapmayı unutma',NULL,5),
(1,2,'Okula gitmeyi unutma',NULL,5),
(1,3,'Spor yapmayı unutma',NULL,5),
(1,4,'İşe gitmeyi unutma',NULL,5),
(1,5,'Toplantıya gitmeyi unutma',1,5),
(1,6,'Uyumayı unutma',NULL,5),
(2,7,'Konaka gitmek için otobüs/izban/vapur/metro kullanabilirsin',1,5),
(2,8,'Bucaya gitmek için otobüs kullanabilirsin',NULL,5),
(2,9,'Karşıyakaya gitmek için otobüs/izban/tranvay/vapur kullanabilirsin',1,5),
(2,10,'Bornovaya gitmek için otobüs/metro kullanabilirsin',NULL,5),
(2,11,'Okula gitmek için otobüs kullanabilirsin',NULL,5),
(2,12,'Eve gitmek için otobüs kullanabilirsin',NULL,5);