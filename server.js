const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(express.static('public'));

const JOBS_FILE = './jobs.json';

// Read all jobs
app.get('/api/jobs', (req, res) => {
  const jobs = JSON.parse(fs.readFileSync(JOBS_FILE, 'utf8') || '[]');
  res.json(jobs);
});

// Post a new job
app.post('/api/jobs', (req, res) => {
  const job = req.body;
  job.duration = `${req.body.durationValue || 1} ${req.body.durationUnit || 'days'}`;
  const jobs = JSON.parse(fs.readFileSync(JOBS_FILE, 'utf8') || '[]');
  job.id = Date.now(); // simple unique ID
  jobs.push(job);
  fs.writeFileSync(JOBS_FILE, JSON.stringify(jobs, null, 2));
  res.json({ message: 'Task Added successfully', job });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
