select * from history;


create or replace function log_change()
returns trigger as
$BODY$
begin
if new.lts_i<>old.lts_i or new.lts_O<>old.lts_O or new.interval_time<>old.interval_time then
insert into history values(old.pid, old.pname, new.desig, new.dept, old.lts_i, new.lts_O, old.lts_O, new.lts_O, old.p_status, new.p_status, old.interval_time,
new.interval_time, old.total_interval_time, new.total_interval_time, old.out_count, new.out_count, current_date);
end if;
return new;
end;
$BODY$
language plpgsql;

create trigger loc_changer
before update
on employee
for each row
execute procedure log_change()

select current_time;
select current_date

-- trigger for update today column if something changes

create or replace function employee_change()
returns trigger as
$BODY$
begin
if new.lts_i<>old.lts_i or new.lts_O<>old.lts_O or new.interval_time<>old.interval_time then
update employee set today = current_date where pid = new.pid;
end;
$BODY$

create trigger employee_changer
after update
on employee
for each row
execute procedure employee_change()

select * from employee