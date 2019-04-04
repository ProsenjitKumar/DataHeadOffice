-- interval time **************************************************************

SELECT EXTRACT(hours from '80 minutes'::interval);
SELECT
 now(),
 now() - INTERVAL '1 year 3 hours 20 minutes' 
             AS "3 hours 20 minutes ago of last year";

select INTERVAL '1 year 2 months 3 days';
select INTERVAL '10:00:00 PM';

SELECT
INTERVAL '2h 50m' + INTERVAL '10m'; -- 03:00:00

SELECT
INTERVAL '2h 50m' - INTERVAL '50m'; -- 02:00:00
 
SELECT EXTRACT(INTERVAL '10:00:00 PM' - INTERVAL '01:00:00 AM'); -- 02:00:00
 
SELECT
600 * INTERVAL '1 minute'; -- 10:00:00

TO_CHAR(interval,format)

SELECT
    TO_CHAR(
        INTERVAL '17h 20m 05s',
        'HH24:MI:SS'
    );

    SELECT
    EXTRACT (
        MINUTE
        FROM
            INTERVAL '5 hours 21 minutes'
    );

SELECT
    justify_interval(interval '1 year -1 hour');
  select justify_interval(interval '10:00:00' - '01:00:00');
  select justify_interval(interval logout - login) from employee where pid = 15;

select current_time - interval '1' hour
select '14:13:49+06' - interval '11:25:00'

select interval '1 month',
       interval '2 weeks',
       2 * interval '1 week',
       78389 * interval '1 ms';

select d::date as month,
       (d + interval '1 month' - interval '1 day')::date as month_end,
       (d + interval '1 month')::date as next_month,
       (d + interval '1 month')::date - d::date as days

  from generate_series(
                       date '2017-01-01',
                       date '2017-12-01',
                       interval '1 month'
                      )
       as t(d);
select INTERVAL YEAR TO MONTH 


-- interval time trigger *******************************************************

create function emp_interval_time()
    returns trigger as
$$
begin
if new.lts_i<>old.lts_i and new.lts_O<>old.lts_O then
	update employee set interval_time = new.lts_i::time - new.lts_O::time where pid = new.pid;
end if;
return new;
end;
$$
language plpgsql;

create trigger update_interval_time
before update
on employee
for each row
execute procedure emp_interval_time()


DROP TRIGGER update_interval_time ON public.employee;
DROP FUNCTION public.emp_interval_time();

SELECT EXTRACT(MICROSECONDS FROM TIMESTAMP '2016-12-31 13:30:15');
SELECT EXTRACT(YEAR FROM TIMESTAMP '2016-12-31 13:30:15');

select time '01:00' - time '11:00' from employee where pid = 45;
	select time '11:00' - time '01:00'

select current_date + current_time
select sum(current_time, current_time)
select '01:00:00' + time '01:00:00'
select current_time + time '01:00:00'
select transaction_timestamp()
select statement_timestamp()
select clock_timestamp() - "2019-03-29 00:34:29.225689+06"
select timeofday() 
select now()
SELECT CURRENT_TIMESTAMP;

SELECT TIMESTAMP '2001-02-16 20:38:40-05' AT TIME ZONE 'Asia/Tokyo' AT TIME ZONE 'America/Chicago';
SELECT now() AT TIME ZONE 'Asia/Dhaka';

SELECT LOCALTIMESTAMP;

select age(timestamp '1994-12-27')
SELECT TO_CHAR(current_timestamp, 'yyyy-mm-dd hh12:mi:ss AM')
SELECT TO_CHAR(current_timestamp, 'yyyy-mm-dd')
SELECT TO_CHAR(current_timestamp, 'yyyy-mm-dd')
SELECT TO_CHAR(current_timestamp, 'hh12:mi:ss AM') - '10:48:21 PM'::time

select '01:48:21 PM'::time - '10:48:21 AM'::time
select '01:48:21 PM'::interval - '10:48:21 AM'::interval
select '01:48:01 PM'::time - '10:48:21 AM'::time
select '00:48:01 PM'::time > '11:48:21 AM'::time
select '00:48:01 PM'::time < '11:48:21 AM'::time


