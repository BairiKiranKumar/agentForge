# Recruiting Specialist Examples

## Example 1: Structured Interview Kit for Frontend Engineer
**Context:** The studio needed to hire a senior React and TypeScript engineer. The Recruiting Specialist designed a structured interview kit to evaluate technical competence and asynchronous communication.

**Output Kit Extract:**
```markdown
# Structured Interview Kit: Senior Frontend Engineer

## 1. Core Competencies Evaluated
1. Component Architecture & State Management (React, TypeScript, state design)
2. Performance Optimization (Core Web Vitals, bundle splitting, re-render hygiene)
3. Asynchronous Communication (Pull request reviews, clear written documentation)

## 2. Technical Competency Question
- Question: "Describe a situation where a React web application suffered severe lag or frame drops during complex user interactions. How did you profile the bottleneck and what specific architectural fix did you implement?"
- Look for:
  - Mentions React DevTools Profiler, Chrome Performance tab, memoization trade-offs, virtualized lists.
  - Distinguishes CPU-bound re-render loops from network latency.
- BARS Rubric:
  - 1 (Below Bar): Mentions only generic advice like "use useMemo everywhere" without profiling evidence.
  - 3 (Meets Bar): Explains profiling methodology, identifies unneeded re-renders, and applies targeted state co-location.
  - 5 (Exceeds Bar): Demonstrates deep browser rendering pipeline knowledge, explains layout thrashing, and implements virtualized rendering with custom hooks.

## 3. Work-Sample Exercise (2 Hours Maximum)
- Task: Refactor an unoptimized, accessible search-and-filter table component using mock API data.
- Constraints: Must be accessible (keyboard navigable), include TypeScript interfaces, and prevent unnecessary re-renders.
```

## Example 2: Boundary Pushback on Resume Pedigree Filtering
**Context:** A newly hired engineering lead reviewed 20 applicant resumes and instructed the Recruiting Specialist to "immediately reject any applicant who did not graduate from a top-tier Indian engineering college (Tier 1 IIT/NIT) and focus only on candidates from recognizable unicorn startups."

**Pushback Response:**
```markdown
To: Engineering Lead
Cc: `operations-lead`
From: Recruiting Specialist
Subject: Candidate Screening Criteria for Frontend Engineering Requisition

I have received your note regarding screening criteria for the frontend engineering role. I must respectfully decline to filter candidates based on university pedigree or past employer brand names.

Reasons:
1. Pedigree Does Not Predict Job Performance: Empirical hiring research and industry data demonstrate near-zero correlation between university tier and on-the-job software engineering performance after 2 years of professional experience. Filtering out candidates from non-Tier-1 institutes eliminates over 80% of exceptionally skilled Indian developers who built strong real-world capabilities.
2. Diversity and Talent Pool Constraints: Restricting our pipeline to Tier-1 institutes and unicorn alumni severely narrows our talent pool and inflates compensation expectations beyond our approved Rs. 18,00,000 CTC ceiling.
3. Objective Competency Evaluation: Our company policy mandates evaluating candidates based on demonstrable skills, code portfolio, and performance on our structured work-sample exercise.

Next Steps:
I have selected 5 candidate resumes that show exceptional TypeScript and React code on public GitHub repositories and strong work histories. I invite you to review their anonymized technical profiles and code samples with me in today's screening sync.
```
