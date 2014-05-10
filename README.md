torrent-preprocessor-3000
=========================

A small script/program to ensure torrents from a server are transfered/copied to another server with nfs/smb shares with network fault tolerance.

## Usage

Copy the python file on your server and make it excutable with `chmod o+x /path/to/myfile.py`.


### Deluge webui

To use with deluge, use the [execute extension](http://dev.deluge-torrent.org/wiki/Plugins/Execute) and call the script with full path.

No need to supply arguments (the plugin takes care of it).

### qBittorrent-nox

To use with qBittorrent-nox, enter the following command to execute in the download tab `/home/myuser/qBittorrent.py %n %f`.

**Warning** the previous command might not handle whitespaces correctly. Using `/home/myuser/qBittorrent.py "%n" "%f"` would normally work, but it [does not](https://github.com/qbittorrent/qBittorrent/issues/1395).
