-- Limpar dados existentes para evitar duplicidade
TRUNCATE role_permissions, ticket_comments, tickets, users, roles, permissions CASCADE;

-- 1. Inserir Permissões Granuladas
INSERT INTO permissions (code, description) VALUES 
('manage_users', 'Criar, editar e remover usuários'),
('manage_roles', 'Gerenciar cargos e permissões do sistema'),
('view_all_tickets', 'Visualizar todos os chamados da organização'),
('manage_tickets', 'Alterar status, prioridade e atribuir qualquer chamado'),
('create_tickets', 'Capacidade de abrir novos chamados'),
('comment_tickets', 'Interagir na timeline dos chamados');

-- 2. Inserir Cargos (Roles)
INSERT INTO roles (name, description) VALUES 
('ADMIN', 'Acesso total ao sistema e configurações'),
('MANAGER', 'Gestão de equipe e monitoramento de métricas'),
('TECHNICIAN', 'Atendimento e resolução de chamados técnicos'),
('USER', 'Usuário final (abertura e acompanhamento)');

-- 3. Vincular Permissões aos Cargos

-- ADMIN: Todas as permissões
INSERT INTO role_permissions (role_id, permission_id)
SELECT (SELECT id FROM roles WHERE name = 'ADMIN'), id FROM permissions;

-- MANAGER: Gestão de tickets e usuários, mas não de cargos
INSERT INTO role_permissions (role_id, permission_id)
SELECT (SELECT id FROM roles WHERE name = 'MANAGER'), id FROM permissions 
WHERE code IN ('manage_users', 'view_all_tickets', 'manage_tickets', 'create_tickets', 'comment_tickets');

-- TECHNICIAN: Focado no atendimento
INSERT INTO role_permissions (role_id, permission_id)
SELECT (SELECT id FROM roles WHERE name = 'TECHNICIAN'), id FROM permissions 
WHERE code IN ('view_all_tickets', 'manage_tickets', 'create_tickets', 'comment_tickets');

-- USER: Apenas o básico
INSERT INTO role_permissions (role_id, permission_id)
SELECT (SELECT id FROM roles WHERE name = 'USER'), id FROM permissions 
WHERE code IN ('create_tickets', 'comment_tickets');

-- 4. Inserir Usuários de Teste
-- SENHA PADRÃO PARA TODOS: teste123
-- Hash gerado via werkzeug.security.generate_password_hash

INSERT INTO users (name, email, department, password_hash, role_id) VALUES 
(
    'Admin Osaka', 
    'admin@osakacorp.com', 
    'Diretoria de TI', 
    'scrypt:32768:8:1$Vq89M5zX$e4f21685a113e6d24669865c3701a2f60a92d86f7e4b93198f24458f310f898c',
    (SELECT id FROM roles WHERE name = 'ADMIN')
),
(
    'Marcello Manager', 
    'manager@osakacorp.com', 
    'Suporte Nível 2', 
    'scrypt:32768:8:1$Vq89M5zX$e4f21685a113e6d24669865c3701a2f60a92d86f7e4b93198f24458f310f898c',
    (SELECT id FROM roles WHERE name = 'MANAGER')
),
(
    'Tati Technician', 
    'tech@osakacorp.com', 
    'Infraestrutura', 
    'scrypt:32768:8:1$Vq89M5zX$e4f21685a113e6d24669865c3701a2f60a92d86f7e4b93198f24458f310f898c',
    (SELECT id FROM roles WHERE name = 'TECHNICIAN')
),
(
    'Uriel User', 
    'user@osakacorp.com', 
    'Recursos Humanos', 
    'scrypt:32768:8:1$Vq89M5zX$e4f21685a113e6d24669865c3701a2f60a92d86f7e4b93198f24458f310f898c',
    (SELECT id FROM roles WHERE name = 'USER')
);

-- 5. Inserir alguns chamados de exemplo para popular o Dashboard
INSERT INTO tickets (title, description, status, priority, user_id) VALUES 
('Erro no acesso ao ERP', 'Não consigo realizar o login no sistema de vendas.', 'OPEN', 'HIGH', (SELECT id FROM users WHERE email = 'user@osakacorp.com')),
('Troca de mouse', 'Mouse parou de funcionar na mesa 04.', 'IN_PROGRESS', 'LOW', (SELECT id FROM users WHERE email = 'user@osakacorp.com')),
('Configuração de VPN', 'Solicito acesso remoto para home office.', 'CLOSED', 'MEDIUM', (SELECT id FROM users WHERE email = 'user@osakacorp.com'));