#Create table
create table foo (id int, padding text);

insert into foo (id, padding) select id, md5(random()::text) 
from generate_series(1, 1000000) as id 
order by random();

create index foo_id_ix on foo (id);

ANALYZE


# CTE - common table expression

