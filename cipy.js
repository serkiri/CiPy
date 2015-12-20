$(document).ready(function() {
    setTimer(5000);
//        $.ajax({
//            url: "getdata",
//            cache: false
//        }).done(onGetDataDone).fail(onGetDataFail);
});

function setTimer(ms){
    setInterval(function(){
        $.ajax({
            url: "getdata",
            cache: false
        }).done(onGetDataDone).fail(onGetDataFail);
    }, ms);
}

function onGetDataDone(data){
    $("#content").html('');
    jobs = $.parseJSON(data);
    $.each(jobs, function(index, job){
        $('<p>' + job['name'] + ' ' + job['number'] + ' ' + job['result'] + '</p>')
        .addClass(job['result'])
        .appendTo("#content");
    });
}

function onGetDataFail(data){
    $("#content").append("ERROR ");
}