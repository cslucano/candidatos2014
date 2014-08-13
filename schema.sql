CREATE TABLE candidatos 
(
    candidato_id text,
    residencia_ubigeo_pro text,
    nombres text,
    nac_pais text,
    nac_ubigeo_dep text,
    forma_designacio text,
    residencia_tiempo text,
    dni text,
    ubigeo_postula_dep text,
    residencia text,
    ubigeo_postula_pro text,
    email text,
    cargo_autoridad text,
    appaterno text,
    sexo text,
    residencia_ubigoe_dis text,
    residencia_ubigeo_dep text,
    org_pol text,
    apmaterno text,
    nac_ubigeo_pro text,
    fdn text,
    nac_ubigeo_dis text,
    ubigeo_portula_dis text
);

CREATE TABLE ingresos
(
    rentaPrivado text,
    remuneracionPrivado text,
    candidato_id text,
    remuneracionPublico text,
    otrosPrivado text,
    otrosPublico text,
    rentaPublico text
);

CREATE TABLE bienes
(
    valor_bienes_inmueble text,
    num_bienes_mueble text,
    candidato_id text,
    num_bienes_inmueble text,
    valor_bienes_mueble text
);

