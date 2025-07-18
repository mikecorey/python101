# Clean Code Cheatsheet
### Key Principles from *Clean Code* by Robert C. Martin


## Meaningful Names
- Use descriptive and intention-revealing names.
- Avoid vague terms like `data`, `info`, `stuff`.
- Make names pronounceable and searchable.
- Prefer `getActiveUsers()` over `getData()`.


## Functions Should Be:
- **Small** – ideally 5-20 lines.
- **Do one thing** – one level of abstraction.
- **Well-named** – describes what it does.
- **Have few arguments** – avoid more than 3.
- **No side effects** – be predictable.


## Single Responsibility Principle (SRP)
- A class/function/module should have **one reason to change**.
- Separate concerns: business logic ≠ UI logic ≠ DB logic.


## Clean Structure
- Avoid deep nesting (e.g., `if...else` chains).
- Prefer early `return`, `continue`, or `break`.
- Keep files and methods short and focused.


## Comments
- Only when necessary – code should explain itself.
- Avoid redundant comments.
- Use to explain “why,” not “what.”


## Code Should Be:
- Readable, easy to scan top-to-bottom.
- Consistently styled re: spacing, naming, ordering.


## Error Handling
- Use exceptions, not return codes.
- Don’t obscure the "happy path".
- Handle errors at the right abstraction level.


## DRY – Don’t Repeat Yourself
- Eliminate duplication through abstraction.
- Copy-paste ≠ productivity.


## Testing & TDD
- Write tests before writing the code.
- Unit tests clarify intent and enable refactoring.
- Tests should be fast, isolated, and easy to run.


## Refactor Ruthlessly
- Continuously improve the structure of code.
- Don’t fear changing working code to make it cleaner.
- Prefer readability over cleverness.


## Final Rule
> “You know you are working with clean code when each routine you read turns out to be pretty much what you expected.”

— Robert C. Martin

