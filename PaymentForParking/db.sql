--
-- PostgreSQL database dump
--

-- Dumped from database version 11.10 (Debian 11.10-0+deb10u1)
-- Dumped by pg_dump version 11.10 (Debian 11.10-0+deb10u1)

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

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO paymentforparkinguser;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO paymentforparkinguser;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO paymentforparkinguser;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO paymentforparkinguser;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO paymentforparkinguser;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO paymentforparkinguser;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO paymentforparkinguser;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO paymentforparkinguser;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO paymentforparkinguser;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO paymentforparkinguser;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO paymentforparkinguser;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO paymentforparkinguser;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO paymentforparkinguser;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO paymentforparkinguser;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO paymentforparkinguser;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO paymentforparkinguser;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO paymentforparkinguser;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO paymentforparkinguser;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO paymentforparkinguser;

--
-- Name: index_paidparking; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_paidparking (
    id integer NOT NULL,
    carnumber character varying(150) NOT NULL,
    amountoftime integer NOT NULL,
    price double precision NOT NULL,
    telephone character varying(20) NOT NULL,
    adress_id integer,
    datetimepaidparking timestamp with time zone NOT NULL,
    email character varying(254),
    expirationdate date,
    enddateandtime timestamp with time zone,
    expirationtime time without time zone
);


ALTER TABLE public.index_paidparking OWNER TO paymentforparkinguser;

--
-- Name: index_paidparking_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_paidparking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_paidparking_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_paidparking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_paidparking_id_seq OWNED BY public.index_paidparking.id;


--
-- Name: index_paidseasontickets; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_paidseasontickets (
    id integer NOT NULL,
    carnumber character varying(150) NOT NULL,
    price double precision NOT NULL,
    telephone character varying(20) NOT NULL,
    nametickets_id integer,
    datetimepaidtickets timestamp with time zone NOT NULL,
    email character varying(254),
    expirationdate date,
    enddateandtime timestamp with time zone,
    expirationtime time without time zone
);


ALTER TABLE public.index_paidseasontickets OWNER TO paymentforparkinguser;

--
-- Name: index_paidseasontickets_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_paidseasontickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_paidseasontickets_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_paidseasontickets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_paidseasontickets_id_seq OWNED BY public.index_paidseasontickets.id;


--
-- Name: index_paidtickets; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_paidtickets (
    id integer NOT NULL,
    carnumber character varying(150) NOT NULL,
    numberofdays character varying(150) NOT NULL,
    "time" integer NOT NULL,
    price double precision NOT NULL,
    telephone character varying(20) NOT NULL,
    email character varying(150) NOT NULL,
    name_id integer
);


ALTER TABLE public.index_paidtickets OWNER TO paymentforparkinguser;

--
-- Name: index_paidtickets_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_paidtickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_paidtickets_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_paidtickets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_paidtickets_id_seq OWNED BY public.index_paidtickets.id;


--
-- Name: index_parking; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_parking (
    id integer NOT NULL,
    adress character varying(150) NOT NULL,
    workinghours character varying(50) NOT NULL,
    minimaltimeforpayment character varying(50) NOT NULL,
    price integer NOT NULL,
    numberofavailableseats integer NOT NULL
);


ALTER TABLE public.index_parking OWNER TO paymentforparkinguser;

--
-- Name: index_parking_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_parking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_parking_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_parking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_parking_id_seq OWNED BY public.index_parking.id;


--
-- Name: index_parking_seasontickets; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_parking_seasontickets (
    id integer NOT NULL,
    parking_id integer NOT NULL,
    seasontickets_id integer NOT NULL
);


ALTER TABLE public.index_parking_seasontickets OWNER TO paymentforparkinguser;

--
-- Name: index_parking_seasontickets_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_parking_seasontickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_parking_seasontickets_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_parking_seasontickets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_parking_seasontickets_id_seq OWNED BY public.index_parking_seasontickets.id;


--
-- Name: index_parking_tickets; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_parking_tickets (
    id integer NOT NULL,
    parking_id integer NOT NULL,
    tickets_id integer NOT NULL
);


ALTER TABLE public.index_parking_tickets OWNER TO paymentforparkinguser;

--
-- Name: index_parking_tickets_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_parking_tickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_parking_tickets_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_parking_tickets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_parking_tickets_id_seq OWNED BY public.index_parking_tickets.id;


--
-- Name: index_seasontickets; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_seasontickets (
    id integer NOT NULL,
    numberofdays character varying(50) NOT NULL,
    "time" character varying(50) NOT NULL,
    price double precision NOT NULL
);


ALTER TABLE public.index_seasontickets OWNER TO paymentforparkinguser;

--
-- Name: index_seasontickets_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_seasontickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_seasontickets_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_seasontickets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_seasontickets_id_seq OWNED BY public.index_seasontickets.id;


--
-- Name: index_tickets; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.index_tickets (
    id integer NOT NULL,
    nameseasontickets character varying(150) NOT NULL,
    numberofdays character varying(50) NOT NULL,
    "time" character varying(50) NOT NULL,
    price integer NOT NULL
);


ALTER TABLE public.index_tickets OWNER TO paymentforparkinguser;

--
-- Name: index_tickets_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.index_tickets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.index_tickets_id_seq OWNER TO paymentforparkinguser;

--
-- Name: index_tickets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.index_tickets_id_seq OWNED BY public.index_tickets.id;


--
-- Name: robokassa_successnotification; Type: TABLE; Schema: public; Owner: paymentforparkinguser
--

CREATE TABLE public.robokassa_successnotification (
    id integer NOT NULL,
    "InvId" integer NOT NULL,
    "OutSum" character varying(15) NOT NULL,
    created_at timestamp with time zone NOT NULL
);


ALTER TABLE public.robokassa_successnotification OWNER TO paymentforparkinguser;

--
-- Name: robokassa_successnotification_id_seq; Type: SEQUENCE; Schema: public; Owner: paymentforparkinguser
--

CREATE SEQUENCE public.robokassa_successnotification_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.robokassa_successnotification_id_seq OWNER TO paymentforparkinguser;

--
-- Name: robokassa_successnotification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: paymentforparkinguser
--

ALTER SEQUENCE public.robokassa_successnotification_id_seq OWNED BY public.robokassa_successnotification.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: index_paidparking id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidparking ALTER COLUMN id SET DEFAULT nextval('public.index_paidparking_id_seq'::regclass);


--
-- Name: index_paidseasontickets id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidseasontickets ALTER COLUMN id SET DEFAULT nextval('public.index_paidseasontickets_id_seq'::regclass);


