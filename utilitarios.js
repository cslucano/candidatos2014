var form = '#wf_BuscarListaCandidato_HV';
var selTipoEleccion = '#ddlTipoEleccion';
var selDepartamento = '#ddlDepartamento';
var selProvincia = '#ddlProvincia';
var selDistrito = '#ddlDistrito';
var submitFunction = 'p_Busca();';

exports.getTiposEleccion = function() {
  options = document.querySelectorAll('#ddlTipoEleccion option');

  return Array.prototype.map.call(options, function(e) {
    return {value: e.getAttribute('value'), content: e.innerHTML};
  });
};

exports.getDepartamentos = function() {
  options = document.querySelectorAll('#ddlDepartamento option');

  return Array.prototype.map.call(options, function(e) {
    return {value: e.getAttribute('value'), content: e.innerHTML};
  });
};

exports.getProvincias = function() {
  options = document.querySelectorAll('#ddlProvincia option');

  return Array.prototype.map.call(options, function(e) {
    return {value: e.getAttribute('value'), content: e.innerHTML};
  });
};

exports.getDistritos = function() {
  options = document.querySelectorAll('#ddlDistrito option');

  return Array.prototype.map.call(options, function(e) {
    return {value: e.getAttribute('value'), content: e.innerHTML};
  });
};

