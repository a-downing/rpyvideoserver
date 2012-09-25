var RPCVideoServer = 
{
    bigSeekBackward: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "bigSeekBackward", args: []});
    },

    bigSeekForward: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "bigSeekForward", args: []});
    },

    pause: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "pause", args: []});
    },

    smallSeekBackward: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "smallSeekBackward", args: []});
    },

    smallSeekForward: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "smallSeekForward", args: []});
    },

    volumeUp: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "volumeUp", args: []});
    },

    volumeDown: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "volumeDown", args: []});
    },

    startVideo: function(filename)
    {
        return rpc_call({"class": "RPCVideoServer", method: "startVideo", args: [filename]});
    },

    stopVideo: function()
    {
        return rpc_call({"class": "RPCVideoServer", method: "stopVideo", args: []});
    },

    videoSearch: function(search_string)
    {
        return rpc_call({"class": "RPCVideoServer", method: "videoSearch", args: [search_string]});
    }
};

var RPCGeneral = 
{
    login: function(password)
    {
        return rpc_call({"class": "RPCGeneral", method: "login", args: [password]});
    },

    logout: function()
    {
        return rpc_call({"class": "RPCGeneral", method: "logout", args: []});
    },

    status: function()
    {
        return rpc_call({"class": "RPCGeneral", method: "status", args: []});
    }
};