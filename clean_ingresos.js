use candidatos2014;
db.ingresos.aggregate([
  {
    $project: {
        candidato_id:'$candidato_id',
        remuneracionPublico: '$d.floRemuneracionPublico',
        remuneracionPrivado: '$d.floRemuneracionPrivado',
        rentaPublico: '$d.floRentaPublico',
        rentaPrivado: '$d.floRentaPrivado',
        otrosPublico: '$d.floOtrosPublico',
        otrosPrivado: '$d.floOtrosPrivado'
    }
  },
  {
    $out : 'clean_ingresos'
  }
]);
