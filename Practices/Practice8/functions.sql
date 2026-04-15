CREATE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, age INT, number VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name, pb.age, pb.number
    FROM phone_book pb
    WHERE pb.name ILIKE '%' || pattern || '%'
       OR pb.number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name VARCHAR, age INT, number VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name, pb.age, pb.number
    FROM phone_book pb
    ORDER BY pb.id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;