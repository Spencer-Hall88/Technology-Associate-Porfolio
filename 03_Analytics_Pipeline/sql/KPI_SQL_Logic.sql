-- This query demonstrates backend logic used to aggregate the metrics directly in the database.
-- It utilizes date arithmetic and CASE WHEN logic for SLA compliance.

SELECT 
    customer_tier,
    COUNT(ticket_id) AS total_tickets,
    ROUND(AVG((julianday(resolved_date) - julianday(created_date)) * 24), 2) AS avg_resolution_hours,
    SUM(CASE WHEN (julianday(resolved_date) - julianday(created_date)) * 24 <= 24 THEN 1 ELSE 0 END) AS tickets_meeting_sla
FROM 
    raw_tickets
WHERE 
    resolved_date IS NOT NULL
GROUP BY 
    customer_tier;