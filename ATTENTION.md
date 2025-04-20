
you may use this image kenneth850511/llamafactory:v0.9.1, or build your own image

must up date llama factory data converter /app/src/llamafactory/data/converter.py


```bash
at column 133
add these code
```python
even_tags = (self.dataset_attr.assistant_tag, self.dataset_attr.function_tag)  
accept_tags = (odd_tags, even_tags)
messages = example[self.dataset_attr.messages]

# above are existing codes
# add this code below
import json
messages = json.loads(messages)
```
