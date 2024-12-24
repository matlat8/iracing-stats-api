import json
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import JSONResponse

class NanJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, float):
            if obj != obj or obj == float('inf') or obj == float('-inf'):
                return None
        return super().default(obj)
    
class NanJSONResponse(JSONResponse):
    def render(self, content):
        return json.dumps(
            content,
            ensure_ascii=False,
            cls=NanJSONEncoder
        ).encode('utf-8')