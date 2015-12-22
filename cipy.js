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
    jobs = $.parseJSON(data);
//    $("#content").html(data);
    $.each(jobs, function(index, job){
        build = $('<p>' + '<a href="' + job['url'] + '">' + job['name'] + ' ' + job['number'] + ' ' + (job['progress'] ? job['progress'] : '') + '</a></p>');
        build.addClass(job['result']).addClass('build');
        build.find("a").addClass(job['result']);
        $("#content").append(build);
        
        if(job['subBuilds']){
            subBuilds = $('<ul class="subBuilds"></ul>');
            $.each(job['subBuilds'], function(index2, subJob){
                subBuild = $('<li><a href="' + subJob['url'] + '">' + subJob['name'] + ' ' + subJob['number'] +'</a></li>');
                subBuild.addClass(subJob['result']).addClass('subBuild');
                subBuild.find("a").addClass(subJob['result']);
                subBuilds.append(subBuild);
            });
            build.append(subBuilds);
        }
    });
}

function onGetDataFail(data){
    $("#content").html("ERROR ");
}