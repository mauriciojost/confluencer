import json
import sys

space_name = sys.argv[1]
page_filename = sys.argv[2]
title = sys.argv[3]
ancestor = int(sys.argv[4])

with open(page_filename, 'r') as content_file:
   content = content_file.read()

print (json.dumps({
"type":"page",
"title":title,
"ancestors":[{"id":ancestor}],
"space": { "key":space_name },
"body": { "storage":{ "value":content, "representation":"storage" }
}
}))


