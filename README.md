# watchdir

Watches directories for changes and runs a shell command when
something does change.

Very simple, uses pyinotify to detect changes to the directory.

Only actually acts on the `IN_CLOSE_WRITE` inotify event, that is,
when a file is closed after writing. The use case for me is that I'm
editing a file, and I want to automatically run some command whenever
the file changes. I don't want it to run the command while the file is
being edited though, only when I've actually finished writing my
changes to it. Just listening to this event seems to work perfectly
fine.

    usage: watchdir [-h] [-c CMD] [-v] dirs [dirs ...]
    
    Execute commands when files in a directory changes
    
    positional arguments:
      dirs               directories to watch
    
    optional arguments:
      -h, --help         show this help message and exit
      -c CMD, --cmd CMD  command to execute when files change. Use $1 to pass file
                         as argument. (default: echo $1)
      -v, --verbose      Verbose output (default: False)
