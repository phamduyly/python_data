-- Create table

https://stackoverflow.com/questions/6601978/completely-copying-a-postgres-table-with-sql

-- copying an old table to a new one
select * into newtable from oldtable

-- copy index

select indexdef from pg_indexes where tablename='oldtable';

--  Coy ifor.
SELECT c.oid,
  n.nspname,
  c.relname
FROM pg_catalog.pg_class c
     LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
WHERE c.relname ~ '^(oldtable)$'
  AND pg_catalog.pg_table_is_visible(c.oid)
ORDER BY 2, 3;

SELECT a.attname,
  pg_catalog.format_type(a.atttypid, a.atttypmod),
  (SELECT substring(pg_catalog.pg_get_expr(d.adbin, d.adrelid) for 128)
   FROM pg_catalog.pg_attrdef d
   WHERE d.adrelid = a.attrelid AND d.adnum = a.attnum AND a.atthasdef),
  a.attnotnull, a.attnum
FROM pg_catalog.pg_attribute a
WHERE a.attrelid = '74359' AND a.attnum > 0 AND NOT a.attisdropped
ORDER BY a.attnum;

-- ELSE - Indexing and statistic pg

-- create Binary index on the column 'titles' on table films
CREATE UNIQUE INDEX title_idx ON films (title);

-- https://www.postgresql.org/docs/9.1/sql-createindex.html
