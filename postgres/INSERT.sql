
DROP SEQUENCE serial_localizacao;
DROP SEQUENCE serial_restaurante;
CREATE SEQUENCE serial_localizacao START 1 MINVALUE 1 NO MAXVALUE INCREMENT BY 1;
CREATE SEQUENCE serial_restaurante START 1 MINVALUE 1 NO MAXVALUE INCREMENT BY 1;


/*==============================================================*/
/* Table: LOCALIZACAO                                           */
/*==============================================================*/

insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),0, 'Viseu');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),0, 'Lisboa');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),1, 'Barbeita');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),2, 'Castro Daire');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),2, 'Vila Nova Paiva');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),2, 'Satão');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),0, 'Porto');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),1, 'Sao Martinho');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),1, 'Santos Evos');
insert into localizacao (id_localizacao, tipo_localizacao, nome_localizacao) values ( nextval('serial_localizacao'),2, 'Mundao');

 select * from localizacao;

/*==============================================================*/
/* Table: RESTAURANTE                                           */
/*==============================================================*/

insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),1, 'Restaurante Quinta dos Barreiros');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),2,'MRV Communications, Inc.');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),3,'Amec Plc Ord');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),1,'Farmers Capital Bank Corporation');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),2,'First Trust China AlphaDEX Fund');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),6,'L Brands, Inc.');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),3,'DISH Network Corporation');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),4,'NASDAQ TEST STOCK');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),6,'Martin Marietta Materials, Inc.');
insert into Restaurante (id_restaurante, id_localizacao, nome_restaurante) values ( nextval('serial_restaurante'),7,'State Street Corporation');


Select * from restaurante;

/*==============================================================*/
/* Table: ADMINISTRADOR                                         */
/*==============================================================*/

insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (1, 'teste', 'teste@teste.com', '12345');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (2, 'teste1', 'aarnison1@ustream.tv', 'RxFFCqnv');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (3, 'teste2', 'vellaway2@google.com.au', 'qQCoP97');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (4, 'teste3', 'jbellfield3@squarespace.com', 'N2it9uqoO');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (5, 'teste4', 'jriolfo4@yahoo.com', 'kOhw1Ga');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (6, 'teste5', 'zrenvoise5@netscape.com', '20NW0li');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (7, 'teste6', 'akornyakov6@geocities.jp', 'hDILmy7');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (8, 'teste7', 'jdisbrow7@woothemes.com', 'iSoDvTa');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (9, 'testinho', 'sgirton8@fc2.com', 'bKXAlG0JtQ');
insert into Administrador (id_restaurante, username_administrador, email_administrador, password_administrador) values (10, 'teste8', 'hisakovitch9@state.tx.us', 'T0jnPGK');


select * from administrador;

/*==============================================================*/
/* Table: EMENTA                                                */
/*==============================================================*/

insert into Ementa (dia_da_semana, id_restaurante) values ('0', 1);
insert into Ementa (dia_da_semana, id_restaurante) values ('1', 2);
insert into Ementa (dia_da_semana, id_restaurante) values ('2', 3);
insert into Ementa (dia_da_semana, id_restaurante) values ('3', 4);
insert into Ementa (dia_da_semana, id_restaurante) values ('4', 5);
insert into Ementa (dia_da_semana, id_restaurante) values ('5', 6);
insert into Ementa (dia_da_semana, id_restaurante) values ('6', 7);

select * from ementa;

/*==============================================================*/
/* Table: CLIENTE                                               */
/*==============================================================*/

insert into Cliente (nome_cliente, data_registo_cliente) values ('Gwen Bound', '1/16/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Marty Kubiczek', '1/26/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Edie Oldrey', '7/28/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Goldarina Di Frisco', '9/1/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Towney Winchester', '8/5/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Karly Canby', '8/14/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Issie Seabright', '7/21/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Gifford D''Aeth', '9/29/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Raychel Melbert', '4/7/2019');
insert into Cliente (nome_cliente, data_registo_cliente) values ('Sallie Surfleet', '2/1/2019');

select * from cliente;

/*==============================================================*/
/* Table: LUGAR                                                 */
/*==============================================================*/

insert into Lugar (tipo_lugar) values (2);
insert into Lugar (tipo_lugar) values (8);
insert into Lugar (tipo_lugar) values (6);
insert into Lugar (tipo_lugar) values (4);
insert into Lugar (tipo_lugar) values (4);
insert into Lugar (tipo_lugar) values (6);
insert into Lugar (tipo_lugar) values (2);
insert into Lugar (tipo_lugar) values (2);
insert into Lugar (tipo_lugar) values (4);
insert into Lugar (tipo_lugar) values (10);

select * from lugar;

/*==============================================================*/
/* Table: PRODUTO                                               */
/*==============================================================*/

insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (2, 'Pudim', 'Byrom', 2, 'Mitella trifida Graham var', 1);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (3, 'Francesinha','Damita', 3, 'Helianthus nuttallii Torr', 2);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (4, 'Dourada', 'Jacquette', 4, 'Erigeron pulchellus Michx.', 3);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (0, 'Pão', 'David', 5, 'Ericameria parishii', 4);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (2, 'Gelatina', 'Rourke', 6, 'Lippia L.', 5);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (3, 'Bife da Casa', 'Micky', 6, 'Sanguisorba menziesii Rydb.', 6);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (4, 'Bacalhau a Gomes de Sá', 'Nike', 6, 'Convallaria L.', 7);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (3,'Bitoque', 'Byram', 2, 'Panax L.', 8);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (4, 'Camarão', 'Kip', 4, 'Arthonia quintaria Nyl.', 9);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (4, 'Sardinhas', 'Osbourne', 4, 'Cojoba graciliflora', 10);
insert into Produto (tipo_produto, nome_produto, designacao_produto, preco_produto, alergia_produto, quantidade_produto) values (1, 'Coca Cola', 'newfsad', 12, 'Fwqdoba grafewfa', 8);

select * from produto;

/*==============================================================*/
/* Table: CARTAO                                                */
/*==============================================================*/

insert into Cartao (id_restaurante, id_cliente, DATA_CRIACAO_CARTAO) values (1, 1, '12/28/2019');
insert into Cartao (id_restaurante, id_cliente, DATA_CRIACAO_CARTAO) values (2, 2, '1/03/2019');
insert into Cartao (id_restaurante, id_cliente, DATA_CRIACAO_CARTAO) values (3, 3, '2/14/2019');
insert into Cartao (id_restaurante, id_cliente, DATA_CRIACAO_CARTAO) values (4, 4, '7/30/2019');
insert into Cartao (id_restaurante, id_cliente, DATA_CRIACAO_CARTAO) values (5, 5, '4/16/2019');
insert into Cartao (id_restaurante, id_cliente, DATA_CRIACAO_CARTAO) values (6, 6, '4/23/2019');
insert into Cartao (id_restaurante, id_cliente, DATA_CRIACAO_CARTAO) values (7, 7, '5/04/2019');

select * from cartao;

/*==============================================================*/
/* Table: CONSUMO                                               */
/*==============================================================*/

insert into Consumo (ID_CARTAO, id_lugar) values (1,2);
insert into Consumo (ID_CARTAO, id_lugar) values (2,3);
insert into Consumo (ID_CARTAO, id_lugar) values (3,1);
insert into Consumo (ID_CARTAO, id_lugar) values (4,5);
insert into Consumo (ID_CARTAO, id_lugar) values (5,2);
insert into Consumo (ID_CARTAO, id_lugar) values (6,7);
insert into Consumo (ID_CARTAO, id_lugar) values (7,6);
insert into Consumo (ID_CARTAO, id_lugar) values (3,8);
insert into Consumo (ID_CARTAO, id_lugar) values (4,9);
insert into Consumo (ID_CARTAO, id_lugar) values (1,10);

select * from consumo;

/*==============================================================*/
/* Table: CONSUMO_PODE_TER_PRODUTO                              */
/*==============================================================*/

insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (1, 1);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (2, 2);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (3, 3);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (4, 4);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (5, 5);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (6, 6);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (7, 7);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (8, 8);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (9, 9);
insert into Consumo_pode_ter_produto (id_consumo, id_produto) values (10, 10);

select * from consumo_pode_ter_produto;

/*==============================================================*/
/* Table: EMPREGADO                                             */
/*==============================================================*/

insert into Empregado (id_restaurante, nome_empregado) values (1, 'Caspar');
insert into Empregado (id_restaurante, nome_empregado) values (2, 'Lisha');
insert into Empregado (id_restaurante, nome_empregado) values (3, 'Borg');
insert into Empregado (id_restaurante, nome_empregado) values (4, 'Phillis');
insert into Empregado (id_restaurante, nome_empregado) values (5, 'Vicki');
insert into Empregado (id_restaurante, nome_empregado) values (6, 'Say');
insert into Empregado (id_restaurante, nome_empregado) values (7, 'Shae');
insert into Empregado (id_restaurante, nome_empregado) values (8, 'Briney');
insert into Empregado (id_restaurante, nome_empregado) values (8, 'Barnebas');
insert into Empregado (id_restaurante, nome_empregado) values (9, 'Seumas');

select * from empregado;


/*==============================================================*/
/* Table: PRODUTO_NA_EMENTA                                     */
/*==============================================================*/

insert into Produto_na_ementa (id_ementa,  id_produto) values (1, 1);
insert into Produto_na_ementa (id_ementa,  id_produto) values (2, 2);
insert into Produto_na_ementa (id_ementa,  id_produto) values (3, 3);
insert into Produto_na_ementa (id_ementa,  id_produto) values (4, 4);
insert into Produto_na_ementa (id_ementa,  id_produto) values (5, 5);
insert into Produto_na_ementa (id_ementa,  id_produto) values (6, 6);
insert into Produto_na_ementa (id_ementa,  id_produto) values (7,7);

select * from produto_na_ementa;

/*==============================================================*/
/* Table: TRANSACAO                                             */
/*==============================================================*/

insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (1, 1, 1, '7/16/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (2, 2, 200, '2/6/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (3, 3, 29, '3/16/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (4, 4, 16, '12/6/2018');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (5, 5,34, '3/5/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (6, 6, 25, '4/8/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (7, 7, 80, '4/22/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (8, 8, 5, '1/16/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (9, 9, 15, '2/28/2019');
insert into Transacao (id_restaurante, id_consumo, valor_transacao, data_transacao) values (10, 10, 10, '4/25/2019');

select * from transacao;





