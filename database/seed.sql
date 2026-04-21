-- Inserir Permissões Básicas
INSERT INTO permissions (code, description) VALUES 
('manage_users', 'Can create, edit and delete users'),
('manage_roles', 'Can manage roles and permissions'),
('view_all_tickets', 'Can view tickets from all users'),
('manage_tickets', 'Can edit and delete any ticket');

-- Inserir Cargo ADMIN
INSERT INTO roles (name, description) VALUES ('ADMIN', 'System Administrator');

-- Vincular todas as permissões ao ADMIN
INSERT INTO role_permissions (role_id, permission_id)
SELECT (SELECT id FROM roles WHERE name = 'ADMIN'), id FROM permissions;

-- Inserir Usuário Administrador (Senha: Welcome@123)
-- Hash gerado pelo werkzeug.security
INSERT INTO users (name, email, department, password_hash, role_id) 
VALUES (
    'Main Admin', 
    'admin@techcorp.com', 
    'IT Management', 
    'scrypt:32768:8:1$WlP7D8m2lO2B$a6f9b1e8e9c9d0b1a2f3e4d5c6b7a8f9e0d1c2b3a4f5e6d7c8b9a0f1e2d3c4b5',
    (SELECT id FROM roles WHERE name = 'ADMIN')
);

-- Inserir Usuários de Teste (Exemplos)
INSERT INTO users (name, email, department) VALUES 
('Ian Curtis', 'ian@joydivision.com', 'IT Security'),
('Robert Smith', 'robert@thecure.com', 'Design'),
('Kurt Cobain', 'kurt@nirvana.com', 'QA');