#!/bin/csh -f

set num=`find . |wc -l`
echo "$num - ./ "
echo "----- TOTAL -------"

foreach dir ( * .* )
    if ( $dir == "." ) then
        continue
    endif
    if ( $dir == ".." ) then
        continue
    endif
    if ( -d $dir ) then
        set num=`find $dir |wc -l`
        echo "$num - $dir "
    endif
end

