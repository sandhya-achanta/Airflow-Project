#autoating user_report table
hive -e "insert OVERWRITE TABLE user_active_dump.user_report
SELECT user.id as user_id,
CASE WHEN s1.totinserts > 0 then s1.totinserts else 0 END as total_inserts,
CASE WHEN s2.totupdates > 0 then s2.totupdates else 0 END as total_updates,
CASE WHEN s3.totdeletes > 0 then s3.totdeletes else 0 END as total_deletes,
CASE WHEN s4.type is not null then s4.type END as last_activity_type,
CASE WHEN s5.active > 0 then true  else false END as is_active,
CASE WHEN s6.upload_count > 0 then s6.upload_count else 0 END as upload_count
FROM user_active_dump.user
                  left outer JOIN
                (SELECT  user_id,count(*) as totinserts
                 FROM  user_active_dump.activitylog where type = 'INSERT'
                 GROUP BY user_id) S1
ON S1.user_id = user.id
left outer JOIN
                (SELECT  user_id,count(*) as totupdates
                 FROM  user_active_dump.activitylog where type = 'UPDATE'
                 GROUP BY user_id) S2
ON S2.user_id = user.id
left outer JOIN
                (SELECT  user_id,count(*) as totdeletes
                 FROM  user_active_dump.activitylog where  type = 'DELETE'
                 GROUP BY user_id) S3
ON S3.user_id = user.id
left outer JOIN (select t1.user_id as user_id ,type from user_active_dump.activitylog t1
join (
  select user_id, max(timestamp) maxModified from user_active_dump.activitylog
  group by user_id
) s
on t1.user_id  = s.user_id and t1.timestamp = s.maxModified) S4
ON S4.user_id = user.id
left outer JOIN (SELECT user_id,count(*) as active  FROM  user_active_dump.activitylog  WHERE timestamp between ( unix_timestamp() -2*24*60*60) and unix_timestamp() group by user_id)S5
ON S5.user_id = user.id
left outer JOIN (select user_id,count(*) as upload_count from user_active_dump.user_upload_dump group by user_id) S6
ON S6.user_id = user.id;"

