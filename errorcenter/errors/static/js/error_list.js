function list() 
{
    var request = new XMLHttpRequest()
    request.open('GET', 'http://127.0.0.1:8000/api/errors/', true)
    request.onload = function() {
        var data = JSON.parse(this.response)
        if (request.status >= 200 && request.status < 400) {
            // Limpa div
            $('.myErrors').empty();
            // Exibe erros
            data.forEach(error => {
                linha = '<tr>'
                +'  <td class="text-center">'
                +'      <input type="checkbox" id="erro">'
                +'  </td>'
                +'  <td class="text-center">'+error.level+'</td>'
                +'  <td class="text-center">'+error.title+'<br>'+error.address+'<br>'+error.created_at+'</td>'
                +'  <td class="text-center">'+error.events+'</td>'
                +'</tr>';
                $('.myErrors').append(linha);
            })
        } else {
            console.log('Erro '+request.status+': recurso não encontrado.')
        }
    }
    request.send()
}

list()