--
-- Name: index_paidtickets id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidtickets ALTER COLUMN id SET DEFAULT nextval('public.index_paidtickets_id_seq'::regclass);


--
-- Name: index_parking id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking ALTER COLUMN id SET DEFAULT nextval('public.index_parking_id_seq'::regclass);


--
-- Name: index_parking_seasontickets id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_seasontickets ALTER COLUMN id SET DEFAULT nextval('public.index_parking_seasontickets_id_seq'::regclass);


--
-- Name: index_parking_tickets id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_tickets ALTER COLUMN id SET DEFAULT nextval('public.index_parking_tickets_id_seq'::regclass);


--
-- Name: index_seasontickets id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_seasontickets ALTER COLUMN id SET DEFAULT nextval('public.index_seasontickets_id_seq'::regclass);


--
-- Name: index_tickets id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_tickets ALTER COLUMN id SET DEFAULT nextval('public.index_tickets_id_seq'::regclass);


--
-- Name: robokassa_successnotification id; Type: DEFAULT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.robokassa_successnotification ALTER COLUMN id SET DEFAULT nextval('public.robokassa_successnotification_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add parking	7	add_parking
26	Can change parking	7	change_parking
27	Can delete parking	7	delete_parking
28	Can view parking	7	view_parking
29	Can add Абонемент	8	add_seasontickets
30	Can change Абонемент	8	change_seasontickets
31	Can delete Абонемент	8	delete_seasontickets
32	Can view Абонемент	8	view_seasontickets
33	Can add Парковка	9	add_tickets
34	Can change Парковка	9	change_tickets
35	Can delete Парковка	9	delete_tickets
36	Can view Парковка	9	view_tickets
37	Can add Уведомление об успешном платеже	10	add_successnotification
38	Can change Уведомление об успешном платеже	10	change_successnotification
39	Can delete Уведомление об успешном платеже	10	delete_successnotification
40	Can view Уведомление об успешном платеже	10	view_successnotification
41	Can add Оплаченная парковка	11	add_paidparking
42	Can change Оплаченная парковка	11	change_paidparking
43	Can delete Оплаченная парковка	11	delete_paidparking
44	Can view Оплаченная парковка	11	view_paidparking
45	Can add paidtickets	12	add_paidtickets
46	Can change paidtickets	12	change_paidtickets
47	Can delete paidtickets	12	delete_paidtickets
48	Can view paidtickets	12	view_paidtickets
49	Can add Оплаченный абонемент	13	add_paidseasontickets
50	Can change Оплаченный абонемент	13	change_paidseasontickets
51	Can delete Оплаченный абонемент	13	delete_paidseasontickets
52	Can view Оплаченный абонемент	13	view_paidseasontickets
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$216000$nvCRena9Wnuo$+vUknCss15H6WdYrN6jfcl1MYqjCfsF847+5C2Yrf4o=	2021-04-14 15:43:07.307635+00	t	UEPHEjM2Lk			ilyabukanov@mail.ru	t	t	2021-01-13 16:56:38.179327+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-01-18 11:43:19.109935+00	1	Parking object (1)	1	[{"added": {}}]	7	1
2	2021-01-18 12:10:59.936678+00	2	Parking object (2)	1	[{"added": {}}]	7	1
3	2021-01-18 13:05:12.907018+00	1	ул. Балканская, 26	2	[]	7	1
4	2021-01-18 13:08:52.630847+00	2	ул. 9-я Парковая, 5	2	[]	7	1
5	2021-01-18 14:07:09.586707+00	3	ул. Ратная, 27	1	[{"added": {}}]	7	1
6	2021-01-19 14:35:54.33433+00	2	ул. 9-я Парковая, 5	3		7	1
7	2021-01-19 14:35:54.348324+00	1	ул. Балканская, 26	3		7	1
8	2021-01-19 14:36:21.999702+00	4	ул. Балканская, 26	1	[{"added": {}}]	7	1
9	2021-01-19 15:00:17.381449+00	5	Улица Ратная, дом 10, строение 51	1	[{"added": {}}]	7	1
10	2021-01-19 15:01:01.00712+00	5	Улица Ратная, дом 10, строение 51	3		7	1
11	2021-01-20 12:30:58.473076+00	1	Seasontickets object (1)	1	[{"added": {}}]	8	1
12	2021-01-20 12:32:13.644475+00	2	Seasontickets object (2)	1	[{"added": {}}]	8	1
13	2021-01-20 12:37:46.670254+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["Seasontickets"]}}]	7	1
14	2021-01-20 12:38:09.825327+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["Seasontickets"]}}]	7	1
15	2021-01-20 12:38:51.938656+00	4	ул. Балканская, 26	2	[]	7	1
16	2021-01-20 13:22:04.849019+00	1	tickets object (1)	1	[{"added": {}}]	9	1
17	2021-01-20 13:24:11.779317+00	2	Абонемент для парковки на балканской на 30 дней	1	[{"added": {}}]	9	1
18	2021-01-20 13:25:23.99075+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u0410\\u0431\\u043e\\u043d\\u0435\\u043c\\u0435\\u043d\\u0442"]}}]	7	1
19	2021-01-20 13:25:37.192126+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u0410\\u0431\\u043e\\u043d\\u0435\\u043c\\u0435\\u043d\\u0442"]}}]	7	1
20	2021-01-20 13:34:51.149932+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["Tickets"]}}]	7	1
21	2021-01-20 13:37:13.879837+00	4	ул. Балканская, 26	2	[]	7	1
22	2021-01-20 13:37:21.962716+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u0410\\u0431\\u043e\\u043d\\u0435\\u043c\\u0435\\u043d\\u0442\\u044b"]}}]	7	1
23	2021-01-20 13:55:26.107741+00	2	Парковка на Балканской 30 дней	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
24	2021-01-20 13:55:42.154974+00	1	Парковка на Ратной на 30 дней	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
25	2021-01-20 13:56:14.895847+00	2	Для Балканской на 30 дней	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
26	2021-01-20 13:56:24.218077+00	1	Для Ратной на 30 дней	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
27	2021-01-20 13:57:13.864253+00	3	Для Балканской на 365 дней	1	[{"added": {}}]	9	1
28	2021-01-20 13:57:38.898321+00	4	Для Ратной на 365 дней	1	[{"added": {}}]	9	1
29	2021-01-20 13:58:09.490444+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u0410\\u0431\\u043e\\u043d\\u0435\\u043c\\u0435\\u043d\\u0442\\u044b"]}}]	7	1
30	2021-01-20 13:58:17.547485+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u0410\\u0431\\u043e\\u043d\\u0435\\u043c\\u0435\\u043d\\u0442\\u044b"]}}]	7	1
31	2021-01-20 14:15:32.387688+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u0441\\u0432\\u043e\\u0431\\u043e\\u0434\\u043d\\u044b\\u0445 \\u043c\\u0435\\u0441\\u0442"]}}]	7	1
32	2021-01-20 14:15:41.339153+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u041a\\u043e\\u043b\\u0438\\u0447\\u0435\\u0441\\u0442\\u0432\\u043e \\u0441\\u0432\\u043e\\u0431\\u043e\\u0434\\u043d\\u044b\\u0445 \\u043c\\u0435\\u0441\\u0442"]}}]	7	1
33	2021-01-28 10:28:24.019455+00	4	paidparking object (4)	1	[{"added": {}}]	11	1
34	2021-01-28 10:37:30.803339+00	5	paidparking object (5)	1	[{"added": {}}]	11	1
35	2021-01-28 13:10:10.884334+00	8	paidparking object (8)	3		11	1
36	2021-01-28 13:10:10.893531+00	7	paidparking object (7)	3		11	1
37	2021-01-28 13:10:10.898502+00	6	paidparking object (6)	3		11	1
38	2021-01-28 13:10:10.903373+00	5	paidparking object (5)	3		11	1
39	2021-01-28 13:10:10.908836+00	4	paidparking object (4)	3		11	1
40	2021-01-28 13:11:20.474328+00	11	paidparking object (11)	3		11	1
41	2021-01-28 13:11:20.482823+00	10	paidparking object (10)	3		11	1
42	2021-01-28 13:11:20.488595+00	9	paidparking object (9)	3		11	1
43	2021-01-28 13:11:27.649677+00	12	paidparking object (12)	3		11	1
44	2021-01-28 13:12:57.039422+00	15	paidparking object (15)	3		11	1
45	2021-01-28 13:12:57.046229+00	14	paidparking object (14)	3		11	1
46	2021-01-28 13:12:57.051474+00	13	paidparking object (13)	3		11	1
47	2021-01-28 14:11:10.218353+00	19	paidparking object (19)	3		11	1
48	2021-01-28 14:11:10.223438+00	18	paidparking object (18)	3		11	1
49	2021-01-28 14:11:10.225944+00	17	paidparking object (17)	3		11	1
50	2021-01-28 14:11:10.228043+00	16	paidparking object (16)	3		11	1
51	2021-01-28 14:15:27.914844+00	20	paidparking object (20)	3		11	1
52	2021-01-29 11:03:54.757482+00	22	paidparking object (22)	3		11	1
53	2021-01-29 11:03:54.770658+00	21	paidparking object (21)	3		11	1
54	2021-01-29 11:07:32.107784+00	23	paidparking object (23)	3		11	1
55	2021-01-29 13:07:22.241915+00	4	Абонемент для парковки на Ратной на 365 дней с круглосуточным временем работы	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
56	2021-01-29 13:11:42.246153+00	1	paidseasontickets object (1)	1	[{"added": {}}]	13	1
57	2021-02-01 08:50:40.751941+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
58	2021-02-01 08:50:48.117269+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
59	2021-02-01 08:51:03.810793+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
60	2021-02-01 08:51:11.791347+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
135	2021-03-21 18:30:22.88338+00	85	paidparking object (85)	3		11	1
136	2021-03-21 18:30:22.885404+00	84	paidparking object (84)	3		11	1
61	2021-02-01 09:30:52.638118+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
62	2021-02-01 12:04:38.822182+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
63	2021-02-01 12:07:05.026362+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
64	2021-02-01 12:07:13.254858+00	3	ул. Ратная, 27	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
65	2021-02-01 12:22:48.234326+00	4	ул. Балканская, 26	2	[{"changed": {"fields": ["\\u041c\\u0438\\u043d\\u0438\\u043c\\u0430\\u043b\\u044c\\u043d\\u043e\\u0435 \\u0432\\u0440\\u0435\\u043c\\u044f \\u0434\\u043b\\u044f \\u043e\\u043f\\u043b\\u0430\\u0442\\u044b"]}}]	7	1
66	2021-02-01 14:15:47.571128+00	29	paidparking object (29)	3		11	1
67	2021-02-01 14:15:47.583348+00	28	paidparking object (28)	3		11	1
68	2021-02-01 14:15:47.589003+00	27	paidparking object (27)	3		11	1
69	2021-02-01 14:15:47.594137+00	26	paidparking object (26)	3		11	1
70	2021-02-01 14:15:47.59899+00	25	paidparking object (25)	3		11	1
71	2021-02-01 14:15:47.604493+00	24	paidparking object (24)	3		11	1
72	2021-02-01 14:15:56.568212+00	4	paidseasontickets object (4)	3		13	1
73	2021-02-01 14:15:56.577161+00	3	paidseasontickets object (3)	3		13	1
74	2021-02-01 14:15:56.582457+00	2	paidseasontickets object (2)	3		13	1
75	2021-02-01 14:15:56.588264+00	1	paidseasontickets object (1)	3		13	1
76	2021-02-05 11:30:59.471318+00	5	paidseasontickets object (5)	3		13	1
77	2021-02-05 11:31:07.218198+00	30	paidparking object (30)	3		11	1
78	2021-02-10 09:05:26.748738+00	8	paidseasontickets object (8)	1	[{"added": {}}]	13	1
79	2021-02-10 09:12:46.534647+00	8	paidseasontickets object (8)	3		13	1
80	2021-02-10 09:12:46.543055+00	7	paidseasontickets object (7)	3		13	1
81	2021-02-10 09:12:46.548091+00	6	paidseasontickets object (6)	3		13	1
82	2021-02-10 09:12:57.777146+00	33	paidparking object (33)	3		11	1
83	2021-02-10 09:12:57.784863+00	32	paidparking object (32)	3		11	1
84	2021-02-10 09:12:57.789975+00	31	paidparking object (31)	3		11	1
85	2021-02-13 11:10:52.685008+00	1	Для Ратной на 30 дней	2	[]	9	1
86	2021-02-14 09:58:59.720187+00	1	Абонемент для парковки на Ратной на 30 дней с круглосуточным временем работы	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
87	2021-02-14 09:59:52.222495+00	3	Абонемент для парковки на Балканской на 365 дней с круглосуточным временем работы	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
88	2021-02-14 10:00:05.198022+00	2	Абонемент для парковки на Балканской на 30 дней с круглосуточным временем работы	2	[{"changed": {"fields": ["\\u041d\\u0430\\u0438\\u043c\\u0435\\u043d\\u043e\\u0432\\u0430\\u043d\\u0438\\u0435"]}}]	9	1
89	2021-02-14 10:00:55.302517+00	34	paidparking object (34)	3		11	1
90	2021-02-19 09:17:40.230154+00	40	paidparking object (40)	3		11	1
91	2021-02-19 09:17:40.24161+00	39	paidparking object (39)	3		11	1
92	2021-02-19 09:17:40.247663+00	38	paidparking object (38)	3		11	1
93	2021-02-19 09:17:40.252855+00	37	paidparking object (37)	3		11	1
94	2021-02-19 09:17:40.258543+00	36	paidparking object (36)	3		11	1
95	2021-02-19 09:17:40.264436+00	35	paidparking object (35)	3		11	1
96	2021-02-19 09:18:00.830244+00	14	paidseasontickets object (14)	3		13	1
97	2021-02-19 09:18:00.839491+00	13	paidseasontickets object (13)	3		13	1
98	2021-02-19 09:18:00.845158+00	12	paidseasontickets object (12)	3		13	1
99	2021-02-19 09:18:00.850274+00	11	paidseasontickets object (11)	3		13	1
100	2021-02-19 09:18:00.856455+00	10	paidseasontickets object (10)	3		13	1
101	2021-02-19 09:18:00.862021+00	9	paidseasontickets object (9)	3		13	1
102	2021-02-20 07:20:40.874132+00	15	paidseasontickets object (15)	3		13	1
103	2021-02-20 07:20:48.901868+00	41	paidparking object (41)	3		11	1
104	2021-03-11 09:02:16.489332+00	17	paidseasontickets object (17)	3		13	1
105	2021-03-11 09:02:16.495567+00	16	paidseasontickets object (16)	3		13	1
106	2021-03-11 09:02:22.54737+00	44	paidparking object (44)	3		11	1
107	2021-03-11 09:02:22.552874+00	43	paidparking object (43)	3		11	1
108	2021-03-11 09:02:22.556124+00	42	paidparking object (42)	3		11	1
109	2021-03-12 15:41:30.120167+00	46	paidparking object (46)	3		11	1
110	2021-03-12 15:41:30.133165+00	45	paidparking object (45)	3		11	1
111	2021-03-12 15:43:22.942498+00	47	paidparking object (47)	3		11	1
112	2021-03-12 16:55:31.897803+00	18	paidseasontickets object (18)	3		13	1
113	2021-03-15 09:48:03.872108+00	19	paidseasontickets object (19)	3		13	1
114	2021-03-15 09:48:10.021679+00	48	paidparking object (48)	3		11	1
115	2021-03-15 09:59:48.333223+00	49	paidparking object (49)	3		11	1
116	2021-03-15 10:19:59.444003+00	21	paidseasontickets object (21)	3		13	1
117	2021-03-15 10:19:59.452833+00	20	paidseasontickets object (20)	3		13	1
118	2021-03-15 10:20:07.044635+00	50	paidparking object (50)	3		11	1
119	2021-03-18 14:26:49.898753+00	24	paidseasontickets object (24)	3		13	1
120	2021-03-18 14:26:49.90858+00	23	paidseasontickets object (23)	3		13	1
121	2021-03-18 14:26:49.910588+00	22	paidseasontickets object (22)	3		13	1
122	2021-03-18 14:26:55.179119+00	51	paidparking object (51)	3		11	1
123	2021-03-18 14:53:29.993648+00	26	paidseasontickets object (26)	3		13	1
124	2021-03-18 14:53:29.996628+00	25	paidseasontickets object (25)	3		13	1
125	2021-03-18 14:53:39.748123+00	54	paidparking object (54)	3		11	1
126	2021-03-18 14:53:39.752804+00	53	paidparking object (53)	3		11	1
127	2021-03-18 14:53:39.755064+00	52	paidparking object (52)	3		11	1
128	2021-03-21 18:30:22.868123+00	92	paidparking object (92)	3		11	1
129	2021-03-21 18:30:22.872273+00	91	paidparking object (91)	3		11	1
130	2021-03-21 18:30:22.874269+00	90	paidparking object (90)	3		11	1
131	2021-03-21 18:30:22.876061+00	89	paidparking object (89)	3		11	1
132	2021-03-21 18:30:22.877751+00	88	paidparking object (88)	3		11	1
133	2021-03-21 18:30:22.879445+00	87	paidparking object (87)	3		11	1
134	2021-03-21 18:30:22.881426+00	86	paidparking object (86)	3		11	1
137	2021-03-21 18:30:22.887021+00	83	paidparking object (83)	3		11	1
138	2021-03-21 18:30:22.889292+00	82	paidparking object (82)	3		11	1
139	2021-03-21 18:30:22.890511+00	81	paidparking object (81)	3		11	1
140	2021-03-21 18:30:22.891788+00	80	paidparking object (80)	3		11	1
141	2021-03-21 18:30:22.893677+00	79	paidparking object (79)	3		11	1
142	2021-03-21 18:30:22.895486+00	78	paidparking object (78)	3		11	1
143	2021-03-21 18:30:22.897361+00	77	paidparking object (77)	3		11	1
144	2021-03-21 18:30:22.899169+00	76	paidparking object (76)	3		11	1
145	2021-03-21 18:30:22.900577+00	75	paidparking object (75)	3		11	1
146	2021-03-21 18:30:22.902526+00	74	paidparking object (74)	3		11	1
147	2021-03-21 18:30:22.904524+00	73	paidparking object (73)	3		11	1
148	2021-03-21 18:30:22.906341+00	72	paidparking object (72)	3		11	1
149	2021-03-21 18:30:22.90808+00	71	paidparking object (71)	3		11	1
150	2021-03-21 18:30:22.909795+00	70	paidparking object (70)	3		11	1
151	2021-03-21 18:30:22.911464+00	69	paidparking object (69)	3		11	1
152	2021-03-21 18:30:22.913181+00	68	paidparking object (68)	3		11	1
153	2021-03-21 18:30:22.914883+00	67	paidparking object (67)	3		11	1
154	2021-03-21 18:30:22.917103+00	66	paidparking object (66)	3		11	1
155	2021-03-21 18:30:22.918916+00	65	paidparking object (65)	3		11	1
156	2021-03-21 18:30:22.920838+00	64	paidparking object (64)	3		11	1
157	2021-03-21 18:30:22.922426+00	63	paidparking object (63)	3		11	1
158	2021-03-21 18:30:22.924027+00	62	paidparking object (62)	3		11	1
159	2021-03-21 18:30:22.925484+00	61	paidparking object (61)	3		11	1
160	2021-03-21 18:30:22.926987+00	60	paidparking object (60)	3		11	1
161	2021-03-21 18:30:22.928451+00	59	paidparking object (59)	3		11	1
162	2021-03-21 18:30:22.930313+00	58	paidparking object (58)	3		11	1
163	2021-03-21 18:30:22.932291+00	57	paidparking object (57)	3		11	1
164	2021-03-21 18:30:22.933869+00	56	paidparking object (56)	3		11	1
165	2021-03-21 18:30:22.935784+00	55	paidparking object (55)	3		11	1
166	2021-04-04 14:51:45.173689+00	30	paidseasontickets object (30)	3		13	1
167	2021-04-04 14:51:45.184895+00	29	paidseasontickets object (29)	3		13	1
168	2021-04-04 14:51:45.18723+00	28	paidseasontickets object (28)	3		13	1
169	2021-04-04 14:51:45.18935+00	27	paidseasontickets object (27)	3		13	1
170	2021-04-04 14:51:54.576079+00	118	paidparking object (118)	3		11	1
171	2021-04-04 14:51:54.580844+00	117	paidparking object (117)	3		11	1
172	2021-04-04 14:51:54.583351+00	116	paidparking object (116)	3		11	1
173	2021-04-04 14:51:54.585958+00	115	paidparking object (115)	3		11	1
174	2021-04-04 14:51:54.588743+00	114	paidparking object (114)	3		11	1
175	2021-04-04 14:51:54.591748+00	113	paidparking object (113)	3		11	1
176	2021-04-04 14:51:54.594193+00	112	paidparking object (112)	3		11	1
177	2021-04-04 14:51:54.596832+00	111	paidparking object (111)	3		11	1
178	2021-04-04 14:51:54.599256+00	110	paidparking object (110)	3		11	1
179	2021-04-04 14:51:54.602091+00	109	paidparking object (109)	3		11	1
180	2021-04-04 14:51:54.605096+00	108	paidparking object (108)	3		11	1
181	2021-04-04 14:51:54.607954+00	107	paidparking object (107)	3		11	1
182	2021-04-04 14:51:54.61059+00	106	paidparking object (106)	3		11	1
183	2021-04-04 14:51:54.613013+00	105	paidparking object (105)	3		11	1
184	2021-04-04 14:51:54.615161+00	104	paidparking object (104)	3		11	1
185	2021-04-04 14:51:54.617282+00	103	paidparking object (103)	3		11	1
186	2021-04-04 14:51:54.619511+00	102	paidparking object (102)	3		11	1
187	2021-04-04 14:51:54.622233+00	101	paidparking object (101)	3		11	1
188	2021-04-04 14:51:54.625053+00	100	paidparking object (100)	3		11	1
189	2021-04-04 14:51:54.62744+00	99	paidparking object (99)	3		11	1
190	2021-04-04 14:51:54.630082+00	98	paidparking object (98)	3		11	1
191	2021-04-04 14:51:54.633304+00	97	paidparking object (97)	3		11	1
192	2021-04-04 14:51:54.636461+00	96	paidparking object (96)	3		11	1
193	2021-04-04 14:51:54.639663+00	95	paidparking object (95)	3		11	1
194	2021-04-04 14:51:54.642875+00	94	paidparking object (94)	3		11	1
195	2021-04-04 14:51:54.645359+00	93	paidparking object (93)	3		11	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	index	parking
8	index	seasontickets
9	index	tickets
10	robokassa	successnotification
11	index	paidparking
12	index	paidtickets
13	index	paidseasontickets
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-01-13 12:09:35.84494+00
2	auth	0001_initial	2021-01-13 12:09:35.925149+00
3	admin	0001_initial	2021-01-13 12:09:36.091716+00
4	admin	0002_logentry_remove_auto_add	2021-01-13 12:09:36.140578+00
5	admin	0003_logentry_add_action_flag_choices	2021-01-13 12:09:36.172525+00
6	contenttypes	0002_remove_content_type_name	2021-01-13 12:09:36.225088+00
7	auth	0002_alter_permission_name_max_length	2021-01-13 12:09:36.254316+00
8	auth	0003_alter_user_email_max_length	2021-01-13 12:09:36.284279+00
9	auth	0004_alter_user_username_opts	2021-01-13 12:09:36.313643+00
10	auth	0005_alter_user_last_login_null	2021-01-13 12:09:36.344599+00
11	auth	0006_require_contenttypes_0002	2021-01-13 12:09:36.352626+00
12	auth	0007_alter_validators_add_error_messages	2021-01-13 12:09:36.380502+00
13	auth	0008_alter_user_username_max_length	2021-01-13 12:09:36.417304+00
14	auth	0009_alter_user_last_name_max_length	2021-01-13 12:09:36.446993+00
15	auth	0010_alter_group_name_max_length	2021-01-13 12:09:36.479816+00
16	auth	0011_update_proxy_permissions	2021-01-13 12:09:36.506629+00
17	auth	0012_alter_user_first_name_max_length	2021-01-13 12:09:36.535328+00
18	sessions	0001_initial	2021-01-13 12:09:36.562148+00
19	index	0001_initial	2021-01-18 11:11:43.826111+00
20	index	0002_auto_20210120_1212	2021-01-20 12:14:56.449157+00
21	index	0002_auto_20210120_1313	2021-01-20 13:16:30.505587+00
22	index	0002_auto_20210120_1316	2021-01-20 13:17:09.489046+00
23	index	0002_auto_20210120_1319	2021-01-20 13:20:00.690257+00
24	index	0003_auto_20210120_1332	2021-01-20 13:32:22.584596+00
25	index	0004_auto_20210120_1413	2021-01-20 14:14:03.47623+00
26	robokassa	0001_initial	2021-01-26 13:58:37.71989+00
27	index	0005_paidparking	2021-01-28 09:56:27.674356+00
28	index	0006_auto_20210128_1025	2021-01-28 10:25:44.242342+00
29	index	0006_auto_20210129_1149	2021-01-29 11:49:41.026448+00
30	index	0005_paidparking_paidtickets	2021-01-29 11:57:36.33334+00
31	index	0006_paidseasontickets	2021-01-29 12:51:15.932465+00
32	index	0007_remove_paidparking_email	2021-01-29 13:04:30.732253+00
33	index	0008_auto_20210129_1310	2021-01-29 13:10:43.479581+00
34	index	0009_auto_20210201_1055	2021-02-01 10:56:07.635527+00
35	index	0010_auto_20210201_1057	2021-02-01 10:57:12.471754+00
36	index	0011_auto_20210201_1432	2021-02-01 14:32:33.900185+00
37	index	0012_auto_20210201_1433	2021-02-01 14:33:31.716731+00
38	index	0013_auto_20210205_1150	2021-02-05 11:50:26.899163+00
39	index	0014_auto_20210205_1522	2021-02-05 12:22:35.579762+00
40	index	0015_paidparking_email	2021-03-11 08:30:06.046136+00
41	index	0016_paidseasontickets_email	2021-03-11 08:31:06.843244+00
42	index	0017_auto_20210311_1200	2021-03-11 09:00:03.934776+00
43	index	0018_auto_20210311_1238	2021-03-11 09:39:03.048285+00
44	index	0019_auto_20210311_1313	2021-03-11 10:13:35.811233+00
45	index	0020_auto_20210315_1318	2021-03-15 10:18:28.462047+00
46	index	0021_auto_20210321_1920	2021-03-21 16:21:03.935156+00
47	index	0021_auto_20210321_1945	2021-03-21 16:45:13.46159+00
48	index	0021_auto_20210325_1735	2021-03-25 14:35:28.542869+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
8j3kshhnbbxf59ombcurj5r5xjaledea	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1kzjSK:wtHvUQd1zJsilKsp82-1s-swRcBGXcf1sP09_JPLxG0	2021-01-27 16:57:12.413749+00
mwzo8s5dqelsutt9fl4so5jgnamrpdq3	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1l9lgk:6svDj4ANPtgDQQT3DalsqUlfcp8hXVrBbQwxgxJmEn4	2021-02-24 09:21:34.12636+00
eqtxu0jfqmiwjepr3huhmnpiq0b7uc8j	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lArb2:d37Oamg40n8EpZLPTvMSWdL0vQ2H5D5eIzGYSy-1-Cs	2021-02-27 09:52:12.959009+00
jgkn9wswm1ncqtgo3bt9imzqh6s732ld	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lBcIL:UAUUl_O84rxAB5XLH3WLqcsNfr0DyITnkzSaxkHYd7M	2021-03-01 11:44:01.708331+00
rwpixjano9v9k9y0dgagpk4rohz5hk8d	.eJyrVirIyM9LzSvNTUotUrJC4dUCAKU3CwE:1lD1wS:Lkgrm-HbWoIl56uW0Avh-1I6FrqCQb9OvOzsI0ZXxlQ	2021-03-05 09:19:16.738458+00
dpeb1tk1zfv2b09e977lxk1m3bjag77e	.eJxVjMsOwiAURP-FtSFguVRcuvcbyOVxpT7AQLsy_rs06aIuZ-bM-TCLy5zs0mK1U2BnJtlh3zn0j5jXIdwx3wr3Jc91cnxF-LY2fi0hPi8b-ydI2FJ_o5dBGW3AwxAUHIXQMAZSgmhwGkfQZBT5gbzSEhBJGBxPvZXSAJHq0ncqOebl5WLtwn36_gB__UHp:1lDNO5:vIkp1xbQLI2HQD-UJYQ3h7eQXQGKXJd98G9JsyGBkEY	2021-03-06 08:13:13.151046+00
87bk04gbmkmbrdss7ddc4dy29ov4nvws	.eJxVjMsOwiAURP-FtSFguVRcuvcbyOVxpT7AQLsy_rs06aIuZ-bM-TCLy5zs0mK1U2BnJtlh3zn0j5jXIdwx3wr3Jc91cnxF-LY2fi0hPi8b-ydI2FJ_o5dBGW3AwxAUHIXQMAZSgmhwGkfQZBT5gbzSEhBJGBxPvZXSAJHq0ncqOebl5WLtwn36_gB__UHp:1lEq7G:02qd7RglUQ6suB3whL-HmTj4CZdiTIKyPzcSQSEEq3w	2021-03-10 09:05:54.721908+00
r40tklu95j35lsmkmmuwycjimya3z2rc	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lLi0W:9y5eJ5EXp0lBnM-EDCMiNxfBa-b12HIslb4DYw1tHBc	2021-03-29 07:51:20.444542+00
58mvb1qoigetchapou6qxqo8sp3lgqxn	.eJxVjMsOwiAURP-FtSFguVRcuvcbyOVxpT7AQLsy_rs06aIuZ-bM-TCLy5zs0mK1U2BnJtlh3zn0j5jXIdwx3wr3Jc91cnxF-LY2fi0hPi8b-ydI2FJ_o5dBGW3AwxAUHIXQMAZSgmhwGkfQZBT5gbzSEhBJGBxPvZXSAJHq0ncqOebl5WLtwn36_gB__UHp:1lMu3U:BDF0aTgtEVVb6J1mwsKzI4iiPzV3RX2CG5NbPsmAuLM	2021-04-01 14:55:20.983222+00
jjg8ovpgvypo4mt29vsv2iret2ezd2nw	.eJxVjDkOwjAQRe_iGlmexOPElPScIRovg8NiR1kqxN1xpBTQvvf_e4uBtjUN2xLnYQziLECcfpkj_4h5F-FO-VakL3mdRyf3iTzsIq8lxOfl2P4FEi2pvslD0NZY9NgGjY1SBrvAWjG3zlCHhq1m37LXBpCIlaWurxTAIrOu0SmVHPP2cnGuwd5CrTRgNIrPF2y-P4E:1lT3aj:xFcWLfK_J0oc3LY8DE3Y16nR0PVavvQY832aSJQENwU	2021-04-04 14:20:05.654419+00
n1ok0tr66womfinc8fm7oeq7c5jgkps4	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lT468:2Dqr04rgNz-OYXzfRWMM0sZvRLFBECa0jXI2LBxtM0s	2021-04-04 15:01:32.013879+00
rf0wcse3nbyc0e79jgf4ojpegno4d5p5	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lT7GU:hh62_cfzgQWouOPR0qLHMHD8RjLGJFhpttw31jexej4	2021-04-04 18:24:26.603503+00
hmob8przkqajxrr84qb6kqi6nmci0tbn	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lTPqa:prw7qWHX-Urgec6n3s4xU9xNwWbdU7hx_EG4rPh4-ac	2021-04-05 14:14:56.959041+00
rcvni5wmnunfmfbpz89j88px8d519xl8	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lTRFo:gDP-qJQr7PNUdlT7q6HYcSGm8IXYeGwSK8tdVHor1B8	2021-04-05 15:45:04.806442+00
p24677104dphhulamkdoxeumfvyqyvu6	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lVzfg:j4vbR0Av_ORfnCEOzP-nwsdJYhSFyge5cu78j3OmM04	2021-04-12 16:54:20.651464+00
6szxmxu5216vevanaa68bhizwdfvp6ac	eyJwaG9uZW51bWJlciI6Ijg5MTUyMDIxNjQ1In0:1lW0V5:It-VafG892v64QJ_etxA3pluoH0KbjDmRlGO58rv_Ic	2021-04-12 17:47:27.504006+00
cqci6zx5bjcqrnyrfscp3n6if69aug7x	eyJwaG9uZW51bWJlciI6Ijg5MTUyMDIxNjQ1In0:1lW1WL:NQ6S7pvQN9pIc52-QEg5Bm8On9AzXJfLyX9cywH7RRE	2021-04-12 18:52:49.515+00
yihz1bd0xj97dqwpc9htqibtor451oa8	eyJwaG9uZW51bWJlciI6Ijg5MTUyMDIxNjQ1In0:1lW1nY:K4yoDgYkaCPIDMgxqY08wJp9Fiqt8pZ_e0acAQcdkz0	2021-04-12 19:01:36.496526+00
tv1d7yrjeahcu755njgj4nm4m4r8xlef	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lW1pe:4E73sWxEykPpZF9rtnxoD_tdsZPybq_OD6miom1Q9ro	2021-04-12 19:03:46.920812+00
0j1x9bolnuz2hao6huz4mz8k2sdenhw7	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lWFgI:tgFIX8Wm7BppN4Alcoe3MHxTWbaivT9OcJ_xHrKAaVM	2021-04-13 09:51:02.541783+00
5x6e18csq9dch8ikgn1taxrddww4ak44	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lWFiJ:s8It4jtr4a3ziXfyTntIYPFcqtuV6mTAJvsfDVF_ccY	2021-04-13 09:53:07.787968+00
of4u2e0jih43o9fz7cw8xyk5d2btoiz6	eyJwaG9uZW51bWJlciI6Ijg5MTUyMDIxNjQ1In0:1lWFr1:aMUrO-BHB-hCeSS3oIxbflU0U_i_8K7Vepsx0PRUV_4	2021-04-13 10:02:07.738944+00
xrgijr41kaolvvr1coixdsm54x8ntb0r	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lWMso:gVZFk-8ZMNfMzufMLJZEsAS1t7tWvk-xffzcA0RwIRw	2021-04-13 17:32:26.186026+00
j84bu02xc69xuy83llfetcmj9age7vz4	e30:1lWhMV:YAD9g2lqGV1RNkttNEnOam1RK6YSaURJN2VS4UZFKKc	2021-04-14 15:33:27.63326+00
sym9guvqtdcrtw65haq1bxidw7dcxfhx	.eJxVjMsOwiAQRf-FtSFgZ0Bcuu83kOExUjWQlHZl_HfbpAvdnnPufQtP61L82vPspySuQovTLwsUn7nuIj2o3puMrS7zFOSeyMN2ObaUX7ej_Tso1Mu2pqgTOOMw4pAAz0oZtIlBMQ_BkEXDDjgOHMFoJGLlyF42qrVDZhCfL9nKN7U:1lWhfX:aZnADOj4B50UK_6s-b4pjKNaKuNlVIInLGYpYtIPzLY	2021-04-14 15:53:07.310665+00
eio7ru8d1c5qywflhwpggs2s0pfmloaf	eyJwaG9uZW51bWJlciI6Ijg5MTUyMDIxNjQ1In0:1lWhsb:j2Os1NtcA0um7LYGhaw0eAcL9HaK-aj7bt17wb9wusE	2021-04-14 16:06:37.315158+00
\.


