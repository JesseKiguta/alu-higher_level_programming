#!/usr/bin/node
$('document').ready(function () {
    let languageCode = $('#language_code');
    let btn = $('#btn_translate');
    let translation = $('DIV#hello');
    let url = 'https://www.fourtonfish.com/hellosalut/?';

    btn.click(function () {
        $.get(url + $.param({ lang: languageCode.val() }), function (data) {
            translation.html(data.hello);
        });
    });
});
