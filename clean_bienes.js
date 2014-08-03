use candidatos2014;
db.bienes.aggregate([
  {
    $unwind: '$d'
  },
  {
    $group: {
      _id: '$candidato_id',
      num_bienes_inmueble: {
        $sum: {
            $cond: [
              { $eq: [ '$d.intId_Bien' , 1 ]},
              1,
              0
            ]
        }
      },
      valor_bienes_inmueble : {
        $sum: { 
            $cond: [
              { $eq: [ '$d.intId_Bien' , 1 ]},
              '$d.floValor_Bien',
              0
            ]
        }
      },
      num_bienes_mueble: {
        $sum: {
            $cond: [
              { $eq: [ '$d.intId_Bien' , 3 ]},
              1,
              0
            ]
        }
      },
      valor_bienes_mueble: {
        $sum: { 
            $cond: [
              { $eq: [ '$d.intId_Bien' , 3 ] },
              '$d.floValor_Bien',
              0
            ]
        }
      }
    }
  },
  {
    $project: {
        _id:0,
        candidato_id: '$_id',
        num_bienes_inmueble: 1,
        valor_bienes_inmueble: 1,
        num_bienes_mueble: 1,
        valor_bienes_mueble: 1
    }
  },
  {
    $limit : 10
  }
]);
