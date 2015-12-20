$(document).ready(function() {
    setInterval(function(){
        $.ajax({
            url: "getdata",
            cache: false
        }).done(onGetDataDone).fail(onGetDataFail);
    }, 5000);
});

function setTimer(ms){
}

function onGetDataDone(data){
    $("#content").html('');
    jobs = $.parseJSON(data);
//    $("#content").html(data);
    $.each(jobs, function(index, job){
        build = $('<p>' + job['name'] + ' ' + job['number'] + ' ' + job['result'] + '</p>');
        build.addClass(job['result']).addClass('build');
        $("#content").append(build);
        
        if(job['subBuilds']){
            subBuilds = $('<ul class="subBuilds"></ul>');
            $.each(job['subBuilds'], function(index2, subJob){
                subBuild = $('<li>' + subJob['name'] + ' ' + subJob['number'] + ' ' + subJob['result'] + ' ' +'</li>');
                subBuild.addClass(subJob['result']).addClass('subBuild');
                subBuilds.append(subBuild);
            });
            build.append(subBuilds);
        }
    });
}

function onGetDataFail(data){
    $("#content").html("ERROR ");
}