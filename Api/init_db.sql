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

CREATE TABLE invites (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id int,
	project_id int,
	status varchar(128),
	joined_at datetime,

	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (project_id) REFERENCES projects(id)
);

INSERT INTO roles (role) VALUES ('admin'), ('manager'), ('developer'), ('tester');
INSERT INTO users (username, email, password, created_at, role_id) 
VALUES ('dev', 'dev@ply.to', '123456', CURRENT_TIMESTAMP, 1);

INSERT INTO users (username, email, password, created_at, role_id) 
VALUES ('test', 'test@mail.to', '123456', CURRENT_TIMESTAMP, 1);

INSERT INTO projects (title, description, creator_id, created_at)
VALUES ('invite project', 'testing if multiple users are in project', 1, CURRENT_TIMESTAMP);

INSERT INTO invites (user_id, project_id, status, joined_at)
VALUES (2, 1, 'joined', CURRENT_TIMESTAMP);
