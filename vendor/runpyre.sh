
#set -e 

for D in *
do
    if [ -d "${D}" ]; then
        echo "${D}"   # your processing here
	pushd $D
	if [ ! -f .pyre_configuration ]; then
	    cp ../../pyre/.pyre_configuration  .
	fi
	if [ ! -f .watchmanconfig ]; then
	    cp ../../pyre/.watchmanconfig  .
	fi
	if [ ! -f  pyre_init.txt ] ; then	    
	    pyre init  |tee pyre_init.txt
	fi
	if [ ! -f  pyre_coverage.txt ] ; then	    
	    pyre coverage |tee pyre_coverage.txt
	fi
	if [ ! -f  pyre_statistics.txt ] ; then	    
	    pyre statistics | tee  pyre_statistics.txt
	fi
	if [ ! -f  pyre_dump.json ] ; then	    
	    #pyre dump --output pyre_dump.json
	    #pyre-check query "types_in_file('tests.py')"
	    echo pass
	fi
	popd
    fi
done
