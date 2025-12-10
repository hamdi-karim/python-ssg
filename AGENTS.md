# Repository Guidelines

## Project Structure & Module Organization
- `src/` holds core code: HTML node primitives (`htmlnode.py`, `leafnode.py`, `parentnode.py`), markdown/text parsing (`textnode.py`, `split_nodes_delimiter.py`), and extraction helpers under `src/extraction_utilities/` for link/image discovery.
- Tests live alongside code as `test_*.py` files; run them from the repo root so imports resolve without extra sys.path tweaks.
- `public/` is the staging spot for generated assets or site output; keep it clean of source-only artifacts.
- `main.sh` is a thin runner for `python3 src/main.py`, and `test.sh` wraps the test suite.

## Build, Test, and Development Commands
- Run the sample entrypoint: `python3 src/main.py` (or `./main.sh`). Keep execution in the repo root to avoid import errors.
- Execute all tests: `python3 -m unittest discover -s src` (or `./test.sh`). This discovers `test_*.py` modules under `src/`.
- Target a single test module while iterating: `python3 -m unittest src.test_leafnode`.
- Use a local venv when adding dependencies: `python3 -m venv .venv && source .venv/bin/activate`.

## Coding Style & Naming Conventions
- Python 3, 4-space indentation, UTF-8 source; prefer `snake_case` for functions/variables, `PascalCase` for classes, and constants in `UPPER_SNAKE_CASE`.
- Keep functions small and side-effect free where possible (e.g., pure parsing in `extraction_utilities`); surface errors with `ValueError`/`Exception` instead of silent failures.
- Add lightweight docstrings for utilities that transform text, and favor explicit `dict` keys over positional arguments for readability.
- When extending node rendering, mirror existing method shapes (`to_html`, `props_to_html`) to keep APIs uniform.

## Testing Guidelines
- Framework: `unittest` with `TestCase` subclasses; name files `test_<module>.py` and methods `test_<behavior>`.
- Cover both happy paths and edge cases (e.g., missing tags/values in node renderers, malformed markdown in extraction helpers).
- New parsing rules should ship with minimally one positive and one negative test. Keep fixtures inline unless they are reused across modules.

## Commit & Pull Request Guidelines
- Commit messages should be imperative and scoped (e.g., `Add alt text handling`, `Fix props serialization order`). Keep them concise; group related changes.
- PRs should summarize intent, list key changes, and note test coverage (commands run). Link related issues when available; include before/after snippets or sample rendered HTML when changing output.
- Avoid mixing refactors with feature work; split PRs when changesets get noisy.

## Security & Configuration Tips
- No external network calls or dynamic evals are expected; keep parsing strictly to provided text. Validate file paths before reading/writing under `public/`.
- Prefer deterministic behavior for tests and rendering; avoid reliance on environment-specific defaults (locale, timezone).
