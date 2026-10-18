# Mandatory project rules

Authority: workspace/Authoring tasks.docx and workspace/Project Summit.pdf. Retain both unchanged. These documents govern all five stages. This digest does not replace them.

Before implementing or producing anything that conflicts with a source requirement, explain the specific conflict and obtain explicit user permission. Permission does not waive external reviewer requirements. Do not silently resolve contradictory requirements.

## Purpose and authorship
Original expert tasks benchmark real, difficult computer work. Prefer distinct failure modes over volume. No artificial handicaps, trivia, obfuscation, withheld necessary context, online task solutions, or model-specific task hunting. Authors personally write instruction.md; AI assistance elsewhere is allowed. Do not generate submission instruction prose for the author.

## Science eligibility
Authentic research, not course exercises or generic coding dressed as science. Five domains, each with four approved fields. Classify by dominant computational content. Author must practise the field. Use real data or disclosed seeded synthetic data. Ground truth must be independent, never from the reference solution; graded results must beat trivial baselines. Explain real/synthetic provenance in difficulty_explanation and ground truth in verification_explanation.

## Bundle and metadata
ZIP contents: instruction.md, task.toml, README.md, environment/Dockerfile, solution/solve.sh, tests/test.sh, tests/Dockerfile; optional authoring/ for provenance/evidence, never mounted. Only allowed root entries. README sections: Difficulty, Reference solution, Verification. Schema 1.4. Top-level artifacts before sections. Name afterquery/<slug>, matching submitted lowercase kebab-case slug, at most three words. Complete required metadata including identity/email, affiliation or exactly Independent Researcher, profile, conflicts or None, domain/field/subfield, category Science, field display-name subcategory, at least one tag, positive expert hours, specific experience and difficulty/solution/verification explanations. research_advisor and referred_by optional. Task authors and keywords mirror metadata.

## Execution and verifier
Agent public network; separate sealed verifier with no network. Only declared artifacts survive agent teardown. No tests or solution references/answers in environment. Solution mounted only for oracle. Preinstall verifier tools, COPY tests to /tests/, create artifact parent directories. Verify contents, not exits/existence/printable strings or agent-writable claims. Every path including crashes writes exactly 0 or 1 to /logs/verifier/reward.txt plus CTRF report; no partial credit. Repeated oracle=1 and nop=0. Reject NaN/infinity; tolerances based on spread of correct methods; enforce all cases/rules, reject constants/averages/shortcuts. No kernel accounting grading or required build-time files in /tmp. Try cheating locally; do not ship cheat/.

## Instructions and environment
Plain prose, no Markdown headings or prescribed step checklist. State goal, all deliverables and absolute paths. End with blank line then exactly: You have N seconds to complete this task. Do not cheat by using online solutions or hints specific to this task. N equals integer agent timeout, at most one trailing newline. Single execution container, no compose/sidecars; install and start services inside each respective container. Dockerfile ends root; optional agent user set in task.toml. Restore executable permissions in scripts for compiled programs. Vendor data or pin immutable sources; deterministic seeds and grading. Pin pip/uv installs with ==, pytest==8.4.1, pytest-json-ctrf==0.3.5. Do not pin apt versions; update then clean apt lists. No FROM --platform pins, allow_internet, or canary GUID markers. OMP/MKL threads <= declared CPUs.

## Limits and workflow
Agent 9000–28800 seconds; verifier <=13500 seconds, no floor. Measure oracle runtime, allow agent several times it within limits. CPUs 1/2/4/8/16; memory MB 1024/2048/4096/8192/16384; storage <=40960 MB. GPUs 0 or selected option exactly 1 with gpu_types=[H100].
Optional advisory idea check; local oracle/nop/Harbor quality review; ZIP submission with matching domain/labels. Gates: structural, AI authorship, similarity, repeated reference verification, 35-criterion agentic quality, anti-cheat, eight-attempt difficulty, trajectory audit, human review. Blocking criteria reject; advisory criteria go to reviewer. Live progress/costs/trajectories, run cancellation. Written rejection reasons; infrastructure failures rerun without penalty. No duplicates or cosmetic rebuilds including own catalogue. $300 USD per approved task, recorded on approval, paid normal cycle; no cycle timing specified.

## Unresolved source contradictions
Rules allow 0–7 solves in eight attempts; difficulty section requires at least one and rejects zero. Do not choose a lower bound without clarification. Dynamic multi-container examples conflict with explicit no-sidecars/compose rules; enforce explicit single-container rule and flag any proposed exception for user permission. Internal acknowledgement is not clarification or external approval.

## Application scope
Stage 1: idea and eligibility. Stage 2: specification. Stage 3: bundle. Stage 4: validation. Stage 5: submission/tracking. Initial app is local and manual; form checks do not prove originality, scientific validity, difficulty, or project acceptance. Do not claim later stages implemented or tests run without evidence.
