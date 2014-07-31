casper = require('casper').create();

var form = '#wf_BuscarListaCandidato_HV';
var selTipoEleccion = '#ddlTipoEleccion';
var selDepartamento = '#ddlDepartamento';
var selProvincia = '#ddlProvincia';
var selDistrito = '#ddlDistrito';
var submitFunction = 'p_Busca();';

function getTiposEleccion() {
  options = document.querySelectorAll('#ddlTipoEleccion option');

  return Array.prototype.map.call(options, function(e) {
    return {value: e.getAttribute('value'), content: e.innerHTML};
  });
};

casper.start('http://200.48.102.68/sipesg_erm2014/wf_BuscarListaCandidato_HV.aspx', function () {
    this.echo('scrapping lista de candidatos 2014');
    this.echo('título - ' + this.getTitle());
    
    var depOptions = this.evaluate(getTiposEleccion);

    for (var i=0; i< depOptions.length; i++) {
      this.echo(depOptions[i]['value'] + ' ' + depOptions[i]['content']);
    }
});


casper.run();
