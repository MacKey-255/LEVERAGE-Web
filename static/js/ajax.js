/* Ajax Functions */
var cmd = {
    //Data AJAX
    url: null,
    request: null,
    type: 'get',
    dataType: 'json',
    online: true,

    //Data Response
    action: null,
    error: function (e) {
        console.log(e)
    },
    //Ping al Servidor
    ping: function() {
        $.ajax({
            url: URL,
            context: document.body,
            error: function(jqXHR, exception) {
                console.log("Error! Conexion Perdida!")
                stop = false
            },
            success: function() {
            }
        })
    },
    //Funciones Basicas
    send: function(url, request, type) {
        this.url = url;
        this.type = (type==undefined)?'get':type;
        this.request = request;
        return this.ajax()
    },
    ajax: function() {
        self = this;
        $.ajax({
            url: this.url,
            data: this.request,
            type: this.type,
            dataType: this.dataType,
            success: function(s) {
                //Respuesta
                self.action(s)
            },
            error : function (e) {
                //Respuesta con Error
                self.error(e);
                self.ping()
            },
        })
    }
}