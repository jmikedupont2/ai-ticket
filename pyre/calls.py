from collections import Counter
import pandas as pd
data=[]
import glob, json
names = "./report/*/report/pyre_callgraph.json"
#pyre_callgraph.json"

files = {}
calls=[]
for name in glob.glob(names):
  print(name)
  with open(name) as fi :
    for x in fi:
      d = json.loads(x)
      data = d["response"]
      for x in list(data.keys()):
        if (len(data[x])):
          for y in data[x]:
            if "direct_target" in y:
              calls.append( y["direct_target"])
df= Counter(calls)
df2=pd.DataFrame(df.most_common(), columns=["name","count"])
df2.to_csv("function_calls.csv")
#table = pd.pivot_table(df,
#       values="count",
#        index="name", sort=True,
#        # columns=['function'],
#      aggfunc="sum")
#table.to_csv("call_sum.csv")
