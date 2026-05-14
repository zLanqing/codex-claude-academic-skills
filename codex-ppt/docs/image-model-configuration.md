# Image Model Configuration

Use this reference only when the local API/CLI fallback is needed and the runtime config is missing or must be changed.

Do not manually parse `.env`. The fallback CLI loads the shared config automatically. Run the fallback command first, then use this document only if the CLI reports missing or invalid configuration.

Ask the user to configure or update settings only when:

- The fallback CLI reports missing `OPENAI_API_KEY`.
- The user explicitly wants to change API key, base URL, or model.
- A real API call fails with authentication, permission, base URL, or model-not-found errors.

## When Configuration Is Needed

Configure image API access only for API/CLI fallback image generation.

Typical cases:

- Codex is using a third-party API or OpenAI-compatible proxy for image generation.
- The skill is being used from Claude Code, OpenClaw, Hermes Agent, or another agent without Codex's built-in image tool.

If Codex is being used through a GPT subscription and the built-in image tool is available, do not ask the user to configure `gpt-image-2`.

## Required And Optional Values

- `OPENAI_API_KEY` is required for real API/CLI fallback calls.
- `OPENAI_BASE_URL` is optional. When it is unset, the CLI uses the official OpenAI API. When it is set, the CLI treats the request as a third-party OpenAI-compatible proxy request.
- `CODEX_PPT_IMAGE_MODEL` is optional. The default is `gpt-image-2`. Use a custom value only when the proxy provider requires one.

Configure provided API settings with `scripts/codex_ppt_runtime.py config --api-key`.

## Official OpenAI Example

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py config \
  --api-key "your-api-key" \
  --model gpt-image-2
```

## Third-Party Proxy Example

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py config \
  --api-key "your-api-key" \
  --base-url "https://your-openai-compatible-endpoint/v1" \
  --model openai/gpt-image-2
```

Replace `--base-url` and `--model` with the values from the proxy provider.

## Runtime Config

The config is written to:

```text
~/.codex-ppt-skill/.env
```

The file is created with mode `0600`. It is shared by Codex, Claude Code, OpenClaw, Hermes Agent, and other local agents.

Process environment variables override `.env` values. A command-line `--model` overrides `CODEX_PPT_IMAGE_MODEL` for that single command.
