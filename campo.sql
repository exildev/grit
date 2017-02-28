--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.4
-- Dumped by pg_dump version 9.5.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: formulario_campo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE formulario_campo (
    id integer NOT NULL,
    nombre character varying(45) NOT NULL,
    tipo_id integer NOT NULL,
    grupo_id integer NOT NULL,
    ver_como character varying(45) NOT NULL
);


ALTER TABLE formulario_campo OWNER TO postgres;

--
-- Name: formulario_campo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE formulario_campo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE formulario_campo_id_seq OWNER TO postgres;

--
-- Name: formulario_campo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE formulario_campo_id_seq OWNED BY formulario_campo.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY formulario_campo ALTER COLUMN id SET DEFAULT nextval('formulario_campo_id_seq'::regclass);


--
-- Data for Name: formulario_campo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY formulario_campo (id, nombre, tipo_id, grupo_id, ver_como) FROM stdin;
4	NOMBRE DEL INDICADOR	1	1	block
5	PROCESO	1	1	block
6	OBJETIVO	1	1	block
7	RESPONSABLE	1	1	block
8	FORMULA DE CALCULO	1	1	block
9	DESCRIPCION DEL INDICADOR	1	1	block
14	FUENTE DE INFORMACION	1	1	block
15	SOBRESALIENTE	2	3	inline
16	BUENO	2	3	inline
17	ACEPTABLE	2	3	inline
18	DEFICIENTE	2	3	inline
10	FRECUENCIA	1	1	inline
11	META	1	1	inline
12	UNIDAD DE MEDIDA	1	1	inline
13	TIPO DE INDICADOR	1	1	inline
\.


--
-- Name: formulario_campo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('formulario_campo_id_seq', 18, true);


--
-- Name: formulario_campo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY formulario_campo
    ADD CONSTRAINT formulario_campo_pkey PRIMARY KEY (id);


--
-- Name: formulario_campo_acaeb2d6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX formulario_campo_acaeb2d6 ON formulario_campo USING btree (grupo_id);


--
-- Name: formulario_campo_d3c0c18a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX formulario_campo_d3c0c18a ON formulario_campo USING btree (tipo_id);


--
-- Name: formulario_campo_grupo_id_a0974800_fk_formulario_grupo_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY formulario_campo
    ADD CONSTRAINT formulario_campo_grupo_id_a0974800_fk_formulario_grupo_id FOREIGN KEY (grupo_id) REFERENCES formulario_grupo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: formulario_campo_tipo_id_7053693d_fk_formulario_tipo_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY formulario_campo
    ADD CONSTRAINT formulario_campo_tipo_id_7053693d_fk_formulario_tipo_id FOREIGN KEY (tipo_id) REFERENCES formulario_tipo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

