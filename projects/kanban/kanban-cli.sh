#!/bin/bash
# Kanban CLI — task management helper
# Usage:
#   kanban list [column]           — list tasks (optional: filter by column)
#   kanban add <column> <title> [desc] [priority] [assignee] — add task
#   kanban move <task_id> <target_column> — move task to column
#   kanban done <task_id>          — shortcut: move to done
#   kanban review <task_id> [msg]  — move to review (blocked, needs human input)
#   kanban find <search_term>      — find task by title substring
#   kanban delete <task_id>        — delete task
#   kanban archive                 — archive done tasks older than 24h
#
# Columns: backlog, todo, in-progress, review, done, archive
# Review = agent elakadt, emberi beavatkozás kell (Telegram alert küldés)

API="http://localhost:3848/api"

case "$1" in
  list)
    FILTER="$2"
    curl -s "$API/tasks" | python3 -c "
import sys,json
d=json.load(sys.stdin)
filt='$FILTER'
for c in d['columns']:
    if filt and c['id'] != filt:
        continue
    if c['id'] == 'archive' and not filt:
        continue
    if c['tasks']:
        print(f\"\\n[{c['title']}] ({len(c['tasks'])})\")
        for t in c['tasks']:
            p = t.get('priority','?')
            a = t.get('assignee','')
            print(f\"  {t['id']} | {p.upper():6} | {t['title']} {('('+a+')') if a else ''}\" )
"
    ;;
  add)
    COL="$2"; TITLE="$3"; DESC="${4:-}"; PRIO="${5:-medium}"; ASSIGN="${6:-Leoni}"
    curl -s -X POST "$API/tasks" -H 'Content-Type: application/json' \
      -d "{\"columnId\":\"$COL\",\"title\":\"$TITLE\",\"description\":\"$DESC\",\"priority\":\"$PRIO\",\"assignee\":\"$ASSIGN\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Created: {d[\"id\"]} | {d[\"title\"]}')"
    ;;
  move)
    TASK_ID="$2"; TARGET="$3"
    curl -s -X POST "$API/tasks/$TASK_ID/move" -H 'Content-Type: application/json' \
      -d "{\"targetColumnId\":\"$TARGET\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print('Moved OK' if d.get('ok') else f'Error: {d}')"
    ;;
  done)
    TASK_ID="$2"
    curl -s -X POST "$API/tasks/$TASK_ID/move" -H 'Content-Type: application/json' \
      -d '{"targetColumnId":"done"}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Moved to Done' if d.get('ok') else f'Error: {d}')"
    ;;
  review)
    TASK_ID="$2"; MSG="${3:-Agent elakadt, emberi beavatkozás szükséges}"
    curl -s -X POST "$API/tasks/$TASK_ID/move" -H 'Content-Type: application/json' \
      -d '{"targetColumnId":"review"}' | python3 -c "import sys,json; d=json.load(sys.stdin); print('Moved to Review' if d.get('ok') else f'Error: {d}')"
    # Note: Telegram alert should be sent by the calling agent
    echo "⚠️  REVIEW: $MSG (send Telegram alert!)"
    ;;
  find)
    SEARCH="$2"
    curl -s "$API/tasks" | python3 -c "
import sys,json
d=json.load(sys.stdin)
s='$SEARCH'.lower()
for c in d['columns']:
    for t in c['tasks']:
        if s in t['title'].lower():
            print(f\"{t['id']} | {c['title']:12} | {t['title']}\")
"
    ;;
  delete)
    TASK_ID="$2"
    curl -s -X DELETE "$API/tasks/$TASK_ID" | python3 -c "import sys,json; d=json.load(sys.stdin); print('Deleted' if d.get('ok') else f'Error: {d}')"
    ;;
  archive)
    curl -s -X POST "$API/tasks/archive" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Archived: {d[\"archived\"]} tasks (total in archive: {d[\"total_archive\"]})')"
    ;;
  *)
    echo "Usage: kanban {list|add|move|done|review|find|delete|archive} [args]"
    echo "Columns: backlog, todo, in-progress, review, done, archive"
    echo ""
    echo "Workflow:"
    echo "  backlog → todo → in-progress → done (→ archive after 24h)"
    echo "  in-progress → review (blocked, Telegram alert) → in-progress"
    ;;
esac
