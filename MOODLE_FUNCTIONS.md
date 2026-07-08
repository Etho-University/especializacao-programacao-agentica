# Funções da Moodle REST API para Implantação da Especialização

## Status: Funções testadas no MoodleCloud (universidade-etho)

### LEGENDA
- **✅ Disponível** — existe e aceita chamada
- **⚠️ Precisa adicionar ao serviço** — existe no MoodleCloud, só não está no serviço ainda
- **❌ Bloqueada** — retornou accessexception (pode ser restrita pelo MoodleCloud)

---

### 1. GESTÃO DE CATEGORIAS (Trilhas)

| Função | Status | Finalidade |
|--------|--------|------------|
| `core_course_create_categories` | ✅ Disponível | Criar categorias (trilhas: Fundamentos, Avançado, etc.) |
| `core_course_get_categories` | ⚠️ Precisa adicionar | Listar categorias |
| `core_course_delete_courses` | ✅ Disponível | Deletar cursos |

### 2. GESTÃO DE CURSOS

| Função | Status | Finalidade |
|--------|--------|------------|
| `core_course_create_courses` | ✅ Disponível | Criar os 16 cursos (ETHAGT01 a 16) |
| `core_course_get_courses` | ⚠️ Precisa adicionar | Listar cursos |
| `core_course_duplicate_course` | ✅ Disponível | Duplicar cursos (template) |
| `core_course_set_custom_fields` | ✅ Disponível | Campos customizados nos cursos |
| `core_course_update_courses` | ❌ Bloqueada | Atualizar cursos |
| `core_course_edit_module` | ❌ Bloqueada | Editar atividades |
| `core_course_edit_section` | ❌ Bloqueada | Editar seções |

### 3. CONTEÚDO (Apostilas, Páginas, Links, Recursos)

| Função | Status | Finalidade |
|--------|--------|------------|
| `mod_resource_add_instance` | ✅ Disponível | Adicionar arquivos/apostilas |
| `mod_resource_update_instance` | ✅ Disponível | Atualizar arquivos |
| `mod_page_add_instance` | ✅ Disponível | Adicionar páginas HTML |
| `mod_page_update_instance` | ✅ Disponível | Atualizar páginas |
| `mod_url_add_instance` | ✅ Disponível | Adicionar links externos |
| `mod_url_update_instance` | ✅ Disponível | Atualizar links |
| `mod_lti_add_instance` | ✅ Disponível | Integração LTI |
| `mod_lti_update_instance` | ✅ Disponível | Atualizar LTI |
| `core_files_upload` | ❌ Bloqueada | Upload de arquivos |

### 4. ATIVIDADES AVALIATIVAS (Projetos, Exercícios, Provas)

| Função | Status | Finalidade |
|--------|--------|------------|
| `mod_assign_create_assignments` | ✅ Disponível | Criar projetos e exercícios (com rubricas, prazos) |
| `mod_assign_get_assignments` | ⚠️ Precisa adicionar | Listar tarefas |
| `mod_assign_get_submission_status` | ⚠️ Precisa adicionar | Status de entrega |
| `mod_assign_save_grade` | ❌ Bloqueada | Lançar notas |
| `mod_assign_save_submission` | ❌ Bloqueada | Submeter entrega |
| `mod_quiz_add_instance` | ✅ Disponível | Criar provas modulares |
| `mod_quiz_update_instance` | ✅ Disponível | Atualizar provas |

### 5. FÓRUNS (Avisos, Discussão)

| Função | Status | Finalidade |
|--------|--------|------------|
| `mod_forum_add_instance` | ✅ Disponível | Criar fóruns de avisos/discussão |
| `mod_forum_update_instance` | ✅ Disponível | Atualizar fóruns |
| `mod_forum_get_forums_by_courses` | ⚠️ Precisa adicionar | Listar fóruns |

### 6. MATRÍCULAS E USUÁRIOS

| Função | Status | Finalidade |
|--------|--------|------------|
| `core_enrol_manual_enrol_users` | ✅ Disponível | Matricular alunos em cursos |
| `core_enrol_get_users_courses` | ✅ Já está no serviço | Cursos do usuário |
| `core_enrol_get_enrolled_users` | ⚠️ Precisa adicionar | Listar matriculados |
| `core_user_create_users` | ❌ Bloqueada | Criar usuários |
| `core_user_get_users` | ⚠️ Precisa adicionar | Buscar usuários |
| `core_role_assign_roles` | ❌ Bloqueada | Atribuir papéis |
| `core_role_unassign_roles` | ❌ Bloqueada | Remover papéis |

### 7. NOTAS (Gradebook - 4 Pilares)

| Função | Status | Finalidade |
|--------|--------|------------|
| `core_grade_create_categories` | ✅ Disponível | Criar categorias de nota (40/30/20/10) |
| `core_grade_update_grades` | ✅ Disponível | Lançar/atualizar notas |
| `core_grade_get_grade_items` | ✅ Disponível | Consultar itens de nota |
| `gradereport_overview_get_course_grades` | ⚠️ Precisa adicionar | Relatório de notas |
| `gradereport_user_get_grade_items` | ⚠️ Precisa adicionar | Notas por usuário |

### 8. PROGRESSÃO E COMPLETUDE

| Função | Status | Finalidade |
|--------|--------|------------|
| `core_completion_update_activity_completion_status` | ✅ Disponível | Marcar atividade concluída |
| `core_completion_get_activities_completion_status` | ⚠️ Precisa adicionar | Status de completude |

---

## Mínimo necessário para implantação completa

Se quiser adicionar só o essencial por enquanto, comece por estas:

```
# Leitura (para o MCP funcionar)
core_course_get_categories
core_course_get_courses
core_enrol_get_enrolled_users
mod_assign_get_assignments
mod_assign_get_submission_status
mod_forum_get_forums_by_courses
gradereport_overview_get_course_grades
gradereport_user_get_grade_items
core_completion_get_activities_completion_status
core_user_get_users
core_files_get_files

# Escrita (para implantar conteúdo)
core_course_create_courses
core_course_create_categories
core_course_duplicate_course
core_course_set_custom_fields
core_enrol_manual_enrol_users
core_grade_create_categories
core_grade_update_grades
core_grade_get_grade_items
core_completion_update_activ
mod_resource_add_instance
mod_resource_update_instance
mod_page_add_instance
mod_page_update_instance
mod_url_add_instance
mod_url_update_instance
mod_forum_add_instance
mod_forum_update_instance
mod_quiz_add_instance
mod_quiz_update_instance
```
