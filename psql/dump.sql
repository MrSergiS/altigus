create TABLE job_alert (
    id SERIAL PRIMARY KEY,
    title VARCHAR(256) NOT NULL,
    intro VARCHAR(1),
    sensin VARCHAR(1),
    think VARCHAR(1),
    percep VARCHAR(1),
    short_description TEXT,
    full_description TEXT,
    min_salary_germany INT,
    max_salary_germany INT,
    min_salary_latvia INT,
    max_salary_latvia INT,
    reason TEXT
);

create TABLE client (
    id SERIAL PRIMARY KEY,
    client_id BIGINT NOT NULL,
    client_name VARCHAR(32),
    language VARCHAR(24)
);

create TABLE client_comunicate (
    id SERIAL PRIMARY KEY,
    client INT,
    consest_save BOOLEAN,
    recommend BOOLEAN,
    FOREIGN KEY (client) REFERENCES client(id)
);

create TABLE quiz (
    id SERIAL PRIMARY KEY,
    client_id INT,
    age SMALLINT,
    gender VARCHAR(32),
    education VARCHAR(32),
    planning_education VARCHAR(32),
    salary INT,
    five_year_salary INT,
    expert_salary INT,
    required_skills VARCHAR(32),
    group_size VARCHAR(32),
    describes VARCHAR(32),
    decision VARCHAR(32),
    difficulty VARCHAR(32),
    job_type VARCHAR(32),
    disappear VARCHAR(32),
    high_demand VARCHAR(32),
    personal_growth VARCHAR(32),
    switch_job VARCHAR(32),
    balance VARCHAR(32),
    impact VARCHAR(32),
    mobile VARCHAR(32),
    work_space VARCHAR(32),
    benefits VARCHAR(32),
    FOREIGN KEY (client_id) REFERENCES client(id)
);

create TABLE result (
    id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    result VARCHAR(4) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES client(id)
);
