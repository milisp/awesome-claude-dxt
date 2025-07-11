# Contributing to Awesome Claude Desktop Extensions

Thanks for your interest in contributing!

## How to Contribute

### Simple way

if your mcp server use npx or uvx, just create a `manifest.json` at your repo root
and test then list at this repo

- servers/{owner}/{repo}/manifest.json
- Create a PR to this repo list by category

### Full way

- Add new `.dxt` tools or resources under the appropriate category
- Add manifest.json to your mcp server, see example below
- Fix typos or improve descriptions
- Keep the list alphabetically sorted within each category
- Ensure links are valid and point to useful content

### example

#### uvx example

##### Step

1. clone your mcp server to folder [servers](./servers) (uvx or npx can skip this step)
  - create a folder owner/repo or author/mcp-server
2. create manifest.json in the folder
3. install dxt

```sh
npm install -g @anthropic-ai/dxt
```

4. pack dxt

```sh
dxt pack
```

- [servers/ahujasid/blender-mcp](./servers/ahujasid/blender-mcp)

`manifest.json`

```json
{
  "dxt_version": "0.1",
  "name": "blender-mcp",
  "display_name": "Blender",
  "version": "1.2",
  "description": "Blender Model Context Protocol Integration",
  "author": {
    "name": "ahujasid"
  },
  "server": {
    "type": "python",
    "entry_point": "main.py",
    "mcp_config": {
      "command": "uvx",
      "args": [
        "blender-mcp@1.2"
      ]
    }
  },
  "license": "MIT"
}
```

## Pull Request Checklist

- Your entry includes a short description
- You tested the link(s)
- You didn’t break formatting

---

By contributing, you agree to follow the project's open source license and code of conduct.