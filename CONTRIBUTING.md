# Contributing to Awesome Claude Desktop Extensions

Thanks for your interest in contributing!

## How to Contribute

- Add new `.dxt` tools or resources under the appropriate category
- Add manifest.json to your mcp server, see example below
- Fix typos or improve descriptions
- Keep the list alphabetically sorted within each category
- Ensure links are valid and point to useful content

### example

#### uvx example

- [servers/blender-mcp](./servers/blender-mcp)

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