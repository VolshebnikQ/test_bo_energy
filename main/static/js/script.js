
$(document).ready(function() {
    if ($('#solve_equation').length == 1) {
        $('#solve_equation')[0].onclick = function () {
            sendAjaxTask1();
        }
    }
    if ($('#suggest_color').length == 1) {
        $('#suggest_color')[0].onclick = function () {
            sendAjaxTask2();
        }
    }
});

function showAnswer(bool) {
    if (bool)
        $('.answer-card')[0].style.display = "block";
    else
        $('.answer-card')[0].style.display = "none";
}   

function sendAjaxTask1() {
    var data = {
        equation: $("#equation")[0].value,
    };
    token = $('#token input')[0].value,

    $.ajax({
        type: "POST",
        url: "/task_1/",
        contentType: "application/json; charset=utf-8",
        headers: { 
            "X-CSRFToken": token,
            "X-Requested-With": "XMLHttpRequest"
        },
        data: JSON.stringify(data)
    }).always(function (result) {
        console.log(result);
        showAnswer(true);
        $('#answer')[0].innerHTML = result.x
    });
}

function sendAjaxTask2() {
    var data = {
        suggest: $("#suggest")[0].value,
    };
    token = $('#token input')[0].value,

    $.ajax({
        type: "POST",
        url: "/task_2/",
        contentType: "application/json; charset=utf-8",
        headers: { 
            "X-CSRFToken": token,
            "X-Requested-With": "XMLHttpRequest"
        },
        data: JSON.stringify(data)
    }).always(function (result) {
        console.log(result);
        showAnswer(true);
        $('#answer')[0].innerHTML = result.answer
    });
}