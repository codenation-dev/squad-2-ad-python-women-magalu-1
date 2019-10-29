window.onload = function() {

    /**
     * Realiza a requisicao para o endpoint de listar erros.
     */
    var request = new XMLHttpRequest()
    request.open('GET', 'http://127.0.0.1:8000/api/errors', true)
    request.onload = function() {
        var data = JSON.parse(this.response)
        if (request.status >= 200 && request.status < 400) {
            // Limpa div
            $('.myErrors').empty();
            // Exibe erros
            data.forEach(error => {
                // Formata a data
                date = formatDateTime(error.created_at)

                linha = '<tr>'
                +'  <td class="text-center">'
                +'      <input type="checkbox" id="erro" value="'+error.id+'">'
                +'  </td>'
                +'  <td class="text-center">'+error.level+'</td>'
                +'  <td class="text-center">'+error.title+'<br>'+error.address+'<br>'+date+'</td>'
                +'  <td class="text-center">'+error.events+'</td>'
                +'  <td class="text-center"><button class="form-control btn btn-info btn-xs">Ver</button></td>'
                +'</tr>';

                $('.myErrors').append(linha);
            })
        } else {
            $('.myErrors').empty();
            $('.myErrors').append('<p>Erro '+request.status+': nenhum recurso não encontrado.');
        }
    }
    request.send()

    /**
     * Ao clicar redireciona para página de detalhes do erro.
     */
    // $(document).on("click", "#list-errors tbody tr", function() {
    //     window.location = '/detail';
    // });  
}

/**
 * Formata data do banco de dados para formato compreensivel.
 * @param {*} date 
 */
function formatDateTime(date)
{
    let dateF = '';
    dateF = new Date(date);
    dateError = ("0" + dateF.getDate()).substr(-2) + "/" + ("0" + (dateF.getMonth() + 1)).substr(-2) + "/" + dateF.getFullYear();
    timeError = dateF.getHours() + ":" + dateF.getMinutes() + ":" + dateF.getSeconds();
    return dateError + ' ' + timeError;
}