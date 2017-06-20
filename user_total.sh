#user Total Automation
hive -e "insert into user_active_dump.user_total
select a.ts,a.total,case when (a.total-b.difflastrun) is null then 0 else (a.total-b.difflastrun) end
from (SELECT from_unixtime(unix_timestamp()) as ts,count(*) as total from user_active_dump.user) a,
(select sum(total_users) as difflastrun from user_active_dump.user_total
where time_ran > from_unixtime(unix_timestamp()))b;"
