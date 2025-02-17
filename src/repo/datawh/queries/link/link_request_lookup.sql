SELECT
    *
from 
    iracing_api.discord_uid_ir_cust_id
WHERE
    request_id = %(request_id)s