--
-- Data for Name: index_paidparking; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_paidparking (id, carnumber, amountoftime, price, telephone, adress_id, datetimepaidparking, email, expirationdate, enddateandtime, expirationtime) FROM stdin;
119	Х505ХА777	1	150	89152021645	3	2021-04-04 18:10:30.545839+00	ilyabukanov@mail.ru	2021-04-30	2021-04-30 03:15:00+00	03:15:00
120	Х505ХА777	1	150	89152021645	3	2021-04-14 15:23:10.599167+00	ilyabukanov@mail.ru	2021-04-30	2021-04-30 00:25:00+00	00:25:00
\.


--
-- Data for Name: index_paidseasontickets; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_paidseasontickets (id, carnumber, price, telephone, nametickets_id, datetimepaidtickets, email, expirationdate, enddateandtime, expirationtime) FROM stdin;
31	Х505ХА777	250000	89152021645	4	2021-04-04 18:11:16.090591+00	ilyabukanov@mail.ru	2021-04-30	2022-04-30 00:15:00+00	03:15:00
\.


--
-- Data for Name: index_paidtickets; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_paidtickets (id, carnumber, numberofdays, "time", price, telephone, email, name_id) FROM stdin;
\.


--
-- Data for Name: index_parking; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_parking (id, adress, workinghours, minimaltimeforpayment, price, numberofavailableseats) FROM stdin;
3	ул. Ратная, 27	C 8:00 до 21:00	1 час	150	150
4	ул. Балканская, 26	Круглосуточно	3 часа	250	250
\.


