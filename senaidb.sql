create table todolist(
"_lineNumber" serial primary key,
item varchar(250),
status varchar(100)
);

insert into todolist(item, status) values('Comprar Pão', 'Iniciado');

select * from todolist;

-- comando bash
-- curl -X POST http://127.0.0.1:5000/item -H "Content-Type: application/json" -d '{"item":"Comprar", "status":"Em Fila"}'

