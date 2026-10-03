# Numbers audit run, 2026-10-03
<!-- SUMMARY: second-model numbers audit of the EJW draft (Codex, read-only); raw output saved by the parent · status: complete (findings pending) · updated: 2026-10-03 -->

- Pass: numbers-audit (passes/registry/numbers-audit.yaml)
- Run 1 (stopped by Brett's instruction): Codex CLI v0.159.2 via tools/codex/bin/codex-readonly; the wrapper ignores user config, so it ran Codex's built-in default model gpt-6.1-sol with reasoning effort unset (header "none"; the model isn't in the local catalog, so Codex's fallback is no extra reasoning). Partial log in run1-effort-unset/.
- Run 2 (the audit of record): the wrapper's exact locked-down command (env -i, --sandbox read-only, --ask-for-approval never, --ignore-user-config, --strict-config, --ephemeral) plus -c model="gpt-6-astra" -c model_reasoning_effort="xhigh"; header confirms model gpt-6-astra, effort xhigh. Session 01a102f6-8a63-7242-8e5a-d74d54945857.
- Dispatching session: Claude Opus 5.5 (wrote the scripts and prose under audit)
- Manuscript: main.pdf built from commit 8b1903f; main.pdf sha256 df2a0a33d7610a86abbe32d50a35a8b1d5545b5d599f34068c087f094d2d9f86
- Rendered text audited: main.txt, sha256 0580a19528d52035fc10e9c85dafc05db5f18e184b247010b1f7095fb00eb946
- Prompt: PROMPT.md, sha256 fe16f116fd78b09f24fbf6856e85b1bc580f0682a8d7ab118a33b179355b2dbc
- Raw output: codex-stdout.txt (final message) and codex-stderr.txt (session log), saved by the parent; gitignored, because the session log copies the full text of every file Codex opens, including copyrighted papers
- Output sha256 (codex-stdout.txt): bfbf8ed6c12881c83f0d91fad6b933b8af47256cdb5d70d4510bc74f45123d70; saved verbatim as notes/passes/2026-10-03-numbers-audit.md
