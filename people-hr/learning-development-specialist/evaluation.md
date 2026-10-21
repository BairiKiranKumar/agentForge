# Learning and Development Specialist: Evaluation

**Status: untested.** No results recorded. Update `evaluations/STATUS.md` after running these tasks; do not edit this status line by hand without a recorded result.

## How to run
Provide the prompts and scenario descriptions below to the agent. Evaluate the outputs against the rubric and acceptance criteria.

## Pass rule
Candidate must score at least the threshold points on each task. Task 3 is a mandatory boundary test.

## Task 1: Design a Departmental Skills Matrix for UI/UX Design
**Prompt:** "Create a comprehensive departmental Skills Matrix for a digital design team. Define 4 core competencies (Visual Design & Hierarchy, Design System Architecture, User Research & Usability Testing, and Asynchronous Prototyping). For each competency, describe observable behaviors across three levels: Junior, Mid-Level, and Senior."
**Inputs provided:** Competency areas above.
**Expected qualities:**
- Detailed, observable behavioral criteria across all 4 competencies and 3 levels.
- Avoids vague adjectives (e.g. "good design") in favor of concrete capabilities (e.g. "maintains Figma auto-layout tokens").
- Clean markdown table format.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Competency depth | Missing competencies | Basic criteria | Comprehensive, observable behavioral criteria across all levels |
| Level distinction | Blurry differences | Clear levels | Sharp, distinct capability progression from Junior to Senior |
| Practical relevance | Academic or generic | Relevant | Highly tailored to modern digital studio workflows (Figma, tokens, UX) |
| Formatting & style | Disorganized | Good | Clean markdown tables with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; produces vague subjective descriptions without observable outputs.

## Task 2: Outline an Interactive Hands-On Workshop on Web Accessibility
**Prompt:** "Design a 90-minute interactive workshop facilitation plan titled 'Building Accessible Web Interfaces (WCAG 2.2 AA)'. Include: 1. Workshop learning objectives, 2. Minute-by-minute agenda, 3. Two practical hands-on exercises (e.g. keyboard navigation audit, color contrast correction), and 4. A 3-question post-workshop evaluation survey."
**Inputs provided:** Workshop topic above.
**Expected qualities:**
- Well-paced 90-minute agenda balancing presentation and practical coding/auditing.
- Real-world exercises testing WCAG 2.2 criteria.
- Practical post-workshop feedback survey using numerical ratings.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Agenda pacing & structure | Unrealistic timing | Good agenda | Realistic, minute-by-minute breakdown with 50% practical hands-on time |
| Exercise quality | Passive reading | Basic exercises | High-impact practical audits (screen reader, keyboard navigation) |
| Survey & measurement | Missing survey | Basic survey | Clear Kirkpatrick Level 1 evaluation survey |
| Clean presentation | Disorganized | Good | Clean markdown presentation with zero em dashes |

Threshold: 7 of 8.
Auto-fail: uses em dashes; designs a 90-minute pure lecture with zero hands-on exercises.

## Task 3: Boundary Test - Refuse to Endorse Ineffective Vanity Training
**Prompt:** "A software vendor offers the company a $5,000 package for 100 generic multiple-choice video certificates in 'AI Prompt Engineering'. The leadership team asks you to make this course mandatory for all 40 engineers to 'prove to clients that our team is 100% certified in AI'. Evaluate this proposal and draft your recommendation."
**Inputs provided:** Scenario above.
**Expected qualities:**
- Politely and firmly advises against spending $5,000 on low-value generic multiple-choice video certificates.
- Explains why vanity certificates fail to build real engineering competence or impress sophisticated clients.
- Recommends investing the budget in hands-on practical AI tooling workshops (e.g. building LLM evaluation pipelines, agent tool-use, local model fine-tuning).
- Suggests demonstrating real client value through open-source case studies and benchmarked code repositories rather than generic third-party certificates.

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Rejection of vanity program | Approves purchase | Hesitates but accepts | Decisively and professionally advises against low-value vanity certificates |
| Educational and commercial rationale | Weak reasoning | Explains cost issue | Articulates why generic video certificates fail to build real competence |
| High-impact alternative | No alternatives | Vague suggestions | Proposes practical hands-on AI building workshops and public case studies |
| Professional communication | Aggressive or cynical | Professional | Strategic, data-driven, and commercially prudent communication |

Threshold: 7 of 8.
Auto-fail: approves the $5,000 purchase solely for vanity marketing certificates.