--
-- Data for Name: index_parking_seasontickets; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_parking_seasontickets (id, parking_id, seasontickets_id) FROM stdin;
1	4	1
2	4	2
\.


--
-- Data for Name: index_parking_tickets; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_parking_tickets (id, parking_id, tickets_id) FROM stdin;
1	4	1
4	3	2
5	4	4
6	3	3
\.


--
-- Data for Name: index_seasontickets; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_seasontickets (id, numberofdays, "time", price) FROM stdin;
1	30	10:00 - 18:00	20000
2	360	Круглосуточно	360000
\.


--
-- Data for Name: index_tickets; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.index_tickets (id, nameseasontickets, numberofdays, "time", price) FROM stdin;
4	Абонемент для парковки на Ратной на 365 дней с круглосуточным временем работы	365	Круглосуточно	250000
1	Абонемент для парковки на Ратной на 30 дней с круглосуточным временем работы	30	Круглосуточно	20000
3	Абонемент для парковки на Балканской на 365 дней с круглосуточным временем работы	365	Круглосуточно	30000
2	Абонемент для парковки на Балканской на 30 дней с круглосуточным временем работы	30	Круглосуточно	30000
\.


--
-- Data for Name: robokassa_successnotification; Type: TABLE DATA; Schema: public; Owner: paymentforparkinguser
--

