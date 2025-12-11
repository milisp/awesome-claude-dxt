#!/usr/bin/env python
import json
from pathlib import Path
import requests

raw_url = "https://raw.githubusercontent.com/samanhappy/mcphub/main/servers.json"
servers_file = Path("servers.json")

if servers_file.exists():
    with open(servers_file, "r") as f:
        servers = json.load(f)
else:
    response = requests.get(raw_url)
    if response.status_code == 200:
        servers = response.json()
        with open(servers_file, "w") as f:
            json.dump(servers, f, indent=2)
    else:
        raise Exception(f"Failed to fetch servers.json: {response.status_code}")


def write_json(filename="manifest.json", manifest=None):
    with open(filename, "w") as f:
        json.dump(manifest, f, indent=2)


def get_server_type_command(installations):
    if "uvx" in installations or "uv" in installations:
        server_type = "python"
        command = "uvx" if "uvx" in installations else "uv"
    elif "npm" in installations or "npx" in installations:
        server_type = "node"
        command = "npx" if "npx" in installations else "npm"
    elif "python" in installations:
        server_type = "python"
        command = "python"
    else:
        print(installations)
        return None, None
    return server_type, command


def get_author(data):
    author = data.get("author", {})
    keys = ["name", "email", "url"]
    return {key: author[key] for key in keys if key in author}


def get_user_config(data):
    _user_config = data.get("arguments", {})
    user_config = {}
    for k, v in _user_config.items():
        try:
            example = v.get("example", v.get("description")).lower()
            if "true" in example:
                _type = "boolean"
            elif "port" in example or example.isalnum():
                _type = "number"
            elif "dir" in example or "path" in example:
                _type = "directory"
            else:
                _type = "string"
            _v = {
                "type": _type,
                "description": v["description"],
                "sensitive": "key" in k.lower() or "token" in k.lower(),
                "title": k,
                "required": v["required"],
            }
            user_config[k] = _v
        except Exception as e:
            raise Exception(f"Error processing user config: {str(e)}")
    return user_config


def get_manifest(data):
    installations = data.get("installations")
    server_type, command = get_server_type_command(installations)
    if not server_type:
        return None
    config = installations[command]
    prompts = data.get("examples", [])
    _prompts = []
    if prompts:
        for prompt in prompts:
            _prompt = {}
            _prompt["name"] = prompt["title"]
            _prompt["description"] = prompt["description"]
            _prompt["text"] = prompt["prompt"]
            _prompts.append(_prompt)
        prompts = _prompts
    author = data.get("author")
    repository = data.get("repository")
    if not author:
        repo_url = repository["url"]
        author = repo_url.split("/")[3]
    if data.get("tools"):
        data["tools"] = [
            {"name": t["name"], "description": t.get("description", "")}
            for t in data["tools"]
        ]
    else:
        data["tools"] = []
    manifest = {
        "dxt_version": "0.1",
        "name": data["name"],
        "display_name": data.get("display_name", data["name"]),
        "version": "1.0.0",
        "description": data.get("description", ""),
        "long_description": "",
        "author": get_author(data),
        "repository": {
            "type": repository.get("type", "git"),
            "url": repository.get("url", ""),
        },
        "homepage": data.get("homepage", ""),
        "screenshots": [],
        "server": {
            "type": server_type,
            "entry_point": "",
            "mcp_config": {
                "command": config.get("command"),
                "args": config.get("args", []),
                "env": config.get("env", {}),
            },
        },
        "tools": data.get("tools", []),
        "prompts": prompts,
        "tools_generated": True,
        "keywords": list(set(data.get("categories", []) + data.get("tags", []))),
        "license": data.get("license", ""),
    }
    user_config = get_user_config(data)
    if user_config:
        manifest.update(dict(user_config=user_config))
    return manifest


count = 0
keys = set()
readme = ""
BASE_DIR = Path.cwd() / "servers"
server_list = []
for k, v in servers.items():
    # print(k, v['installations'].keys())
    installations = v["installations"]
    if (
        "uvx" in installations
        or "python" in installations
        or "npm" in installations
        or "uv" in installations
        or "npx" in installations
    ):
        # print(k, list(installations.keys()))
        count += 1
        manifest = get_manifest(v)
        repository = v["repository"]
        repo_url = repository.get("url")
        repo_name = repository.get("url").split("/")[-1]
        author = v.get("author", {}).get("name", "")
        if not author:
            repo_url = repository["url"]
            author = repo_url.split("/")[3]
            print("no author", author, repo_name, repo_url)
        if not repo_name:
            print("no repo_name", author, repo_name, repo_url)
        name = v["name"]
        cache_dir = BASE_DIR / Path(author) / name
        cache_dir.mkdir(parents=True, exist_ok=True)
        description = v["description"]
        categories = v["categories"]
        if len(categories) > 1:
            pass
            # print(k, categories)
        readme += f"{categories} - [{author}/{repo_name}]({repo_url}) - {description}\n"
        server_list.append(
            dict(
                categorie=categories[0],
                author=author,
                repo_name=repo_name,
                repo_url=repo_url,
                description=description,
            )
        )
        write_json(cache_dir / "manifest.json", manifest)
        write_json(cache_dir / "user_config.json", get_user_config(v))
    if count == 10:
        # break
        pass


_servers = {}
for i, server in enumerate(server_list):
    try:
        cat = server["categorie"]
        # print(server)
        repo_name = server["repo_name"]
        repo_url = server["repo_url"]
        author = server["author"]
        description = server["description"]

        line = f"- [{author}/{repo_name}]({repo_url}) - {description}\n"
        if cat not in _servers:
            _servers[cat] = line
        else:
            _servers[cat] += line
    except Exception as e:
        print(f"Error processing server {i}: {e}")
        raise Exception(f"Failed to process server {i}: {str(e)}")


text = ""
for cat, awesome_servers in _servers.items():
    # print(awesome_servers)
    text += f"### {cat}\n\n{awesome_servers}\n"
    print(cat)


temp_readme = Path("/tmp/README_tmp.md")
print(temp_readme)
temp_readme.write_text(text)
