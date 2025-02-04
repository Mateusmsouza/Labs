INSERT INTO bugs (summary, description, send_to_kanban) 
VALUES ('Login button not working', 'The login button does not respond when clicked.', FALSE);

UPDATE bugs 
SET send_to_kanban = TRUE
WHERE summary = 'Login button not working';

DELETE FROM bugs 
WHERE summary = 'Login button not working';

