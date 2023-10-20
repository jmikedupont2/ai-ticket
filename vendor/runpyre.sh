
#set -e 

for D in *
do
    if [ -d "${D}" ]; then
        echo "${D}"   # your processing here
	pushd $D
	DIRN="../../pyre/report/$D/report/"
	if [ ! -d $DIRN ] ;
	then
	    echo mkdir $DIRN
	fi	

	if [ ! -f .pyre_configuration ]; then
	    cp ../../pyre/.pyre_configuration  .
	fi
	if [ ! -f .watchmanconfig ]; then
	    cp ../../pyre/.watchmanconfig  .
	fi
	if [ ! -f  ${DIRN}/pyre_init.txt ] ; then	    
	    pyre init  > $DIRN/pyre_init.txt
	fi
	if [ ! -f  ${DIRN}/pyre_coverage.txt ] ; then	    
	    pyre coverage > $DIRN/pyre_coverage.txt
	fi
	if [ ! -f  ${DIRN}/pyre_statistics.txt ] ; then	    
	    pyre statistics >  $DIRN/pyre_statistics.txt
	fi
	
	#rm pyre_callgraph.json
	if [ ! -f  ${DIRN}/pyre_callgraph.json ] ; then
	    pyre start
	    pyre query "dump_call_graph()" >  ${DIRN}/pyre_callgraph.json
	    pyre stop
	fi

	if [ ! -f ${DIRN}/functions.txt ] ; then
	    
	    jq ".response|keys[]" -r pyre_callgraph.json  > ${DIRN}/functions.txt
	fi

	#pyre analyze --save-results-to $DIRN
	
	popd
    fi
done
