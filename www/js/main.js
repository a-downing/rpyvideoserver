$(document).ready(function()
{
    if(RPCGeneral.status().data == false)
    {
        do
        {
            var password = prompt("Enter Password");
            ret = RPCGeneral.login(password);
        } while(ret.data == false);
    }

    $("body").attr("style", "display: normal");

    $("#search_button").click(function()
    {
        var search_text = $("#search_text").val();
        $("#video_list").html("");

        var ret = RPCVideoServer.videoSearch(search_text);
        for(movie in ret.data)
        {
            var fullpath = ret.data[movie]
            var filename = filenameFromPath(fullpath);

            var li = $("<li></li>");

            var a = $("<a></a>");
            a.html(filename);
            a.attr("href", "javascript:void(0)");
            a.attr("data-filename", fullpath);
            a.attr("style", "white-space: normal");

            li.append(a);

            $("#video_list").append(li);
        }

        $("#video_list").listview("refresh");
    });

    $(document).on("click", "#video_list li a", function(e)
    {
        var target = $(e.target);
        var filename = target.attr("data-filename");
        RPCVideoServer.startVideo(filename);
        $.mobile.changePage("#video_player");
    });

    $(document).on("click", "#stop_button", function()
    {
        RPCVideoServer.stopVideo();
        $.mobile.changePage("#video_search");
    });

    $(document).on("click", "#pause_button", function()
    {
        RPCVideoServer.pause();
    });

    $(document).on("click", "#forward_button", function()
    {
        RPCVideoServer.smallSeekForward();
    });

    $(document).on("click", "#backward_button", function()
    {
        RPCVideoServer.smallSeekBackward();
    });

    $(document).on("click", "#volume_up_button", function()
    {
        RPCVideoServer.volumeUp();
    });

    $(document).on("click", "#volume_down_button", function()
    {
        RPCVideoServer.volumeDown();
    });

    $(document).on("click", "#toggle_subtitles_button", function()
    {
        RPCVideoServer.volumeDown();
    });

    $(document).on("click", "#next_subtitles_button", function()
    {
        RPCVideoServer.nextSubtitles();
    });

    $(document).on("click", "#prev_subtitles_button", function()
    {
        RPCVideoServer.prevSubtitles();
    });
});
