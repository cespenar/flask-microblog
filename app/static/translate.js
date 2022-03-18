function translate(sourceElem, destElem, sourceLang, destLang) {
    $(destElem).html('<img src="/static/loading.gif" alt="loading">');
    $.post('/translate', {
        text: $(sourceElem).text(),
        source_language: sourceLang,
        dest_language: destLang
    }).done(function (response) {
        $(destElem).text(response['text'])
    }).fail(function () {
        $(destElem).text("{{ _('Error: Could not contact server.') }}");
    });
}