prep
`pip install pyre-check`

run this to collect data
`vendor/runpyre.sh`

list of files
`jq -r keys[] pyre_statistics.txt ` 

pyre-check query "types_in_file('tests.py')"
