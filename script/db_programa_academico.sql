PGDMP     	        
            {            bd_programa_academico    15.3    15.3 
    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16398    bd_programa_academico    DATABASE     �   CREATE DATABASE bd_programa_academico WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Ecuador.1252';
 %   DROP DATABASE bd_programa_academico;
                postgres    false            �            1259    16415    tb_estudiante    TABLE     �   CREATE TABLE public.tb_estudiante (
    id integer NOT NULL,
    nombre character varying(25),
    apellido character varying(25),
    edad integer
);
 !   DROP TABLE public.tb_estudiante;
       public         heap    postgres    false            �            1259    16414    tb_estudiante_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_estudiante_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.tb_estudiante_id_seq;
       public          postgres    false    215            �           0    0    tb_estudiante_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.tb_estudiante_id_seq OWNED BY public.tb_estudiante.id;
          public          postgres    false    214            e           2604    16418    tb_estudiante id    DEFAULT     t   ALTER TABLE ONLY public.tb_estudiante ALTER COLUMN id SET DEFAULT nextval('public.tb_estudiante_id_seq'::regclass);
 ?   ALTER TABLE public.tb_estudiante ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �          0    16415    tb_estudiante 
   TABLE DATA                 public          postgres    false    215   �	       �           0    0    tb_estudiante_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.tb_estudiante_id_seq', 10, true);
          public          postgres    false    214            �   �   x��ϱ�0�ᝧ��4�DL�b"�j.��MjKJ�����lg������s��0�Q�t��G->HB�$��b��Қ�e�$����%z(8�\HZ����Q��%N^��݅�c��o�1�LG}�M�6�G�%஌�k"�~�)���>\\XS��~���$y�     