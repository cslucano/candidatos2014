CREATE TABLE candidatos_stage 
(
    candidato_id integer,
    residencia_ubigeo_pro text,
    nombres text,
    nac_pais text,
    nac_ubigeo_dep text,
    postula_ubigeo text,
    forma_designacio text,
    residencia_tiempo text,
    dni text,
    residencia text,
    email text,
    cargo_autoridad text,
    appaterno text,
    postula_ubigeo_dis text,
    sexo integer,
    residencia_ubigeo_dep text,
    postula_ubigeo_pro text,
    org_pol text,
    apmaterno text,
    postula_ubigeo_dep text,
    nac_ubigeo_pro text,
    fdn text,
    residencia_ubigeo_dis text,
    nac_ubigeo_dis text,
    residencia_ubigeo text,
    nac_ubigeo text
);

CREATE TABLE ingresos_stage
(
    rentaPrivado text,
    remuneracionPrivado text,
    candidato_id text,
    remuneracionPublico text,
    otrosPrivado text,
    otrosPublico text,
    rentaPublico text
);

CREATE TABLE bienes_stage
(
    valor_bienes_inmueble text,
    num_bienes_mueble text,
    candidato_id text,
    num_bienes_inmueble text,
    valor_bienes_mueble text
);

CREATE TABLE bien_stage
(
   candidatojneid integer,
   idbien integer,
   nombre text,
   descripcion text,
   caracteristicas text,
   valor double precision
)
