CREATE TABLE testing
(
  id integer NOT NULL,
  name character varying,
  login time without time zone,
  logout time without time zone,
  "interval" time without time zone,
  PRIMARY KEY (id)
)

select * from testing;
select count(*) from testing;

DECLARE cnt INTEGER;
--SELECT INTO cnt count(*) FROM testing;

insert into login_count values(COUNT(login)) FROM testing;
insert into testing values login_count count(login);
insert into testing values login_count count(login);


-- ************************* login() insert history data *****************


CREATE OR REPLACE FUNCTION public.log_change()
  RETURNS trigger AS
$BODY$
begin
if new.lts_i<>old.lts_i or new.lts_O<>old.lts_O or new.interval_time<>old.interval_time then
insert into history values(old.pid, old.pname, new.desig, new.dept, old.lts_i, new.lts_O, old.lts_O, new.lts_O, old.p_status, new.p_status, old.interval_time,
new.interval_time, old.total_interval_time, new.total_interval_time, old.out_count, new.out_count, current_date);
end if;
return new;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION public.log_change()
  OWNER TO prosenjit;

  CREATE TRIGGER loc_changer
  BEFORE UPDATE
  ON public.employee
  FOR EACH ROW
  EXECUTE PROCEDURE public.log_change();

DROP TRIGGER loc_changer ON public.employee;
DROP FUNCTION public.log_change();

-- login() insert history data and update into login and logout to employee ******************************************************************

CREATE OR REPLACE FUNCTION login_out()
  RETURNS trigger AS
$BODY$
begin
	if new.lts_i <> old.lts_i then
		new.login := TO_CHAR(current_timestamp, 'hh12:mi:ss AM');
		new.today := current_date;
		insert into history values(old.pid, old.pname, new.desig, new.dept, old.lts_i, new.lts_O, old.lts_O, new.lts_O, old.p_status, 
			new.p_status, old.out_count, new.out_count, current_date, new.login_count, old.login_count,
			old.interval_time, new.interval_time, old.total_interval_time, new.total_interval_time);
		new.login_count := count(new_lts_i) from history where log_date = current_date and pid = new.pid;
	elsif new.lts_O <> old.lts_O then
		new.logout = TO_CHAR(current_timestamp, 'hh12:mi:ss AM');
		new.today := current_date;
		new.out_count := count(new_lts_O) from history where log_date = current_date and pid = new.pid;
	end if;
	return new;
end;
$BODY$
LANGUAGE plpgsql;

CREATE TRIGGER login_out
  BEFORE UPDATE
  ON employee
  FOR EACH ROW
  EXECUTE PROCEDURE login_out();


DROP TRIGGER update_loogin ON public.employee;
DROP FUNCTION public.login();
