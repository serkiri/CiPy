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
        $("#content").append('<p style="color:' + job['result'] +' ">' + job['name'] + ' ' + job['number'] + ' ' + job['result'] + '</p>');
    });
}

function onGetDataFail(data){
    $("#content").append("ERROR ");
}