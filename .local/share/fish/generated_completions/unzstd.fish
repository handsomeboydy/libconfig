# unzstd
# Autogenerated from man page /usr/share/man/man1/unzstd.1.gz
complete -c unzstd -s z -l compress --description 'Compress.'
complete -c unzstd -s d -l decompress -l uncompress --description 'Decompress.'
complete -c unzstd -s t -l test --description 'Test the integrity of compressed files.'
complete -c unzstd -o 'b#' --description 'Benchmark file(s) using compression level # .'
complete -c unzstd -l train --description 'Use FILEs as a training set to create a dictionary.'
complete -c unzstd -s l -l list --description 'Display information related to a zstd compressed file, such as size, ratio, a…'
complete -c unzstd -s '#' --description '# compression level [1-19] (default: 3) .'
complete -c unzstd -l fast --description 'switch to ultra-fast compression levels.'
complete -c unzstd -l ultra --description 'unlocks high compression levels 20+ (maximum 22), using a lot more memory.'
complete -c unzstd -l long --description 'enables long distance matching with # windowLog, if not # is not present it d…'
complete -c unzstd -o 'T#' -l threads --description 'Compress using # working threads (default: 1).'
complete -c unzstd -l single-thread --description 'Does not spawn a thread for compression, use a single thread for both I/O and…'
complete -c unzstd -l adapt --description 'zstd will dynamically adapt compression level to perceived I/O conditions.'
complete -c unzstd -l rsyncable --description 'zstd will periodically synchronize the compression state to make the compress…'
complete -c unzstd -s D --description 'use file as Dictionary to compress or decompress FILE(s) .'
complete -c unzstd -l no-dictID --description 'do not store dictionary ID within frame header (dictionary compression).'
complete -c unzstd -s o --description 'save result into file (only possible with a single INPUT-FILE) .'
complete -c unzstd -s f -l force --description 'overwrite output without prompting, and (de)compress symbolic links .'
complete -c unzstd -s c -l stdout --description 'force write to standard output, even if it is the console .'
complete -c unzstd -l sparse --description 'enable / disable sparse FS support, to make files with many zeroes smaller on…'
complete -c unzstd -l rm --description 'remove source file(s) after successful compression or decompression .'
complete -c unzstd -s k -l keep --description 'keep source file(s) after successful compression or decompression.'
complete -c unzstd -s r --description 'operate recursively on directories .'
complete -c unzstd -l format --description 'compress and decompress in other formats.'
complete -c unzstd -o h/-H -l help --description 'display help/long help and exit .'
complete -c unzstd -s V -l version --description 'display version number and exit.'
complete -c unzstd -s v --description 'verbose mode .'
complete -c unzstd -s q -l quiet --description 'suppress warnings, interactivity, and notifications.'
complete -c unzstd -l no-progress --description 'do not display the progress bar, but keep all other messages.'
complete -c unzstd -s C -l check --description 'add integrity check computed from uncompressed data (default: enabled) .'

