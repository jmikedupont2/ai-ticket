
Functions to inspect: `add_chat_*`

`  grep add_chat_ function_calls2.csv | cut -d, -f2 |cut -d. -f3- |sort |uniq -c`

`forge.sdk.memory.memstore_tools.add_chat_memory`

In the `forge.db.ForgeDatabase` :
	`add_chat_history` calls `add_chat_message` in the derived classes




  511  grep on_message function_calls2.csv
  512  grep add_chat_message function_calls2.csv
  513  grep add_chat_message function_calls2.csv |grep -v ,autogpts
  514  grep add_chat_message function_calls2.csv | cut -d, -f2
  515  grep add_chat_message function_calls2.csv | cut -d, -f2 |cut -d. -f3
  516  grep add_chat_message function_calls2.csv | cut -d, -f2 |cut -d. -f3-
  517  grep add_chat_message function_calls2.csv | cut -d, -f2 |cut -d. -f3- |sort |uniq -c



