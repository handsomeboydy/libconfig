# svnserve
# Autogenerated from man page /usr/share/man/man8/svnserve.8.gz
complete -c svnserve -s d -l daemon --description 'Causes svnserve to run in daemon mode.'
complete -c svnserve -l listen-port --description 'Causes svnserve to listen on port when run in daemon mode.'
complete -c svnserve -l listen-host --description 'Causes svnserve to listen on the interface specified by host, which may be ei…'
complete -c svnserve -l foreground --description 'When used together with -d, this option causes svnserve to stay in the foregr…'
complete -c svnserve -s i -l inetd --description 'Causes svnserve to use the stdin/stdout file descriptors, as is appropriate f…'
complete -c svnserve -s h -l help --description 'Displays a usage summary and exits.'
complete -c svnserve -l version --description 'Print svnserve\'s version and the repository filesystem back-end(s) a particul…'
complete -c svnserve -s r -l root --description 'Sets the virtual root for repositories served by svnserve.'
complete -c svnserve -s R -l read-only --description 'Force all write operations through this svnserve instance to be forbidden, ov…'
complete -c svnserve -s t -l tunnel --description 'Causes svnserve to run in tunnel mode, which is just like the inetd mode of o…'
complete -c svnserve -l tunnel-user --description 'When combined with --tunnel, overrides the pre-authenticated username with th…'
complete -c svnserve -s T -l threads --description 'When running in daemon mode, causes svnserve to spawn a thread instead of a p…'
complete -c svnserve -l config-file --description 'When specified, svnserve reads filename once at program startup and caches th…'
complete -c svnserve -l pid-file --description 'When specified, svnserve will write its process ID to filename.'
complete -c svnserve -s X -l listen-once --description 'Causes svnserve to accept one connection on the svn port, serve it, and exit.'

