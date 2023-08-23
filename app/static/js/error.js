// Вставляем в место для ссылки ссылки
$('ul').html('<li class="link"><a href="/">Main</a></li>' + $('ul').html());
$('ul').html('<li class="link"><a href="/api">API</a></li>' + $('ul').html());