# Code Review Guide: What to Look for as a Senior Engineer

> Start with KISS (Keep It Simple) and DRY (Don't Repeat Yourself) — then go deeper.

---

## 1. Correctness & Edge Cases

- Does it actually solve the stated problem, not just the happy path?
- Race conditions, null/undefined states, concurrent access
- Off-by-one errors, empty collections, boundary values
- Error paths — do failures propagate or get silently swallowed?

**Ask:** What's the worst realistic input this will receive?

---

## 2. API & Contract Design

- Are interfaces/props intuitive? Would a new dev understand them without reading the implementation?
- Leaky abstractions — does internal state bleed into the public surface?
- Breaking changes to existing consumers — are they handled or documented?
- Are function signatures honest about what they do? (no hidden side effects)

**Ask:** If I only saw the function signature, would I trust it?

---

## 3. Security (OWASP mindset)

- Injection vectors — XSS, SQL injection, command injection
- Auth/authz gaps — does the new code path respect existing access controls?
- Sensitive data in logs, error messages, or network responses
- User input: is it validated at the boundary before use?

**Ask:** What happens if a malicious user calls this directly?

---

## 4. Performance & Scalability

- O(n²) hiding in innocent-looking nested loops
- Unnecessary re-renders (React: missing memoization, unstable references)
- N+1 query problems (loading related data in a loop)
- Bundle size impact — did a 2KB change pull in a 200KB dependency?

**Ask:** How does this behave with 10x the expected load?

---

## 5. Maintainability

- Single Responsibility — does each function/component do one thing?
- Naming — can you understand intent without reading the body?
- Coupling — how many files break if this one changes?
- Abstraction level is consistent within a module (no mixing low-level and high-level logic)

**Ask:** Could someone unfamiliar with this PR maintain this code in 6 months?

---

## 6. Testability

- Is the new code testable in isolation?
- Are side effects separated from pure logic?
- Did they actually add tests, or defer them?
- Do tests assert behavior, not implementation details?

**Ask:** Can I break this code without breaking a test?

---

## 7. Consistency with the Codebase

- Follows existing patterns — not inventing new conventions mid-project
- Error handling style matches the rest of the project
- File/folder placement makes sense in the current architecture
- If there's a framework or established way to do X, is it used?

**Ask:** Does this feel like it belongs here, or is it a new world?

---

## 8. Operational Readiness

- Logging/observability — can you debug this in production without SSH access?
- Feature flags or rollback strategy for risky changes
- Database migrations: are they reversible?
- What happens during a partial deploy (old consumers, new code)?

**Ask:** If this breaks at 3am, what does the on-call engineer have to work with?

---

## How to Actually Review

**Read the diff twice.**

- **First pass:** Understand intent. What is the author trying to do?
- **Second pass:** Find what's wrong. Look for the gap between intent and implementation.

Most bugs live in that gap.

---

## Quick Mental Checklist

| Category | Key Question |
|---|---|
| Correctness | Does it work for bad inputs, not just good ones? |
| API Design | Is the interface honest and intuitive? |
| Security | Can user input cause harm? |
| Performance | Does it scale, or does it hide an O(n²)? |
| Maintainability | Can someone else own this tomorrow? |
| Testability | Is the behavior actually verified? |
| Consistency | Does it fit the existing codebase? |
| Operations | Can you debug and rollback this in production? |
