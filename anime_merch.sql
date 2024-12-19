--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.0

-- Started on 2024-12-19 13:28:44

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 218 (class 1259 OID 16932)
-- Name: anime; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.anime (
    id_anime integer NOT NULL,
    a_name character varying(255) NOT NULL
);


ALTER TABLE public.anime OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16931)
-- Name: anime_id_anime_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.anime_id_anime_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.anime_id_anime_seq OWNER TO postgres;

--
-- TOC entry 4874 (class 0 OID 0)
-- Dependencies: 217
-- Name: anime_id_anime_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.anime_id_anime_seq OWNED BY public.anime.id_anime;


--
-- TOC entry 220 (class 1259 OID 16941)
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    id_product integer NOT NULL,
    p_name character varying(255) NOT NULL,
    p_anime integer NOT NULL,
    p_price real NOT NULL,
    p_count integer NOT NULL
);


ALTER TABLE public.product OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16940)
-- Name: product_id_product_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_id_product_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.product_id_product_seq OWNER TO postgres;

--
-- TOC entry 4875 (class 0 OID 0)
-- Dependencies: 219
-- Name: product_id_product_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_id_product_seq OWNED BY public.product.id_product;


--
-- TOC entry 222 (class 1259 OID 16953)
-- Name: sale; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sale (
    id_sale integer NOT NULL,
    s_product integer NOT NULL,
    s_count integer NOT NULL,
    s_price real NOT NULL,
    s_date date NOT NULL
);


ALTER TABLE public.sale OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16952)
-- Name: sale_id_sale_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sale_id_sale_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sale_id_sale_seq OWNER TO postgres;

--
-- TOC entry 4876 (class 0 OID 0)
-- Dependencies: 221
-- Name: sale_id_sale_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sale_id_sale_seq OWNED BY public.sale.id_sale;


--
-- TOC entry 4705 (class 2604 OID 16935)
-- Name: anime id_anime; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.anime ALTER COLUMN id_anime SET DEFAULT nextval('public.anime_id_anime_seq'::regclass);


--
-- TOC entry 4706 (class 2604 OID 16944)
-- Name: product id_product; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product ALTER COLUMN id_product SET DEFAULT nextval('public.product_id_product_seq'::regclass);


--
-- TOC entry 4707 (class 2604 OID 16956)
-- Name: sale id_sale; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sale ALTER COLUMN id_sale SET DEFAULT nextval('public.sale_id_sale_seq'::regclass);


--
-- TOC entry 4864 (class 0 OID 16932)
-- Dependencies: 218
-- Data for Name: anime; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.anime (id_anime, a_name) FROM stdin;
\.


--
-- TOC entry 4866 (class 0 OID 16941)
-- Dependencies: 220
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product (id_product, p_name, p_anime, p_price, p_count) FROM stdin;
\.


--
-- TOC entry 4868 (class 0 OID 16953)
-- Dependencies: 222
-- Data for Name: sale; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sale (id_sale, s_product, s_count, s_price, s_date) FROM stdin;
\.


--
-- TOC entry 4877 (class 0 OID 0)
-- Dependencies: 217
-- Name: anime_id_anime_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.anime_id_anime_seq', 1, false);


--
-- TOC entry 4878 (class 0 OID 0)
-- Dependencies: 219
-- Name: product_id_product_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_id_product_seq', 1, false);


--
-- TOC entry 4879 (class 0 OID 0)
-- Dependencies: 221
-- Name: sale_id_sale_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sale_id_sale_seq', 1, false);


--
-- TOC entry 4709 (class 2606 OID 16939)
-- Name: anime anime_a_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.anime
    ADD CONSTRAINT anime_a_name_key UNIQUE (a_name);


--
-- TOC entry 4711 (class 2606 OID 16937)
-- Name: anime anime_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.anime
    ADD CONSTRAINT anime_pkey PRIMARY KEY (id_anime);


--
-- TOC entry 4713 (class 2606 OID 16946)
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id_product);


--
-- TOC entry 4715 (class 2606 OID 16958)
-- Name: sale sale_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sale
    ADD CONSTRAINT sale_pkey PRIMARY KEY (id_sale);


--
-- TOC entry 4716 (class 2606 OID 16947)
-- Name: product product_p_anime_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_p_anime_fkey FOREIGN KEY (p_anime) REFERENCES public.anime(id_anime) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 4717 (class 2606 OID 16959)
-- Name: sale sale_s_product_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sale
    ADD CONSTRAINT sale_s_product_fkey FOREIGN KEY (s_product) REFERENCES public.product(id_product) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2024-12-19 13:28:45

--
-- PostgreSQL database dump complete
--

