prep
`pip install pyre-check`

run this to collect data
`vendor/runpyre.sh`

list of files
`jq -r keys[] pyre_statistics.txt ` 

pyre-check query "types_in_file('tests.py')"

# produce graphs

`python ./graphs.py ./function_calls2.csv `

strong graphs with 

`python ./strong_graphs.py ./function_calls2.csv `

# split by autogpt

now we can split by the autogpt name


# index

Manually update the index with `tree -H "." > index.html` 

published in webpage: https://jmikedupont2.github.io/ai-ticket/pyre/


# Split out autogpt

```
  grep autogpt function_calls2.csv > autogpt_function_calls.csv
  mkdir autogpt 
  cd autogpt/
  mv ../autogpt_function_calls.csv .
  mkdir graphs
  python ../graphs.py autogpt_function_calls.csv 
  tree -H "." > index.html
  git add autogpt/
```

# analyse sub graphs

```
	jq ".edges[]|.from"  graphComponent*.json  |sort |uniq -c | sort -n |grep autogpt
    jq ".edges[]|.to"  graphComponent*.json  |sort |uniq -c | sort -n |grep autogpt
``` 
  
