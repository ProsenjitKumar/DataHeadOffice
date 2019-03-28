select * from employee
select * from history


select lts_i::time - lts_O::time from employee

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

-- Note that <> doesn't properly deal with NULL values. If lts_i or lts_o can contain null values, then firing condition is better written as:

  when (   NEW.lts_i is distinct from OLD.lts_i
        or NEW.lts_O is distinct from OLD.lts_O)

-- ******************** interval time *****************************

create function emp_interval_time()
    returns trigger as
$$
begin
if new.lts_i and new.today = current_date then
    if new.lts_O then
        if new.lts_i then
            update employee set interval_time = new.lts_i::time - new.lts_O::time;
            return new;
        end if;
    end if;
end if;
end;
$$
language plpgsql;

DROP FUNCTION public.emp_interval_time();
DROP TRIGGER update_interval_time ON public.employee;

create trigger update_interval_time
before update
on employee
for each row
execute procedure emp_interval_time()



--$$
--begin
--if new.lts_i and new.today = current_date then
--    select lts_i from employee;
--    select lts_i from employee;
--end if;
--end;
--$$