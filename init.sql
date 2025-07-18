-- Создание таблицы stations
CREATE TABLE IF NOT EXISTS stations (
    station_id INT PRIMARY KEY,
    station_name VARCHAR(100)
);

-- Создание таблицы elements
CREATE TABLE IF NOT EXISTS elements (
    element_id INT PRIMARY KEY,
    station_id INT REFERENCES stations(station_id),
    element_name VARCHAR(100),
    certificate_number VARCHAR(50),
    manufacturer_name VARCHAR(100),
    passport_number BIGINT,
    factory_number INT,
    date_last_metrological_control TIMESTAMP,
    check_interval INT,
    range_measurements VARCHAR(100),
    date_last_check DATE,
    block_key_status BOOL,
    working_status BOOL,
    checking_date_start TIMESTAMP,
    checking_date_finish TIMESTAMP
);

-- Создание таблицы documents
CREATE TABLE IF NOT EXISTS documents (
    document_id INT PRIMARY KEY,
    element_id INT REFERENCES elements(element_id),
    document_name VARCHAR(200)
);


COPY stations FROM '/import_data/stations.csv' DELIMITER ',' CSV HEADER ENCODING 'WIN1251';
COPY elements FROM '/import_data/elements.csv' DELIMITER ',' CSV HEADER ENCODING 'WIN1251';
COPY documents FROM '/import_data/documents.csv' DELIMITER ',' CSV HEADER ENCODING 'WIN1251';