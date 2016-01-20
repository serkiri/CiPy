$(document).ready(function() {
    refresh();
    setInterval(function(){
        refresh();
    }, 5000);
});

function refresh(){
        $.ajax({
            url: "getdata",
            cache: false
        }).done(onGetDataDone).fail(onGetDataFail);
}

function onGetDataDone(data){
    $("#content").html('');
    responce = $.parseJSON(data);
    if($('.cipyVersion').text() != responce['cipyVersion']){
        location.reload();
    }
    jobs = responce['jobs']
    $.each(jobs, function(index, job){
        build = $('<div class="build"><div class="progress"><span>.</span></div><div class="buildContent">' + '<a href="' + job['url'] + '">' + job['name'] + ' ' + job['number'] + '</a></div></div>');
        build.addClass(job['result']);
        build.find("a").addClass(job['result']);
        build.find(".progress").addClass(job['result']);
        $("#content").append(build);
        if (job['progress']){
            build.find(".progress").width(build.width() * job['progress'] / 100);
        } else {
            build.find(".progress span").remove();
        }
        
        if(job['subBuilds']){
            subBuilds = $('<div class="subBuilds"></div>');
            $.each(job['subBuilds'], function(index2, subJob){
                subBuild = $('<a class="subBuild" href="' + subJob['url'] + '">' + subJob['name'] + ' ' + subJob['number'] +'</a>');
                subBuild.addClass(subJob['result'])
                subBuilds.append(subBuild);
            });
            build.find('.buildContent').append(subBuilds);
        }
    });
}

function onGetDataFail(data){
    $("#content").html("ERROR ");
}