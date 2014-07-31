var casper = require('casper').create();
var utils = require('./utilitarios.js');

var form = '#wf_BuscarListaCandidato_HV';
var selTipoEleccion = '#ddlTipoEleccion';
var selDepartamento = '#ddlDepartamento';
var selProvincia = '#ddlProvincia';
var selDistrito = '#ddlDistrito';
var submitFunction = 'p_Busca();';

casper.start('http://200.48.102.68/sipesg_erm2014/wf_BuscarListaCandidato_HV.aspx', function () {
    this.echo('scrapping lista de candidatos 2014');
    this.echo('título - ' + this.getTitle());
    var tiposEleccion = this.evaluate(utils.getTiposEleccion);
    for (var i=0; i< tiposEleccion.length; i++) {
      tipoEleccion = tiposEleccion[i];
      this.echo('Tipo de Elección ' + tipoEleccion['content']);

      if(tipoEleccion['content'].indexOf('PROV') >= 0) {
        this.fill('form#wf_BuscarListaCandidato_HV', {
          ddlTipoEleccion : tipoEleccion['value']
        }, false);

        this.waitFor(
          function check() {
            return this.evaluate(function() {
              return document.querySelectorAll('#ddlDepartamento option').length > 2;
            });
          }, 
          function then() {
            var dpts = this.evaluate(utils.getDepartamentos);
            for (var j=0; j< dpts.length; j++) {
              departamento = dpts[j];

                if(departamento['value'] >= 0) {
                  this.echo('  Departamento ' + departamento['content']);
                  this.fill('form#wf_BuscarListaCandidato_HV', {
                    ddlDepartamento : departamento['value']
                  }, false);
 
                  this.waitFor(
                    function check() {
                      return this.evaluate(function() {
                        return document.querySelectorAll('#ddlProvincia option').length > 2;
                      });
                    },
                    function then() {
                      var prvs = this.evaluate(utils.getProvincias);
                      for (var k=0; k< prvs.length; k++) {
                        this.echo('    ' + prvs[k]['value'] + ' ' + prvs[k]['content']);
                      }
                    }
                  );
                }

            }
          }
        );
      }
    }
});


casper.run();
