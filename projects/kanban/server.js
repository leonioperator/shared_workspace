import express from 'express';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const app = express();
const PORT = 3848;
const DATA_FILE = join(__dirname, 'tasks.json');

app.use(express.json());
app.use(express.static(join(__dirname, 'public')));

function loadTasks() {
  if (!existsSync(DATA_FILE)) {
    const initial = {
      columns: [
        { id: 'backlog', title: 'Backlog', tasks: [] },
        { id: 'todo', title: 'To Do', tasks: [] },
        { id: 'in-progress', title: 'In Progress', tasks: [] },
        { id: 'review', title: 'Review', tasks: [] },
        { id: 'done', title: 'Done', tasks: [] }
      ]
    };
    writeFileSync(DATA_FILE, JSON.stringify(initial, null, 2));
    return initial;
  }
  return JSON.parse(readFileSync(DATA_FILE, 'utf8'));
}

function saveTasks(data) {
  writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

// Get all tasks
app.get('/api/tasks', (req, res) => {
  res.json(loadTasks());
});

// Add task to column
app.post('/api/tasks', (req, res) => {
  const { columnId, title, description, priority, assignee } = req.body;
  const data = loadTasks();
  const col = data.columns.find(c => c.id === columnId);
  if (!col) return res.status(404).json({ error: 'Column not found' });
  
  const task = {
    id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
    title,
    description: description || '',
    priority: priority || 'medium',
    assignee: assignee || '',
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString()
  };
  col.tasks.push(task);
  saveTasks(data);
  res.json(task);
});

// Update task
app.put('/api/tasks/:taskId', (req, res) => {
  const { taskId } = req.params;
  const updates = req.body;
  const data = loadTasks();
  
  for (const col of data.columns) {
    const idx = col.tasks.findIndex(t => t.id === taskId);
    if (idx !== -1) {
      col.tasks[idx] = { ...col.tasks[idx], ...updates, updatedAt: new Date().toISOString() };
      saveTasks(data);
      return res.json(col.tasks[idx]);
    }
  }
  res.status(404).json({ error: 'Task not found' });
});

// Move task between columns
app.post('/api/tasks/:taskId/move', (req, res) => {
  const { taskId } = req.params;
  const { targetColumnId, position } = req.body;
  const data = loadTasks();
  
  let task;
  for (const col of data.columns) {
    const idx = col.tasks.findIndex(t => t.id === taskId);
    if (idx !== -1) {
      task = col.tasks.splice(idx, 1)[0];
      break;
    }
  }
  if (!task) return res.status(404).json({ error: 'Task not found' });
  
  const targetCol = data.columns.find(c => c.id === targetColumnId);
  if (!targetCol) return res.status(404).json({ error: 'Target column not found' });
  
  const pos = position !== undefined ? position : targetCol.tasks.length;
  targetCol.tasks.splice(pos, 0, task);
  saveTasks(data);
  res.json({ ok: true });
});

// Delete task
app.delete('/api/tasks/:taskId', (req, res) => {
  const { taskId } = req.params;
  const data = loadTasks();
  
  for (const col of data.columns) {
    const idx = col.tasks.findIndex(t => t.id === taskId);
    if (idx !== -1) {
      col.tasks.splice(idx, 1);
      saveTasks(data);
      return res.json({ ok: true });
    }
  }
  res.status(404).json({ error: 'Task not found' });
});

app.listen(PORT, () => {
  console.log(`Kanban board running on http://localhost:${PORT}`);
});
