var session = new SessionStorage();
session.createItem("session_id", "");

function rpc_call(arg)
{
    var rqst_json = JSON.stringify({session: session.getItem('session_id'), call: arg});
    var ret = null;

    $.ajax({url: "http://" + document.location.host + "/rpc", type: "post", data: {request: rqst_json}, async: false, success: function(data)
    {
        ret = data;
        //alert(ret);
    }});

    if(ret.session != undefined)
    {
        session.setItem('session_id', ret.session)
    }

    //ret = jQuery.parseJSON(ret);
    if(ret.rpc_status == false)
    {
        alert("RPC Error:\n" + ret.rpc_fail_msg)
    }
    else
    {
        return ret.return_value;
    }
}

function filenameFromPath(path)
{
    var idx = path.lastIndexOf('/');
    return path.substring(idx + 1);
}

