DROP TABLE if exists cartao cascade;
DROP TABLE if exists TRANSACAO cascade;
DROP TABLE if exists empregado cascade;
DROP TABLE if exists PRODUTO_NA_EMENTA cascade; 
DROP TABLE if exists CONSUMO_PODE_TER_PRODUTO cascade;
DROP TABLE if exists consumo cascade; 
DROP TABLE if exists PRODUTO cascade; 
DROP TABLE if exists lugar cascade; 
DROP TABLE if exists cliente cascade; 
DROP TABLE if exists ementa cascade; 
DROP TABLE if exists administrador cascade; 
DROP TABLE if exists restaurante cascade; 
DROP TABLE if exists localizacao cascade; 



/*==============================================================*/
/* Table: LOCALIZACAO                                           */
/*==============================================================*/
create table LOCALIZACAO (
   ID_LOCALIZACAO       INT4                 not null,
   TIPO_LOCALIZACAO     INT4                 not null,
   NOME_LOCALIZACAO     TEXT                 not null,
   constraint PK_LOCALIZACAO primary key (ID_LOCALIZACAO)
);

/*==============================================================*/
/* Table: RESTAURANTE                                           */
/*==============================================================*/
create table RESTAURANTE (
   ID_RESTAURANTE       INT4                 not null,
   ID_LOCALIZACAO       INT4                 not null,
   NOME_RESTAURANTE     TEXT                 not null,
   constraint PK_RESTAURANTE primary key (ID_RESTAURANTE),
   constraint FK_RESTAURA_RESTAURAN_LOCALIZA foreign key (ID_LOCALIZACAO)
      references LOCALIZACAO (ID_LOCALIZACAO)
      on delete cascade on update cascade
);

/*==============================================================*/
/* Table: ADMINISTRADOR                                         */
/*==============================================================*/
create table ADMINISTRADOR (
   ID_ADMINISTRADOR     SERIAL                 not null,
   ID_RESTAURANTE       INT4                 not null,
   USERNAME_ADMINISTRADOR TEXT               not null,
   EMAIL_ADMINISTRADOR  TEXT                 not null,
   PASSWORD_ADMINISTRADOR TEXT                 not null,
   constraint PK_ADMINISTRADOR primary key (ID_ADMINISTRADOR),
   constraint FK_ADMINIST_RESTAURAN_RESTAURA foreign key (ID_RESTAURANTE)
      references RESTAURANTE (ID_RESTAURANTE)
      on delete cascade on update cascade
);


/*==============================================================*/
/* Table: EMENTA                                                */
/*==============================================================*/
create table EMENTA (
   ID_EMENTA            SERIAL                 not null,
   DIA_DA_SEMANA        INT4                 not null,
   ID_RESTAURANTE       INT4                 not null,
   constraint PK_EMENTA primary key (ID_EMENTA),
   constraint FK_EMENTA_EMENTAS_D_RESTAURA foreign key (ID_RESTAURANTE)
      references RESTAURANTE (ID_RESTAURANTE)
      on delete cascade on update cascade
);

/*==============================================================*/
/* Table: CLIENTE                                               */
/*==============================================================*/
create table CLIENTE (
   ID_CLIENTE           SERIAL                 not null,
   NOME_CLIENTE         TEXT                 not null,
   DATA_REGISTO_CLIENTE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   constraint PK_CLIENTE primary key (ID_CLIENTE)
);

/*==============================================================*/
/* Table: LUGAR                                                 */
/*==============================================================*/
create table LUGAR (
   ID_LUGAR             SERIAL                 not null,
   TIPO_LUGAR           INT4                 not null,
   constraint PK_LUGAR primary key (ID_LUGAR)
);

/*==============================================================*/
/* Table: PRODUTO                                               */
/*==============================================================*/
create table PRODUTO (
   ID_PRODUTO           SERIAL                not null,
   TIPO_PRODUTO         INT4                  not null,
   NOME_PRODUTO         TEXT                 not null,
   DESIGNACAO_PRODUTO    TEXT                 null,
   PRECO_PRODUTO        MONEY                not null,
   ALERGIA_PRODUTO       TEXT                 null,
   QUANTIDADE_PRODUTO    INT4                 null,
   constraint PK_PRODUTO primary key (ID_PRODUTO)
);

