CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS tasks (
  id          SERIAL PRIMARY KEY,
  source      TEXT NOT NULL,
  agent       TEXT,
  payload     JSONB NOT NULL DEFAULT '{}',
  status      TEXT NOT NULL DEFAULT 'pending',
  result      JSONB,
  error       TEXT,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS leads (
  id          SERIAL PRIMARY KEY,
  name        TEXT,
  email       TEXT,
  company     TEXT,
  score       INT,
  category    TEXT,
  notes       TEXT,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS emails (
  id              SERIAL PRIMARY KEY,
  sender          TEXT,
  subject         TEXT,
  body            TEXT,
  category        TEXT,
  suggested_reply TEXT,
  status          TEXT NOT NULL DEFAULT 'new',
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS approvals (
  id          SERIAL PRIMARY KEY,
  task_id     INT REFERENCES tasks(id) ON DELETE CASCADE,
  action      TEXT NOT NULL,
  details     JSONB NOT NULL DEFAULT '{}',
  status      TEXT NOT NULL DEFAULT 'pending',
  decided_at  TIMESTAMPTZ,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS agent_memory (
  id          SERIAL PRIMARY KEY,
  session_id  TEXT NOT NULL,
  role        TEXT NOT NULL,
  content     TEXT NOT NULL,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_memory_session ON agent_memory(session_id, created_at);

CREATE TABLE IF NOT EXISTS documents (
  id          SERIAL PRIMARY KEY,
  source      TEXT,
  content     TEXT NOT NULL,
  embedding   vector(1536),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_documents_embedding
  ON documents USING hnsw (embedding vector_cosine_ops);
