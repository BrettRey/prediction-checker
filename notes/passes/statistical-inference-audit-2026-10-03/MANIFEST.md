# Statistical inference audit run, 2026-10-03
<!-- SUMMARY: independent inference/dependence audit of the EJW draft (Codex gpt-6-astra, xhigh, read-only) · status: complete (findings pending) · updated: 2026-10-03 -->

- Pass: statistical-inference-audit (passes/registry/statistical-inference-audit.yaml); checks adapted to a four-point time series with an externally calibrated error scale (see PROMPT.md)
- Auditor: Codex CLI v0.159.2, model gpt-6-astra, reasoning effort xhigh; locked-down command as for the numbers audit (env -i, read-only sandbox, no approvals, user config ignored, ephemeral)
- Dispatching session: Claude Opus 5.5 (designed the analysis and wrote the prose under audit)
- Manuscript: commit 3046dc3; main.txt sha256 aae2c3ab98c49265e642dba3cda57ddf209c4cf89acbdb4f7b644c8f3a2a0b54
- Prompt sha256: 0ce728e76bf6af04d8cb24e19088ebf8052b74b65938a5a455f2f05ad8466ce8
- Raw output: codex-stdout.txt and codex-stderr.txt, saved by the parent, gitignored
- Output sha256 (codex-stdout.txt): 7860a403412cad8a5b4645c4f604d3c85387854eceed0b4337f326d0fd0534be; saved verbatim as notes/passes/2026-10-03-statistical-inference-audit.md