--a := '00:48:01 PM' time with time zone;
--b := '01:48:01 PM' time with time zone;
$BODY$
declare
	a := 5 integer;
	b := 2 integer;
begin
if a > b then
	select '01:48:01 PM'::time - '10:48:21 AM'::time;
end if;
end;
$BODY$

SELECT TO_CHAR(now(), 'HH24:MI:SS') 

if lts_i > lts_O then
	new.interval_time := new.lts_i - new.lts_O
else if
	new.interval_time := new.lts_O - new.lts_i

select lts_i - lts_O from employee where pid = 15;
select lts_O - lts_i from employee where pid = 15;
select count(lts_O) from employee where pid = 101;

create or replace function interval_time()
returns trigger as
$BODY$
    begin
        if new.lts_i<>old.lts_i and new.today = current_date or new.lts_O<>old.lts_O and new.today = current_date then
		if new.lts_O<>old.lts_O then
			if new.lts_i<>old.lts_i then
				if new.logout::time > new.login::time where new.today = current_date and new.pid = new.pid then
					new.interval_time := new.logout::time - new.login::time where new.today = current_date and new.pid = new.pid;
				else
					new.interval_time := new.login::time - new.logout::time where new.today = current_date and new.pid = new.pid; 
				end if;
		else
			if new.logout::time < new.login::time where new.today = current_date and new.pid = new.pid then
					new.interval_time := new.logout::time - new.login::time where new.today = current_date and new.pid = new.pid;
				else
					new.interval_time := new.login::time - new.logout::time where new.today = current_date and new.pid = new.pid; 
				end if;
			end if;
		end if;
        end if;
    return new;
    end;
$BODY$
language plpgsql;
	

create trigger interval_time_update
before update
on employee
for each row
execute procedure interval_time()

-- new interval time ************************************************************

create or replace function interval_time()
returns trigger as
$$
begin
	if new.login<>old.login and new.login_count > new.out_count and new.today = current_date then
		if new.logout::time > new.login::time where new.today = current_date and new.pid = new.pid then
			new.interval_time := new.logout::time - new.login::time where new.today = current_date and new.pid = new.pid;
		elsif new.logout::time < new.login::time where new.today = current_date and new.pid = new.pid then
			new.interval_time := new.logout::time - new.login::time where new.today = current_date and new.pid = new.pid;
		end if;
	end if;
	return new;
end;
$$
language plpgsql;

create trigger interval_time_update
before update
on employee
for each row
execute procedure interval_time()

-- ***********************************

select login_count > out_count from employee where pid = 1;


create or replace function interval_time()
returns trigger as
$$
begin	
	if new.login_count > new.out_count then
		new.interval_time := login::time - logout::time from employee where pid = new.pid and today = current_date and TO_CHAR(current_timestamp, 'hh12:mi:ss AM') < '23:59:59 PM';
	end if;
	return new;
end;
$$
language plpgsql;
				

DROP TRIGGER interval_time_update ON public.employee;
DROP FUNCTION public.interval_time();

update employee set lts_i = '01:45:00' where pid = 25;
update employee set lts_O = '01:46:00' where pid = 25;


update employee set interval_time = login::time - logout::time where pid = 100;

select TO_CHAR(current_timestamp, 'hh12:mi:ss AM') < '23:59:59 PM'
select logout::time > login::time from employee where today = current_date and pid = 15;
select logout::time - login::time from employee where today = current_date and pid = 100;
select logout::time > login::time from employee where today = current_date and pid = 100;
select logout::time - login::time from employee where today = current_date and pid = 1;
select login::time > logout::time from employee where today = current_date and pid = 15;
select '01:00:00'::time - '10:00:00'::time

	--if new.login<>old.login and new.login_count > new.out_count and new.today = current_date then
		--new.interval_time := logout::time - login::time from employee where today = current_date and pid = new.pid;





