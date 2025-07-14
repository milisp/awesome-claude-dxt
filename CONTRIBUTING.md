# Contributing to Awesome Claude Desktop Extensions

Thank you for your interest in contributing!

## How to Contribute

- Add your DXT server/tool to the list
- [Report an issue](https://github.com/milisp/awesome-claude-dxt/issues)
- Translate README.md into your familiar language 

---

## Quick Contribution (Recommended)

If your MCP server uses `npx` or `uvx`, you can contribute in a few simple steps:

1. **Create a `manifest.json`**  
   Place it at the root of your repository.
2. **Test your server**  
   Make sure it works as expected.
3. **Add your server to this repo**  
   (Option)
   Place your manifest at:  
   `servers/{owner}/{repo}/manifest.json`
4. **Open a Pull Request**  
   Add your server under the appropriate category in the list.

---

## Full Contribution Guide

If you want to add new DXT tools, resources, or make improvements:

- Add new `.dxt` tools or resources under the correct category.
- Add a `manifest.json` to your MCP server (see example below).
- Fix typos or improve descriptions.
- Keep the list alphabetically sorted within each category.
- Ensure all links are valid and useful.

---

## Example: Python (uvx) Server

**Step-by-step:**

1. Clone your MCP server into the `servers` folder (skip if using `npx` or `uvx`).
   - Folder structure: `servers/{owner}/{repo}` or `servers/{author}/{mcp-server}`
2. Create a `manifest.json` in your server folder.
3. Install DXT CLI:
   ```sh
   npm install -g @anthropic-ai/dxt
   ```
4. Pack your DXT:
   ```sh
   dxt pack
   ```
5. Add your server to the list, e.g.:
   - [servers/ahujasid/blender-mcp](./servers/ahujasid/blender-mcp)

**Sample `manifest.json`:**
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

---

## Pull Request Checklist

- [ ] Your entry includes a short description
- [ ] You tested the link(s)
- [ ] You didn’t break formatting

---

By contributing, you agree to follow the project's open source license and code of conduct.