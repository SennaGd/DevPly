CREATE TABLE roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role varchar(255) NOT NULL
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL CHECK (LENGTH(password) >= 6),
    created_at datetime,
    role_id int,

    FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(255) NOT NULL,
    description text NOT NULL,
    creator_id int NOT NULL,
    created_at datetime,

    FOREIGN KEY (creator_id) REFERENCES users(id)
);

CREATE TABLE project_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id int NOT NULL,
    user_id int NOT NULL,
    role_id int NOT NULL,
    joined_at datetime,

    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE requirements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id int,
    title varchar(255),
    description text,
    status int,

    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requirement_id int,
    project_id int,
    title varchar(255),
    description text,
    status int,

    FOREIGN KEY (requirement_id) REFERENCES requirements(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id int,
    project_id int,
    title varchar(255),
    description text,
    status int,

    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

INSERT INTO roles (role) VALUES ('admin'), ('manager'), ('developer'), ('tester');
INSERT INTO users (username, email, password, created_at, role_id) 
VALUES ('dev', 'dev@ply.to', '123456', CURRENT_TIMESTAMP, 1);
