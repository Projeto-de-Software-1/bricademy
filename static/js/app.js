//Faz funcionar o click do navbar no mobile
$(document).ready(function() {
  $(".sidenav").sidenav();
});

//Faz funcionar o botão com menu na pagina home
$(document).ready(function() {
  $(".fixed-action-btn").floatingActionButton();
});

//faz fucionar a side bar
$(document).ready(function() {
  $(".sidenav").sidenav();
});

//faz funcionar os selects fields
$(document).ready(function() {
  $("select").formSelect();
});

//faz funcionar o dropdown
$(".dropdown-trigger").dropdown({ constrainWidth: false });

//faz funcionar os tooltips 'dicas'
$(document).ready(function() {
  $(".tooltipped").tooltip();
});
