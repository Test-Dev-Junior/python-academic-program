--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-06-05 10:23:58

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE bd_programa_academico;
--
-- TOC entry 3323 (class 1262 OID 16398)
-- Name: bd_programa_academico; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE bd_programa_academico WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Ecuador.1252';


ALTER DATABASE bd_programa_academico OWNER TO postgres;

\connect bd_programa_academico

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16415)
-- Name: tb_estudiante; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tb_estudiante (
    id integer NOT NULL,
    nombre character varying(25),
    apellido character varying(25),
    edad integer
);


ALTER TABLE public.tb_estudiante OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16414)
-- Name: tb_estudiante_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tb_estudiante_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tb_estudiante_id_seq OWNER TO postgres;

--
-- TOC entry 3324 (class 0 OID 0)
-- Dependencies: 214
-- Name: tb_estudiante_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tb_estudiante_id_seq OWNED BY public.tb_estudiante.id;


--
-- TOC entry 3173 (class 2604 OID 16418)
-- Name: tb_estudiante id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tb_estudiante ALTER COLUMN id SET DEFAULT nextval('public.tb_estudiante_id_seq'::regclass);


--
-- TOC entry 3317 (class 0 OID 16415)
-- Dependencies: 215
-- Data for Name: tb_estudiante; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tb_estudiante (id, nombre, apellido, edad) VALUES (2, 'Edison', 'Salinas', 23);
INSERT INTO public.tb_estudiante (id, nombre, apellido, edad) VALUES (4, 'Jacinto', 'Tapia', 45);
INSERT INTO public.tb_estudiante (id, nombre, apellido, edad) VALUES (3, 'Javier', 'Mendoza', 25);
INSERT INTO public.tb_estudiante (id, nombre, apellido, edad) VALUES (9, 'Arturo', 'Cruz', 22);


--
-- TOC entry 3325 (class 0 OID 0)
-- Dependencies: 214
-- Name: tb_estudiante_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tb_estudiante_id_seq', 10, true);


-- Completed on 2023-06-05 10:23:58

--
-- PostgreSQL database dump complete
--

