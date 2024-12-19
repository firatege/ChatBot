CREATE DATABASE chatbot;

-- user table
CREATE TABLE user_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- user_message table

CREATE TABLE user_message (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_table(id)
);


-- entity table
CREATE TABLE entity_table (
    id SERIAL PRIMARY KEY,
    intent_id INT NOT NULL,
    entity_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


--intent table
CREATE TABLE intent_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);


-- message_table
CREATE TABLE message_table (
    id SERIAL PRIMARY KEY,
    message_id INT NOT NULL,
    intend_id INT NOT NULL,
    entity_id INT NOT NULL,
    entity_value VARCHAR(255) NOT NULL,
    FOREIGN KEY (message_id) REFERENCES user_message(id),
    FOREIGN KEY (intend_id) REFERENCES intent_table(id)
);



-- context table

CREATE TABLE context_table (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    previous_intent_id INT,
    previous_entity_id INT,
    context_data TEXT NOT NULL,
    last_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_table(id),
    FOREIGN KEY (previous_intent_id) REFERENCES intent_table(id),
    FOREIGN KEY (previous_entity_id) REFERENCES entity_table(id)

);

-- response pool

CREATE TABLE response_pool (
    id SERIAL PRIMARY KEY,
    intent_id INT NOT NULL,
    entity_id INT NOT NULL,
    response TEXT NOT NULL,
    context_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rating INT,
    FOREIGN KEY (intent_id) REFERENCES intent_table(id),
    FOREIGN KEY (entity_id) REFERENCES entity_table(id),
    FOREIGN KEY (context_id) REFERENCES context_table(id)
);