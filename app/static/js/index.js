
let urlArea = $('#url_area');
let shortButton = $('#short_button');
let copyButton = $('#copy_button');
let shortUrl = $('#short_url');
let resultPanel = $('#result_panel');
let blockedValues = ['',]; // Значения поля
let clickButton = false; // Флаг, показывающий, надо ли анимировать заново выдвижение панели
let speedTogglePanel = 300; // Скорость появления/исчезания панели с коротким URL
let speedAnimateText = 20; // Скорость появления/исчезания текста на панели

// Нужно задвинуть панель, потому что при рендере страницы она почему-то выдвинута
resultPanel.slideToggle(0);
shortButton.toggleClass("active");

// Вставляем в место для ссылки ссылку на API
$('ul').html('<li class="link"><a href="/api">API</a></li>' + $('ul').html());

// Цвета
let mainColor = "rgb(237, 237, 237)";
let outlineColor = "rgb(203, 203, 203)";
let pushedButtonColor = 'rgb(203, 203, 203)';
let buttonColor = "rgb(255, 255, 255)";


function getShortUrl() {
    let url = urlArea.prop('value').trim();
    if (!blockedValues.includes(url)) {
        let data = JSON.stringify({ "url": url });
        $.ajax({
            url: "/",
            type: "POST",
            contentType: 'application/json',
            data: data,
            success: function (result) {
                // Если кнопка не нажималась, то выдвигаем панельку
                if (!clickButton) {
                    resultPanel.slideToggle(speedTogglePanel);
                    shortButton.toggleClass("active");
                    clickButton = true;
                }
                // Анимация появления текста
                shortUrl.animate({
                    opacity: 1
                }, speedAnimateText);
                // Вставка ссылки
                $('#href').html(result);
                $('#href').attr('href', `http://${result}`);
            },
            error: function () { return 'error' },
        });
    } else {
        // Если кнопка уже нажималась и в поле полного URL ничего нету, то
        if (clickButton) {
            // скрываем текст
            shortUrl.animate({
                opacity: 0
            }, speedAnimateText);
            // скрываем панельку
            resultPanel.slideToggle(speedTogglePanel);
            shortButton.toggleClass("active");
            clickButton = false;
        }
    }
}

// Костыльная функция для копирования. Суть: создаётся новый элемент input, в который вставляется значение для копирования,
// созданный элемент выбирается (".select()") и происходит копирование
function copyUrl() {
    let tag = document.createElement("input");
    tag.id = 'temporary';
    tag.value = $('#href').html();
    $('html').append(tag);
    $('#temporary').select();
    document.execCommand("copy");
    $('html #temporary').remove();

}


shortButton.click(getShortUrl); // вешаем функцию получения короткой ссылки на клик кнопки
copyButton.click(copyUrl);


// Красивая анимация кликов для кнопки сокращения ссылки
shortButton.mouseup(function () {
    shortButton.css({
        "background-color": buttonColor,
    });
})
shortButton.mousedown(function () {
    shortButton.css({
        "background-color": pushedButtonColor,
    });
})

// То же самое, что и сверху, но для кнопки вставки ссылки
copyButton.mouseup(function () {
    copyButton.css({
        "background-color": buttonColor,
    });
})
copyButton.mousedown(function () {
    copyButton.css({
        "background-color": pushedButtonColor,
    });
})



$('html').keyup(function (event) {
    // при нажатии кнопки Enter в области тега html (везде) будет вызываться клик на кнопку
    if (event.keyCode === 13) {
        shortButton.click();
    }

    // При нажатии escape фокус на поле должен теряться
    else if (event.keyCode === 27 && urlArea.is(':focus')) {
        urlArea.blur();
    }
});

// при нажатии кнопки backspace переносим фокус на поле ввода
$('html').keydown(function (event) {
    if (event.keyCode === 8 && !urlArea.is(':focus')) {
        urlArea.focus();
    }
});


// Реакция на нажатие различных кнопок (результат нажатия которых печатается), чтобы при вводе чего либо это было в поле для URL
$('html').keypress(function (event) {
    if (!urlArea.is(':focus')) {
        urlArea.focus();
    }
});