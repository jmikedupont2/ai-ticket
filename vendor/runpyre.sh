
#set -e 

for D in PolyGPT-alpha Tonic-AI
do
    if [ -d "${D}" ]; then
        echo "${D}"   # your processing here
	pushd $D
	DIRN="../../pyre/report/$D/report/"
	if [ ! -d $DIRN ] ;
	then
	    mkdir -p $DIRN
	fi	

	if [ ! -f .pyre_configuration ]; then
	    cp ../../pyre/.pyre_configuration  .
	fi
	if [ ! -f .watchmanconfig ]; then
	    cp ../../pyre/.watchmanconfig  .
	fi
	ls "${DIRN}"
	if [ ! -f  ${DIRN}/pyre_init.txt ] ; then	    
	    pyre init  > $DIRN/pyre_init.txt

	    #echo init
	fi
	pyre start
	if [ ! -f  ${DIRN}/pyre_coverage.txt ] ; then	    
	    pyre coverage > $DIRN/pyre_coverage.txt	    
	fi
	if [ ! -f  ${DIRN}/pyre_statistics.txt ] ; then	    
	    pyre statistics >  $DIRN/pyre_statistics.txt
	fi
	
	#rm pyre_callgraph.json
	if [ ! -f  ${DIRN}/pyre_callgraph.json ] ; then

	    pyre query "dump_call_graph()" >  ${DIRN}/pyre_callgraph.json

	fi

	if [ ! -f ${DIRN}/functions.txt ] ; then
	    jq ".response|keys[]" -r pyre_callgraph.json  > ${DIRN}/functions.txt
	fi
	pyre stop
	#pyre analyze --save-results-to $DIRN
	
	popd
    fi
done
