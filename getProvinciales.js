var casper = require('casper').create();
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

                this.fill('form#wf_BuscarListaCandidato_HV', {
                  ddlTipoEleccion : tipoEleccion['value']
                }, true);

                var dpts = this.evaluate(utils.getDepartamentos);

                this.each(dpts, function(self, departamento) {
                    this.then(function() { 
                        if(departamento['value'] >= 0) {
                            this.echo('  Departamento ' + departamento['content']);
                            this.fill('form#wf_BuscarListaCandidato_HV', {
                              ddlDepartamento : departamento['value']
                            }, true);
 
                            var prvs = this.evaluate(utils.getProvincias);

                            this.each(prvs, function(self, provincia) {
                                this.echo('    ' + provincia['value'] + ' ' + provincia['content']);
                            });
                        }
                    });
                }); //end each dpts

            }
        });
    }); // End each TipoElección
});


casper.run();
