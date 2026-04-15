CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_number TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phone_book WHERE name = p_name) THEN
        UPDATE phone_book
        SET number = p_number
        WHERE name = p_name;
    ELSE
        INSERT INTO phone_book(name, age, number)
        VALUES (p_name, NULL, p_number);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], numbers TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        
        IF numbers[i] ~ '^\+7[0-9 ]+$' THEN
            CALL upsert_user(names[i], numbers[i]);
        ELSE
            RAISE NOTICE 'Invalid: % %', names[i], numbers[i];
        END IF;

    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phone_book
    WHERE name = p_value OR number = p_value;
END;
$$;