t=# select now();
              now
-------------------------------
 2017-05-23 09:04:46.105322+00
(1 row)

Time: 0.690 ms
t=# select now()::timestamp;
            now
----------------------------
 2017-05-23 09:04:51.849522
(1 row)

Time: 0.537 ms
So for query in original post it would be:

select (to_timestamp(timestamp_start, 'YYYY-MM-DD HH24:MI:SS.US') + interval '24 hour')::timestamp as tstamp 
from tablename

select * from history where log_date = '2019-03-27'

-- logout trigger ***********************************

create or replace function logout()
returns trigger as
$BODY$
    begin
        new.logout = TO_CHAR(current_timestamp, 'hh12:mi:ss AM');
        return new;
    end;
$BODY$
language plpgsql;

create trigger logout_update
before update
on employee
for each row
when (new.lts_O <> old.lts_O)
execute procedure logout()


-- ******************************************* if else condition *********************************************

DO $$
DECLARE
  a integer := 10;
  b integer := 20;
BEGIN 
  IF a > b THEN
 RAISE NOTICE 'a is greater than b';
  END IF;
 
  IF a < b THEN
 RAISE NOTICE 'a is less than b';
  END IF;
 
  IF a = b THEN
 RAISE NOTICE 'a is equal to b';
  END IF;
END $$;



DO $$
DECLARE
  a integer := 10;
  b integer := 20;
BEGIN 
   IF a > b THEN 
      RAISE NOTICE 'a is greater than b';
   ELSE
      RAISE NOTICE 'a is not greater than b';
   END IF;
END $$;

DO $$
DECLARE
   a integer := 10;
   b integer := 10;
BEGIN 
  IF a > b THEN 
     RAISE NOTICE 'a is greater than b';
  ELSIF a < b THEN
     RAISE NOTICE 'a is less than b';
  ELSE
     RAISE NOTICE 'a is equal to b';
     PERFORM pname from employee where pid = 2;
  END IF;
END $$;

select * from history where log_date = '2019-03-27';


-- truncate data if first login current_date ***************************************
/*
	new.interval_time := null where new.today = current_date and new.pid = new.pid;
	new.out_count := null where new.today = current_date and new.pid = new.pid;
	new.lts_O := null where new.today = current_date and new.pid = new.pid;
	new.logout := null where new.today = current_date and new.pid = new.pid;
	new.login := null where new.today = current_date and new.pid = new.pid;
	new.out_count := null where new.today = current_date and new.pid = new.pid;
	new.login_count := null where new.today = current_date and new.pid = new.pid;
	new.total_interval_time := null where new.today = current_date and new.pid = new.pid;
	*/
--if current_time = '23:59:59+06' then
--if current_time = '00:59:59+06' then

create or replace function truncate_data()
returns trigger as
$BODY$
    begin
    if TO_CHAR(current_timestamp, 'hh12:mi:ss AM') = ('12:47:00 PM') then
	update employee set (lts_O, interval_time, total_interval_time, out_count, login, logout, login_count) = (null, null, null, null, null, null, null) where pid = new.pid and today = current_date; 
    end if;
    return new;
    end;
$BODY$
language plpgsql;

create trigger truncate_data
before update
on employee
for each row
execute procedure truncate_data()

DROP TRIGGER truncate_data ON public.employee;
DROP FUNCTION public.truncate_data();


select TO_CHAR(current_timestamp, 'hh12:mi:ss AM') = ('12:35:00 AM')
select current_timestamp = '12:35:00 AM'
select current_time = '12:35:00'
update employee set interval_time = null where pid = 22;
select TO_CHAR(current_timestamp, 'hh12:mi:ss');

-- employee logout/ out count ********************************************
select count(lts_i) from employee where pid = 15;
select count(logout) from employee where pid = 15;
select count(old_out_count) from history where pid = 1;
select count(new_out_count) from history where pid = 1;
select count(out_count) from employee where pid = 1;
select count(new_lts_i) from history where log_date = current_date and pid = 1;
select count(old_lts_i) from history where log_date = current_date and pid = 1;
select count(new_lts_O) from history where log_date = current_date and pid = 1;
select count(old_lts_O) from history where log_date = current_date and pid = 1;

