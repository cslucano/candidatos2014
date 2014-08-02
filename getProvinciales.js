var casper = require('casper').create(
  {
    verbose: true,
    logLevel: "debug"
  }
);
var utils = require('./utilitarios.js');

var form = '#wf_BuscarListaCandidato_HV';
var selTipoEleccion = '#ddlTipoEleccion';
var selDepartamento = '#ddlDepartamento';
var selProvincia = '#ddlProvincia';
var selDistrito = '#ddlDistrito';
var submitFunction = 'p_Busca();';

casper.start('http://200.48.102.68/sipesg_erm2014/wf_BuscarListaCandidato_HV.aspx', function() {
    this.echo('scrapping lista de candidatos 2014');
    this.echo('título - ' + this.getTitle());
    var tiposEleccion = this.evaluate(utils.getTiposEleccion);

    this.each(tiposEleccion, function(self, tipoEleccion) {
        this.then(function() {
            self.echo('Tipo de Elección ' + tipoEleccion['content']);

            if(tipoEleccion['content'].indexOf('PROV') >= 0) {
                this.then(function() {
                    this.fill('form#wf_BuscarListaCandidato_HV', {
                      ddlTipoEleccion : tipoEleccion['value']
                    }, true);


                });

                var dpts = this.evaluate(utils.getDepartamentos);

                this.then(function() {
                    this.each(dpts, function(self, departamento) {
                        this.then(function() {
                            if(departamento['value'] > 0) {
                                this.then(function() {
                                    this.echo('  Departamento ' + departamento['content']);
                                    this.fill('form#wf_BuscarListaCandidato_HV', {
                                      ddlDepartamento : departamento['value']
                                    }, true);


                                });

                                var prvs = this.evaluate(utils.getProvincias);

                                this.then(function() {
                                    this.each(prvs, function(self, provincia) {
                                        this.then(function(){
                                        if(provincia['value'] > 0) {
                                            this.then(function() {
                                                this.echo('    ' + provincia['value'] + ' ' + provincia['content']);
                                                this.fill('form#wf_BuscarListaCandidato_HV', {
                                                  ddlProvincia : provincia['value']
                                                }, true);
                                            });


                                            this.then(function() {
                                                this.click('#wf_BuscarListaCandidato_HV input[type=button]');
                                            });

                                            this.then(function() {
                                                var op = this.evaluate(function() {
                                                    var op_json = 'xxx';
                                                    var op_row = $('.tabla_main>tbody>tr');

                                                    if (op_row.length>2) {
                                                        arrOp = [];
                                                        op_json = 'yyy';
                                                        for(var op_index = 2; op_index < op_row.length; op_index++) {
                                                            var e_op = op_row[op_index];
                                                            var arrCd = [];

                                                            if (e_op.innerHTML.indexOf('body_tabla') == -1) {
                                                              var beOp = {
                                                                jee : $(e_op).find('td:nth(1)')[0].textContent.trim(),
                                                                expediente : $(e_op).find('td:nth(2)')[0].textContent.trim(),
                                                                solicitud : $(e_op).find('td:nth(3)')[0].textContent.trim(),
                                                                org_pol : $(e_op).find('td:nth(4)')[0].textContent.trim(),
                                                                estado : $(e_op).find('td:nth(5)')[0].textContent.trim(),
                                                              };

                                                              if(op_index<op_row.length-1)
                                                                {
                                                                  var cd_row = $(op_row[op_index+1]).find('.body_tabla tr');

                                                                  if(cd_row.length>1) {
                                                                    for(var cd_index = 1; cd_index < cd_row.length; cd_index++) {
                                                                      var e_cd = cd_row[cd_index];

                                                                      var beCd = {
                                                                          pos : $(e_cd).find('td:nth(1)')[0].textContent.trim(),
                                                                          cargo : $(e_cd).find('td:nth(2)')[0].textContent.trim(),
                                                                          dni : $(e_cd).find('td:nth(3)')[0].textContent.trim(),
                                                                        };

                                                                      arrCd.push(beCd);
                                                                    }

                                                                    beOp['candidatos'] = arrCd;
                                                                  }
                                                                }

                                                              arrOp.push(beOp);
                                                            }
                                                          }

                                                        op_json = JSON.stringify(arrOp);
                                                      }

                                                    return op_json;
                                              });

                                              this.echo(op);
                                            });
                                          }
                                        });
                                    }); //end each prov
                                });
                            }
                        });
                    }); //end each dpts
                });
            }
        });
    }); // End each TipoElección
});


casper.run();
