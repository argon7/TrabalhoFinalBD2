# TrabalhoFinalBD2
<h3>Trello</h3>
https://trello.com/b/vonwvqNa
<h3>Documentos/Relatório</h3>
https://estgv-my.sharepoint.com/:f:/r/personal/estgv17192_alunos_estgv_ipv_pt/Documents/BD2%20Projeto?csf=1&e=8Pydom
<br>
user: admin@admin.com --- vai dar erro com o sqlalchemy<br>
pass : admin --- vai dar erro com o sqlalchemy<br>
<br>
user: admin1@admin1.com<br>
pass : admin1<br>
<br>
<h2>Conta Mail / ElephantSQL</h2>
Gmail: basedados2ipv<br>
pass: vodkashot<br>
<br>
<br>                                 user="fphawxtr",
<br>                                 password="wjLOHRDOaplszZ6zyg1GyoGstd2hUWUf",
<br>                                 host="rogue.db.elephantsql.com",
<br>                                 port="5432",
<br>                                 database="fphawxtr"




API Example fucntion blah blah
````
CREATE OR REPLACE FUNCTION createAdministrador(username_admin text,email_admin text, password_admin text, nome_Restaurante text) returns boolean AS $$
DECLARE IDRestaurante_variable int;
DECLARE ExistsEmail int;
DECLARE ExistsUsername int;
BEGIN
SELECT COUNT (*) from Administrador where email_administrador= email_admin into ExistsEmail;
IF(ExistsEmail > 0) THEN
   RETURN FALSE;
END IF;
SELECT COUNT (*) from Administrador where username_administrador= username_admin into ExistsUsername;
IF(ExistsUsername > 0) THEN
   RETURN FALSE;
END IF;
select getIdRestaurante(nome_Restaurante) into IDRestaurante_variable;
IF(IDRestaurante_variable = 0) THEN
	RETURN FALSE;
END IF;
insert into Administrador(id_restaurante,username_administrador, email_administrador, password_administrador)
   values ( IDRestaurante_variable,username_admin, email_admin, password_admin);
RETURN TRUE;
END;
$$ LANGUAGE plpgsql;
````

API Example fucntion blah blahAPI Example fucntion blah blah

````
CREATE OR REPLACE FUNCTION createAdministrador(username_admin text,email_admin text, password_admin text, nome_Restaurante text) returns boolean AS $$
DECLARE IDRestaurante_variable int;
DECLARE ExistsEmail int;
DECLARE ExistsUsername int;
BEGIN
SELECT COUNT (*) from Administrador where email_administrador= email_admin into ExistsEmail;
IF(ExistsEmail > 0) THEN
   RETURN FALSE;
END IF;
SELECT COUNT (*) from Administrador where username_administrador= username_admin into ExistsUsername;
IF(ExistsUsername > 0) THEN
   RETURN FALSE;
END IF;
select getIdRestaurante(nome_Restaurante) into IDRestaurante_variable;
IF(IDRestaurante_variable = 0) THEN
	RETURN FALSE;
END IF;
insert into Administrador(id_restaurante,username_administrador, email_administrador, password_administrador)
   values ( IDRestaurante_variable,username_admin, email_admin, password_admin);
RETURN TRUE;
END;
$$ LANGUAGE plpgsql;
````


