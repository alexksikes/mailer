function preview_recipients() {
    var sql_query = $('#sql_query')[0].value;
    $("#recipients_preview").load("/recipients?sql_query="+escape(sql_query));
}

function ajax_load(url) {
    $("#recipients_preview").load(url);
}

function send_mails() {
    $('#template button').replaceWith('<div class="sending">Sending ...</div>');
    var data = new Object();
    $('#sendmail_form input, #sendmail_form textarea, #recipients textarea').each(
        function() {
            /* on firefox javascript considers no value for a checkbox as a checked checkbox */
            if (this.type == 'checkbox') {
                data[this.name] = this.checked || '';
            } else {
                data[this.name] = this.value;
            }
        }
    );
    $('#sendmail_form').load('/send', data);
    return false;    
}