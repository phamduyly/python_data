-- create procedure
CREATE PROCEDURE myproc()
BEGIN
    DECLARE i int DEFAULT 237692001;
    WHILE i <= 237692004 DO
        INSERT INTO mytable (code, active, total) VALUES (i, 1, 1);
        SET i = i + 1;
    END WHILE;
END

-- INDEXING 




-- Fragment testing source : https://serverfault.com/questions/202000/how-find-and-fix-fragmented-mysql-tables


-- Index Fragement
select ENGINE,
  concat(TABLE_SCHEMA, '.', TABLE_NAME) as table_name,
  round(DATA_LENGTH/1024/1024, 2) as data_length,
  round(INDEX_LENGTH/1024/1024, 2) as index_length,
  round(DATA_FREE/1024/1024, 2) as data_free,
  (data_free/(index_length+data_length)) as frag_ratio
FROM information_schema.tables
WHERE DATA_FREE > 0
ORDER BY frag_ratio DESC;


-- log rotation source: https://www.question-defense.com/2009/12/20/configure-logrotate-to-rotate-and-flush-mysql-logs-without-a-password

