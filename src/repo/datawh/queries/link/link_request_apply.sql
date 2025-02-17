ALTER TABLE iracing_api.discord_uid_ir_cust_id
UPDATE ir_cust_id = %(cust_id)s
WHERE request_id = %(request_id)s