# Weeks 5–6: Informed Search (A*) and Constraint Satisfaction Problems

**Self-directed learning pack — no live lecture for these two weeks.**

Your lecturer is away for the next two weeks. This repo replaces the lecture:
read the guides, work through the two worked examples, then complete the
assignment during your normal Tuesday/Thursday class slots. A tutor/TA may
be present in the room to answer logistics questions, but the technical
content is fully self-contained here.

## What you need to do, in order

1. Clone or fork this repo (see **Getting the repo** below).
2. Read `01_Informed_Search_A_Star/guide.md`, then work through
   `01_Informed_Search_A_Star/worked_example.md`.
3. Read `02_CSP/guide.md`, then work through `02_CSP/worked_example.md`.
4. Read `03_Test_Case_Design/mindmap.md` and `training_guide.md` — this
   teaches you how to design the 3 test cases the assignment requires.
5. Do the assignment: `assignments/assignment_wk5_6.md`.
6. Submit by pushing your work and opening a pull request (see
   **Submission** below) before the deadline stated in the assignment brief.

## Schedule (Tue / Thu class slots)

| Session | Focus | What to bring / submit |
|---|---|---|
| Week 5, Tue | Read A* guide + worked example. Start `astar_grid.py`. | — |
| Week 5, Thu | Finish A* implementation + 3 test cases for A*. | Push A* work-in-progress commit. |
| Week 6, Tue | Read CSP guide + worked example. Start `csp_map_coloring.py`. | — |
| Week 6, Thu | Finish CSP implementation + 3 test cases for CSP. Final submission. | Open your Pull Request. |

Work at your own pace within this — the important thing is that both parts
are submitted by the final deadline in `assignments/assignment_wk5_6.md`.

## Repo map

```
Wk5_6/
├── README.md                          <- you are here
├── 01_Informed_Search_A_Star/
│   ├── guide.md                       <- concepts + step-by-step method
│   ├── worked_example.md              <- Sample 1: fully solved by hand
│   ├── starter_code/                  <- your assignment starts here
│   └── solution/                      <- full code for the worked example only
├── 02_CSP/
│   ├── guide.md
│   ├── worked_example.md              <- Sample 2: fully solved by hand
│   ├── starter_code/
│   └── solution/
├── 03_Test_Case_Design/
│   ├── mindmap.md                     <- how to think about test coverage
│   └── training_guide.md              <- worked demo: deriving 3 test cases
├── assignments/
│   └── assignment_wk5_6.md            <- the actual assignment brief
├── resources/
│   └── reading_links.md               <- external reading, videos, references
├── requirements.txt
└── .gitignore
```

## Recommended setup for the lecturer

Two ways to run this as a self-guided exercise while you're away. Both use
the same repo content — they differ in how students get their copy and how
you see their progress.

**Option A — GitHub Classroom (recommended).** Free for educators, and
built exactly for this situation: unsupervised, individually-graded
exercises with a hard deadline.

1. Push this repo to GitHub, then mark it a **template repository**
   (Settings → check "Template repository").
2. Go to [classroom.github.com](https://classroom.github.com), create a
   classroom for your course, and create a new **individual assignment**
   pointing at this template repo.
3. Turn on **autograding** — this repo already ships
   `.github/workflows/tests.yml`, which runs both pytest suites on every
   push. Classroom can surface those same results as pass/fail checks per
   student, or you can just point students at the "Actions" tab of their
   own repo.
4. Share the assignment's join link with students (post it wherever you'd
   normally post the class link). Each student gets their own **private**
   repo cloned from this template — no risk of students seeing each
   other's solutions, and no git-workflow knowledge required beyond
   `git clone`, `git add`, `git commit`, `git push`.
5. You get a single dashboard showing every student's repo, last commit
   time, and (with autograding on) their test pass/fail status — checkable
   from anywhere, including while travelling.

**Option B — plain fork + Pull Request (zero setup, works today).** This is
what the rest of this README documents below. Push the repo to GitHub,
leave it public, and students fork it and submit via PR. No Classroom
account needed, but forks are public by default (students could see each
other's solutions if they go looking), and you'll be reading N pull
requests by hand instead of one dashboard.

If you have 15–20 minutes before you leave, Option A is worth it,
especially for a class the size of a normal cohort. If you're pressed for
time, Option B works immediately with what's already in this repo.

## Getting the repo (student instructions)

```bash
# 1. Fork this repo on GitHub (use the Fork button), then clone YOUR fork:
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Create your working branch
git checkout -b wk5-6-<your-student-id>

# 3. Set up Python environment
python -m venv venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 4. Run the starter code / tests as you work
python 01_Informed_Search_A_Star/starter_code/astar_grid.py
pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v
```

## Submission

1. Commit your completed code (starter files with TODOs filled in, plus your
   3 test cases per problem) to your branch.
2. Push your branch to your fork.
3. Open a Pull Request from your fork/branch back to the original repo.
4. Submit the PR link as instructed in `assignments/assignment_wk5_6.md`
   before the deadline. Late PRs are timestamped automatically by GitHub.

## Getting unstuck

- Re-read the relevant `guide.md` and `worked_example.md` first — most
  questions are answered there.
- Check `resources/reading_links.md` for external explanations and videos.
- Post your question in the class channel/forum so classmates and the TA
  can help — this is normal and encouraged during self-study weeks.
