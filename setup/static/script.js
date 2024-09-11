$(document).ready(function () {
  $(".btn-add-tarefa").click(function (event) {
    event.preventDefault();

    var tarefa_auditoria = $(this).data("id"); // Obtém o ID do atributo data-id
    var tarefa_realizada = $(this).text(); // Obtém o texto do botão

    $.ajax({
      url: "add_tarefa",
      type: "POST",
      data: {
        tarefa_auditoria: tarefa_auditoria,
        tarefa_realizada: tarefa_realizada,
      },
      success: function (response) {
        if (response.success) {
          alert(response.mensagem);
        } else {
          alert(response.mensagem);
        }
      },
      error: function () {
        alert("Erro na requisição AJAX");
      },
    });
  });
});