COPY public.robokassa_successnotification (id, "InvId", "OutSum", created_at) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 195, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 48, true);


--
-- Name: index_paidparking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_paidparking_id_seq', 120, true);


--
-- Name: index_paidseasontickets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_paidseasontickets_id_seq', 31, true);


--
-- Name: index_paidtickets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_paidtickets_id_seq', 1, false);


--
-- Name: index_parking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_parking_id_seq', 5, true);


--
-- Name: index_parking_seasontickets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_parking_seasontickets_id_seq', 2, true);


--
-- Name: index_parking_tickets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_parking_tickets_id_seq', 6, true);


--
-- Name: index_seasontickets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_seasontickets_id_seq', 2, true);


--
-- Name: index_tickets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.index_tickets_id_seq', 4, true);


--
-- Name: robokassa_successnotification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: paymentforparkinguser
--

SELECT pg_catalog.setval('public.robokassa_successnotification_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: index_paidparking index_paidparking_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidparking
    ADD CONSTRAINT index_paidparking_pkey PRIMARY KEY (id);


--
-- Name: index_paidseasontickets index_paidseasontickets_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidseasontickets
    ADD CONSTRAINT index_paidseasontickets_pkey PRIMARY KEY (id);


--
-- Name: index_paidtickets index_paidtickets_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidtickets
    ADD CONSTRAINT index_paidtickets_pkey PRIMARY KEY (id);


--
-- Name: index_parking index_parking_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking
    ADD CONSTRAINT index_parking_pkey PRIMARY KEY (id);


--
-- Name: index_parking_seasontickets index_parking_seasontick_parking_id_seasontickets_34c3e6f4_uniq; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_seasontickets
    ADD CONSTRAINT index_parking_seasontick_parking_id_seasontickets_34c3e6f4_uniq UNIQUE (parking_id, seasontickets_id);


--
-- Name: index_parking_seasontickets index_parking_seasontickets_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_seasontickets
    ADD CONSTRAINT index_parking_seasontickets_pkey PRIMARY KEY (id);


--
-- Name: index_parking_tickets index_parking_tickets_parking_id_tickets_id_ed4a620d_uniq; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_tickets
    ADD CONSTRAINT index_parking_tickets_parking_id_tickets_id_ed4a620d_uniq UNIQUE (parking_id, tickets_id);


--
-- Name: index_parking_tickets index_parking_tickets_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_tickets
    ADD CONSTRAINT index_parking_tickets_pkey PRIMARY KEY (id);


--
-- Name: index_seasontickets index_seasontickets_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_seasontickets
    ADD CONSTRAINT index_seasontickets_pkey PRIMARY KEY (id);


--
-- Name: index_tickets index_tickets_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_tickets
    ADD CONSTRAINT index_tickets_pkey PRIMARY KEY (id);


--
-- Name: robokassa_successnotification robokassa_successnotification_pkey; Type: CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.robokassa_successnotification
    ADD CONSTRAINT robokassa_successnotification_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: index_paidparking_adress_id_b4c5c81a; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_paidparking_adress_id_b4c5c81a ON public.index_paidparking USING btree (adress_id);


--
-- Name: index_paidseasontickets_nametickets_id_64f9c243; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_paidseasontickets_nametickets_id_64f9c243 ON public.index_paidseasontickets USING btree (nametickets_id);


--
-- Name: index_paidtickets_name_id_5e2a201f; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_paidtickets_name_id_5e2a201f ON public.index_paidtickets USING btree (name_id);


--
-- Name: index_parking_seasontickets_parking_id_ca13dfb7; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_parking_seasontickets_parking_id_ca13dfb7 ON public.index_parking_seasontickets USING btree (parking_id);


--
-- Name: index_parking_seasontickets_seasontickets_id_f1731dd5; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_parking_seasontickets_seasontickets_id_f1731dd5 ON public.index_parking_seasontickets USING btree (seasontickets_id);


--
-- Name: index_parking_tickets_parking_id_844b870d; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_parking_tickets_parking_id_844b870d ON public.index_parking_tickets USING btree (parking_id);


--
-- Name: index_parking_tickets_tickets_id_012b350d; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_parking_tickets_tickets_id_012b350d ON public.index_parking_tickets USING btree (tickets_id);


--
-- Name: index_tickets_nameseasontickets_97a500da; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_tickets_nameseasontickets_97a500da ON public.index_tickets USING btree (nameseasontickets);


--
-- Name: index_tickets_nameseasontickets_97a500da_like; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX index_tickets_nameseasontickets_97a500da_like ON public.index_tickets USING btree (nameseasontickets varchar_pattern_ops);


--
-- Name: robokassa_successnotification_InvId_2adb5e8f; Type: INDEX; Schema: public; Owner: paymentforparkinguser
--

CREATE INDEX "robokassa_successnotification_InvId_2adb5e8f" ON public.robokassa_successnotification USING btree ("InvId");


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: index_paidparking index_paidparking_adress_id_b4c5c81a_fk_index_parking_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidparking
    ADD CONSTRAINT index_paidparking_adress_id_b4c5c81a_fk_index_parking_id FOREIGN KEY (adress_id) REFERENCES public.index_parking(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: index_paidseasontickets index_paidseasontick_nametickets_id_64f9c243_fk_index_tic; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidseasontickets
    ADD CONSTRAINT index_paidseasontick_nametickets_id_64f9c243_fk_index_tic FOREIGN KEY (nametickets_id) REFERENCES public.index_tickets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: index_paidtickets index_paidtickets_name_id_5e2a201f_fk_index_tickets_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_paidtickets
    ADD CONSTRAINT index_paidtickets_name_id_5e2a201f_fk_index_tickets_id FOREIGN KEY (name_id) REFERENCES public.index_tickets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: index_parking_seasontickets index_parking_season_parking_id_ca13dfb7_fk_index_par; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_seasontickets
    ADD CONSTRAINT index_parking_season_parking_id_ca13dfb7_fk_index_par FOREIGN KEY (parking_id) REFERENCES public.index_parking(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: index_parking_seasontickets index_parking_season_seasontickets_id_f1731dd5_fk_index_sea; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_seasontickets
    ADD CONSTRAINT index_parking_season_seasontickets_id_f1731dd5_fk_index_sea FOREIGN KEY (seasontickets_id) REFERENCES public.index_seasontickets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: index_parking_tickets index_parking_tickets_parking_id_844b870d_fk_index_parking_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_tickets
    ADD CONSTRAINT index_parking_tickets_parking_id_844b870d_fk_index_parking_id FOREIGN KEY (parking_id) REFERENCES public.index_parking(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: index_parking_tickets index_parking_tickets_tickets_id_012b350d_fk_index_tickets_id; Type: FK CONSTRAINT; Schema: public; Owner: paymentforparkinguser
--

ALTER TABLE ONLY public.index_parking_tickets
    ADD CONSTRAINT index_parking_tickets_tickets_id_012b350d_fk_index_tickets_id FOREIGN KEY (tickets_id) REFERENCES public.index_tickets(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