/*==============================================================*/
/* Table: CARTAO                                                */
/*==============================================================*/
create table CARTAO (
   ID_CARTAO            SERIAL                not null,
   ID_RESTAURANTE       INT4                  not null,
   ID_CLIENTE           INT4                  not null,
   DATA_CRIACAO_CARTAO       TIMESTAMP        DEFAULT CURRENT_TIMESTAMP,
   constraint PK_CARTAO primary key (ID_CARTAO),
   constraint FK_CARTAO_RESTAURANTE foreign key (ID_RESTAURANTE)
      references RESTAURANTE (ID_RESTAURANTE)
      on delete cascade on update cascade,
   constraint FK_CARTAO_CLIENTE foreign key (ID_CLIENTE)
      references CLIENTE (ID_CLIENTE)
      on delete cascade on update cascade
);

/*==============================================================*/
/* Table: CONSUMO                                               */
/*==============================================================*/
create table CONSUMO (
   ID_CONSUMO           SERIAL               not null,
   ID_CARTAO            INT4                 not null,
   ID_LUGAR             INT4                 not null,
   constraint PK_CONSUMO primary key (ID_CONSUMO),
   constraint FK_CONSUMO_LUGAR_DO_LUGAR foreign key (ID_LUGAR)
      references LUGAR (ID_LUGAR)
      on delete cascade on update cascade,
      constraint FK_CONSUMO_CARTAO foreign key (ID_CARTAO)
      references CARTAO (ID_CARTAO)
      on delete cascade on update cascade
      
);


/*==============================================================*/
/* Table: CONSUMO_PODE_TER_PRODUTO                              */
/*==============================================================*/
create table CONSUMO_PODE_TER_PRODUTO (
   ID_CONSUMO           INT4                 not null,
   ID_PRODUTO           INT4                    not null,
   constraint PK_CONSUMO_PODE_TER_PRODUTO primary key (ID_CONSUMO, ID_PRODUTO),
   constraint FK_CONSUMO__CONSUMO_P_CONSUMO foreign key (ID_CONSUMO)
      references CONSUMO (ID_CONSUMO)
      on delete cascade on update cascade,
   constraint FK_CONSUMO__CONSUMO_P_PRODUTO foreign key (ID_PRODUTO)
      references PRODUTO (ID_PRODUTO)
      on delete cascade on update cascade
);

/*==============================================================*/
/* Table: EMPREGADO                                             */
/*==============================================================*/
create table EMPREGADO (
   ID_EMPREGADO         SERIAL               not null,
   ID_RESTAURANTE       INT4                 not null,
   NOME_EMPREGADO       TEXT                 not null,
   constraint PK_EMPREGADO primary key (ID_EMPREGADO),
   constraint FK_EMPREGAD_RESTAURAN_RESTAURA foreign key (ID_RESTAURANTE)
      references RESTAURANTE (ID_RESTAURANTE)
      on delete cascade on update cascade
);

/*==============================================================*/
/* Table: PRODUTO_NA_EMENTA                                     */
/*==============================================================*/
create table PRODUTO_NA_EMENTA (
   ID_EMENTA            INT4                 not null,
   ID_PRODUTO           INT4                 not null,
   constraint PK_PRODUTO_NA_EMENTA primary key (ID_EMENTA, ID_PRODUTO),
   constraint FK_PRODUTO_NA_EMENTA_EMENTA foreign key (ID_EMENTA)
      references EMENTA (ID_EMENTA)
      on delete cascade on update cascade,
   constraint FK_PRODUTO_NA_EMENTA_DE foreign key (ID_PRODUTO)
      references PRODUTO (ID_PRODUTO)
      on delete cascade on update cascade
);

/*==============================================================*/
/* Table: TRANSACAO                                             */
/*==============================================================*/
create table TRANSACAO (
   ID_RESTAURANTE       INT4                 not null,
   ID_CONSUMO           INT4                 not null,
   ID_TRANSACAO         SERIAL                not null,
   VALOR_TRANSACAO      INT4                 not null,
   DATA_TRANSACAO       TIMESTAMP            DEFAULT CURRENT_TIMESTAMP,
   constraint FK_TRANSACA_RESTAURAN_RESTAURA foreign key (ID_RESTAURANTE)
      references RESTAURANTE (ID_RESTAURANTE)
      on delete cascade on update cascade,
   constraint FK_TRANSACA_TRANSACAO_CONSUMO foreign key (ID_CONSUMO)
      references CONSUMO (ID_CONSUMO)
      on delete cascade on update cascade
);