create or replace function out_count()
returns trigger as
$BODY$
    begin
        new.out_count := count(new_lts_O) from history where log_date = current_date and pid = new.pid;
        return new;
    end;
$BODY$
language plpgsql;

create trigger out_count_update
before update
on employee
for each row
when (new.lts_i <> old.lts_i and new.today = current_date)
execute procedure out_count()

DROP TRIGGER out_count_update ON public.employee;
DROP FUNCTION public.out_count();

-- total interval time count *******************************************
select '12:23:23' + '01:45:11'::interval;

create or replace function total_interval_time()
returns trigger as
$BODY$

declare
current_interval interval := sum(interval_time) from employee where pid = new.pid and today = current_date;
history_total_interval interval := sum(new_interval_time) from history where log_date = current_date and pid = new.pid;

    begin
	new.total_interval_time := current_interval + history_total_interval;
	--new.total_interval_time := sum(new_interval_time) from history where log_date = current_date and pid = new.pid;
        return new;
    end;
$BODY$
language plpgsql;

create trigger total_interval_time_update
before update
on employee
for each row
when ((new.interval_time<>old.interval_time) and (new.today = current_date))
execute procedure total_interval_time()

DROP TRIGGER total_interval_time_update ON public.employee;
DROP FUNCTION public.total_interval_time();

update employee set lts_i = '10:16:00' where pid = 100;
update employee set lts_O = '11:55:00' where pid = 100;

select sum(new_interval_time) from history where log_date = current_date and pid = 100;
select sum(interval_time) from employee where today = current_date and pid = 100;
select sum(interval_time) from employee where today = current_date and pid = 100;


-- **************** update data manually *************************
update employee set interval_time = login::time - logout::time where pid = 100;
update employee set lts_i = '01:43:00' where pid = 13;
update employee set lts_O = '01:42:00' where pid = 13;

update employee set lts_i = '10:13:00' where pid = 100;
update employee set lts_O = '11:12:00' where pid = 100;


-- time declare ********************************************


DO $$ 
DECLARE
   a time := '05:00:00';
   b time := '10:00:00';
BEGIN 
   RAISE NOTICE '%', a;
   PERFORM pg_sleep(5);
   RAISE NOTICE '%', b;
   RAISE NOTICE '%', a::time + b;
END $$;


DO $$ 
DECLARE
   current_interval time := sum(interval_time) from employee where pid = 100 and today = current_date;
history_total_interval time := sum(new_interval_time) from history where log_date = current_date and pid = 100;
BEGIN 
   RAISE NOTICE '%', current_interval;
   PERFORM pg_sleep(10);
   RAISE NOTICE '%', history_total_interval;
   RAISE NOTICE '%', history_total_interval + current_interval::time;
END $$;

-- column add again *************************************************

ALTER TABLE public.employee ADD COLUMN interval_time time without time zone;
ALTER TABLE public.employee ADD COLUMN total_interval_time time without time zone;

ALTER TABLE public.history ADD COLUMN old_interval_time time without time zone;
ALTER TABLE public.history ADD COLUMN new_interval_time time without time zone;
ALTER TABLE public.history ADD COLUMN old_total_interval_time time without time zone;
ALTER TABLE public.history ADD COLUMN new_total_interval_time time without time zone;


how to update value a certain time later with postgresql

-- cron job shedule *********************************************

SELECT cron.schedule(‘0 11 * * *’, ‘VACUUM ANALYZE’);

select pid first(login, time) from employee gruop by pid = 100;
SELECT device_id, time_bucket('5 minutes', time) AS interval,

SELECT * FROM employee WHERE today >= now() - INTERVAL 1 DAY;
SELECT * FROM employee WHERE today > DATE_SUB(NOW(), INTERVAL 24 HOUR)




