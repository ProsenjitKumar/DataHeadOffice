create function emp_trigger_func()
  returns trigger
as
$$
begin
   new.today := current_date;
end;
$$
language plpgsql;

create trigger update_today
  before update on employee
  for each row
  when (NEW.lts_i <> OLD.lts_i or NEW.lts_O <> OLD.lts_O)
  execute procedure emp_trigger_func();

  create trigger update_today
  before update on employee
  for each row
  when (   NEW.lts_i is distinct from OLD.lts_i 
        or NEW.lts_O is distinct from OLD.lts_O)
  execute procedure emp_trigger_func();

  DROP TRIGGER update_today ON public.employee;
  DROP FUNCTION public.emp_trigger_func();

-- ********************************************************
create or replace function employee_change()
returns trigger as
$BODY$
begin
if new.lts_i<>old.lts_i or new.lts_O<>old.lts_O or new.interval_time<>old.interval_time then
update employee set today = current_date where pid = new.pid;
end if;
end;
$BODY$
language plpgsql;

create trigger employee_changer
before update
on employee
for each row
execute procedure employee_change()





How to measure interval time from two individual time with postgresql

I have some column fields respectively pid(primary key) login, logout, interval_time, today(current_date)

login and logout data types are (time without time zone)

Here login and logout data data such like 10:00:45, 12:45:12, 07: 32:02( not like 14:32:12, 18:65:78, 23:51:00)

So i can't understand when night or day, or pm or am.

If someone login = 07:00:00 and logout = 11:00:00
again he/she login = 01:00:00
that means here interval_time will be 2 hours. Exactly how much time he/she was inactive.

I've written a trigger

create or replace function interval_time()
returns trigger as
$BODY$
    begin
        if new.login or new.logout then
            if new.login then
                update employee set interval_time = new.logout::time - login::time where pid = new.pid; -- employee is my table name
            end if;
        end if;
    end;
$BODY$
language plpgsql;

# this trigger just sample, it doesn't work.


create trigger employee_changer
before update
on employee
for each row
execute procedure employee_change()

Please let me know if you have any question
Any help woud be appreciated
Thanks.


















