import json
import sys

space_name = sys.argv[1]
page_filename = sys.argv[2]
title = sys.argv[3]
ancestor = int(sys.argv[4])

with open(page_filename, 'r') as html_content_file:
   html_content = html_content_file.read()

print (json.dumps({
"type":"page",
"title":title,
"ancestors":[{"id":ancestor}],
"space": { "key":space_name },
"body": { "storage":{ "value":html_content, "representation":"storage" }
}
}))


