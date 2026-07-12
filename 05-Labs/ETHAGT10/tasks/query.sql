-- Schema do banco de dados da aplicação Etho
-- IMPORTANTE: este script deve ser executado como admin

-- Tabela de usuários
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PROBLEMA: sem índice no email — queries de login ficam lentas com muitos usuários
-- PROBLEMA: sem índice no role — queries de auditoria ficam lentas

-- Tabela de sessões
CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    token TEXT NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PROBLEMA: foreign key para users mas sem ON DELETE CASCADE
-- Sessões órfãs ficam no banco quando usuário é deletado

-- Tabela de logs
CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    action VARCHAR(100) NOT NULL,
    details TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PROBLEMA: sem partitioning — tabela vai crescer indefinidamente
-- PROBLEMA: sem índice em created_at — queries de relatório lentas

-- Tabela de configurações
CREATE TABLE settings (
    key VARCHAR(100) PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dados iniciais (HARDCODED)
INSERT INTO settings (key, value) VALUES ('max_upload_size', '10485760');
INSERT INTO settings (key, value) VALUES ('session_timeout', '3600');
INSERT INTO settings (key, value) VALUES ('enable_2fa', 'false');
