import fnmatch
import os
import subprocess
import binascii

import cherrypy

import rpc_utils
from server_config import config

class RPCVideoServer:
    def __init__(self):
        self.videoplayer_proc = None

    @rpc_utils.rpc_enable()
    def videoSearch(self, search_string, **kwargs):

        pattern = search_string
        result = []

        for rootPath in config['video_dirs']:
            for root, dirs, files in os.walk(rootPath):
                for filename in files:
                    if fnmatch.fnmatch(filename.lower(), pattern.lower()):
                        fullpath = os.path.join(root, filename)
                        if fullpath.endswith(config['video_extensions']) == True:
                            result.append(fullpath)

        return rpc_utils.rpc_return(True, result)


    @rpc_utils.rpc_enable()
    def startVideo(self, filename, **kwargs):
        cmd = list(config['video_player_cmd'])
        cmd.append(filename)
        self.videoplayer_proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def stopVideo(self, **kwargs):
        self.videoplayer_proc.terminate()
        self.videoplayer_proc.wait()
        self.videoplayer_proc = None
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def pause(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['pause'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def smallSeekForward(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['small_seek_forward'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def smallSeekBackward(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['small_seek_backward'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def bigSeekForward(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['big_seek_forward'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def bigSeekBackward(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['big_seek_backward'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def volumeUp(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['vol+'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def volumeDown(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['vol-'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def toggleSubtitles(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['subtitles'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def nextSubtitles(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['subtitles_next'])
        return rpc_utils.rpc_return(True, None)

    @rpc_utils.rpc_enable()
    def prevSubtitles(self, **kwargs):
        self.videoplayer_proc.stdin.write(config['subtitles_prev'])
        return rpc_utils.rpc_return(True, None)
        