CREATE TABLE shoelace_log (
    sl_name    text,          -- shoelace changed
    sl_avail   integer,       -- new available value
    log_who    text,          -- who did it
    log_when   timestamp,      -- when
    primary key(sl_avail)
);


insert into shoelace_log values('Prosenjit Das', 13, 'Prosenjit', '1994-06-12');
insert into shoelace_log values('Pagla Das', 33, 'Pagla', '1944-06-12');


update shoelace_log set log_who = 'Prosenjit' where sl_avail = 12;
update shoelace_log set log_when = current_date where sl_avail = 33;

CREATE RULE log_shoelace AS ON UPDATE TO shoelace_log
    WHERE NEW.sl_avail <> OLD.sl_avail
    DO INSERT INTO shoelace_log VALUES (
                                    NEW.sl_name,
                                    NEW.sl_avail,
                                    current_user,
                                    current_timestamp
                                );




CREATE OR REPLACE FUNCTION public.employee_change()
  RETURNS trigger AS
$BODY$
begin
if new.lts_i<>old.lts_i or new.lts_O<>old.lts_O or new.interval_time<>old.interval_time then
update employee set today = current_date where pid = new.pid;
end if;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION public.employee_change()
  OWNER TO prosenjit;



create function emp_trigger_func()
returns trigger
as
$$
begin
   new.today := current_date;
   return new;
end;
$$
language plpgsql;

create trigger update_today
  before update on employee
  for each row
  when (NEW.lts_i <> OLD.lts_i or NEW.lts_O <> OLD.lts_O)
  execute procedure emp_trigger_func();

DROP FUNCTION public.employee_change();
DROP TRIGGER employee_changer ON public.employee;
