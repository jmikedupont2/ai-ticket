
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
	    pyre init  > pyre_init.txt
	fi
	if [ ! -f  pyre_coverage.txt ] ; then	    
	    pyre coverage > pyre_coverage.txt
	fi
	if [ ! -f  pyre_statistics.txt ] ; then	    
	    pyre statistics >  pyre_statistics.txt
	fi
	#rm pyre_callgraph.json
	if [ ! -f  pyre_callgraph.json ] ; then
	    pyre start
	    pyre query "dump_call_graph()" >  pyre_callgraph.json
	    pyre stop
	fi

	if [ ! -f functions.txt ] ; then
	    
	    jq ".response|keys[]" -r pyre_callgraph.json  > functions.txt
	fi
	
	popd
    fi
done
