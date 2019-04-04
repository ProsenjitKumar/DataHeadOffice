select * from history
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


-- ******************************* function for duplicate key error ****************************

CREATE FUNCTION upsert (sql_update TEXT, sql_insert TEXT)
    RETURNS VOID
    LANGUAGE plpgsql
AS $$
BEGIN
    LOOP
        -- first try to update
        EXECUTE sql_update;
        -- check if the row is found
        IF FOUND THEN
            RETURN;
        END IF;
        -- not found so insert the row
        BEGIN
            EXECUTE sql_insert;
            RETURN;
            EXCEPTION WHEN unique_violation THEN
                -- do nothing and loop
        END;
    END LOOP;
END;
$$;


********


CREATE FUNCTION employee_db(
  pid1 integer,
  pname1 text,
  desig1 text,
  dept1 text,
  lts_i1 time,
  lts_o1 time,
  p_status1 text
) RETURNS VOID AS
$$
BEGIN
LOOP
-- first try to update the key
-- note that "a" must be unique
UPDATE employee SET (lts_i, lts_o, p_status) = (lts_i1, lts_o1, p_status1) WHERE pid = pid1;
IF found THEN
RETURN;
END IF;
-- not there, so try to insert the key
-- if someone else inserts the same key concurrently,
-- we could get a unique-key failure
BEGIN
INSERT INTO employee(pid, pname, desig, dept, lts_i, lts_o, p_status) VALUES (pid1, pname1, desig1, dept1, lts_i1, lts_o1, p_status1);
RETURN;
EXCEPTION WHEN unique_violation THEN
-- do nothing, and loop to try the UPDATE again
END;
END LOOP;
END;
$$
LANGUAGE plpgsql;