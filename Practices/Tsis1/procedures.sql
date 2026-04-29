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



CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR, 
    p_phone VARCHAR, 
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name;

    IF v_contact_id IS NOT NULL THEN
        INSERT INTO phones (contact_id, phone, type) 
        VALUES (v_contact_id, p_phone, p_type);
        RAISE NOTICE 'Phone added to contact %', p_contact_name;
    ELSE
        RAISE EXCEPTION 'Contact % not found', p_contact_name;
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR, 
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INTEGER;
BEGIN
    INSERT INTO groups (name) 
    VALUES (p_group_name)
    ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name
    RETURNING id INTO v_group_id;

    UPDATE contacts 
    SET group_id = v_group_id 
    WHERE name = p_contact_name;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Contact % not found', p_contact_name;
    END IF;
END;
$$;