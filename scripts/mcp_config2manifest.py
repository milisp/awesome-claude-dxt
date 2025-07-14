#!/usr/bin/env python3
"""
MCP Server Configuration to DXT Manifest.json Converter

This tool automatically converts MCP server configurations to Claude Desktop extension
manifest.json format according to the DXT specification.
"""

import json
import os
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, Optional, List
import re


BASE_DIR = Path(__file__).parent.parent

class MCPToManifestConverter:
    def __init__(self):
        self.manifest_template = {
            "dxt_version": "0.1",
            "name": "",
            "version": "1.0.0",
            "description": "",
            "author": {
                "name": "",
                "email": "",
                "url": ""
            },
            "server": {
                "type": "python",
                "entry_point": "",
                "mcp_config": {
                    "command": "",
                    "args": [],
                    "env": {}
                }
            }
        }

    def detect_server_type(self, config: Dict[str, Any]) -> str:
        """Detect server type based on command or arguments"""
        command = config.get("command", "")
        args = config.get("args", [])

        if command == "python" or command.endswith("python"):
            return "python"
        elif command == "node" or command.endswith("node"):
            return "node"
        elif command == "npx":
            return "node"
        elif any(arg.endswith(".py") for arg in args):
            return "python"
        elif any(arg.endswith(".js") for arg in args):
            return "node"
        elif os.path.isfile(command) and os.access(command, os.X_OK):
            return "binary"
        else:
            return "python"  # Default fallback

    def extract_entry_point(self, config: Dict[str, Any], server_type: str) -> str:
        """Extract entry point from MCP config"""
        command = config.get("command", "")
        args = config.get("args", [])

        if server_type == "python":
            # Look for .py file in args
            for arg in args:
                if arg.endswith(".py"):
                    return arg
            return "server/main.py"  # Default

        elif server_type == "node":
            # Look for .js file in args
            for arg in args:
                if arg.endswith(".js"):
                    return arg
            return "server/index.js"  # Default

        elif server_type == "binary":
            return command

        return "server/main.py"  # Default fallback

    def generate_name_from_path(self, path: str) -> str:
        """Generate a name from file path or command"""
        # Remove common prefixes and suffixes
        name = os.path.basename(path)
        name = re.sub(r'\.(py|js|exe)$', '', name)
        name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
        return name.lower()

    def convert_claude_desktop_config(self, config_path: str, server_name: str = None) -> Dict[str, Any]:
        """Convert Claude Desktop MCP configuration to manifest.json"""
        try:
            with open(config_path, 'r') as f:
                claude_config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Error reading Claude Desktop config: {e}")

        # Extract MCP server configuration
        mcp_servers = claude_config.get("mcpServers", {})

        if not mcp_servers:
            raise ValueError("No MCP servers found in Claude Desktop configuration")

        # If server_name is specified, use that server, otherwise use the first one
        if server_name:
            if server_name not in mcp_servers:
                raise ValueError(f"Server '{server_name}' not found in configuration")
            server_config = mcp_servers[server_name]
            name = server_name
        else:
            # Use the first server
            name = list(mcp_servers.keys())[0]
            server_config = mcp_servers[name]

        return self.convert_mcp_config(server_config, name)

    def convert_mcp_config(self, config: Dict[str, Any], name: str = None) -> Dict[str, Any]:
        """Convert MCP server configuration to manifest.json"""
        manifest = self.manifest_template.copy()

        # Set basic info
        command = config.get("command", "")
        args = config.get("args", [])
        env = config.get("env", {})

        # Generate name if not provided
        if not name:
            name = self.generate_name_from_path(command)

        manifest["name"] = name
        manifest["display_name"] = name.replace("_", " ").replace("-", " ").title()
        manifest["description"] = f"MCP server for {name}"

        # Detect server type and entry point
        server_type = self.detect_server_type(config)
        entry_point = self.extract_entry_point(config, server_type)

        manifest["server"]["type"] = server_type
        manifest["server"]["entry_point"] = entry_point
        manifest["server"]["mcp_config"] = {
            "command": command,
            "args": args,
            "env": env
        }

        # Add compatibility requirements based on server type
        if server_type == "python":
            manifest["compatibility"] = {
                "runtimes": {
                    "python": ">=3.8"
                }
            }
        elif server_type == "node":
            manifest["compatibility"] = {
                "runtimes": {
                    "node": ">=16.0.0"
                }
            }

        return manifest

    def enhance_manifest_with_package_info(self, manifest: Dict[str, Any], package_dir: str) -> Dict[str, Any]:
        """Enhance manifest with information from package.json or pyproject.toml"""
        package_dir = Path(package_dir)

        # Try to read package.json
        package_json_path = package_dir / "package.json"
        if package_json_path.exists():
            try:
                with open(package_json_path, 'r') as f:
                    package_data = json.load(f)

                # Update manifest with package.json info
                if "name" in package_data:
                    manifest["name"] = package_data["name"]
                if "version" in package_data:
                    manifest["version"] = package_data["version"]
                if "description" in package_data:
                    manifest["description"] = package_data["description"]
                if "author" in package_data:
                    if isinstance(package_data["author"], str):
                        manifest["author"]["name"] = package_data["author"]
                    elif isinstance(package_data["author"], dict):
                        manifest["author"].update(package_data["author"])
                if "repository" in package_data:
                    if isinstance(package_data["repository"], str):
                        manifest["repository"] = {"type": "git", "url": package_data["repository"]}
                    elif isinstance(package_data["repository"], dict):
                        manifest["repository"] = package_data["repository"]
                if "license" in package_data:
                    manifest["license"] = package_data["license"]
                if "keywords" in package_data:
                    manifest["keywords"] = package_data["keywords"]
                if "homepage" in package_data:
                    manifest["homepage"] = package_data["homepage"]

            except (json.JSONDecodeError, KeyError):
                pass

        # Try to read pyproject.toml for Python projects
        pyproject_path = package_dir / "pyproject.toml"
        if pyproject_path.exists():
            try:
                import tomllib
                with open(pyproject_path, 'rb') as f:
                    pyproject_data = tomllib.load(f)

                project = pyproject_data.get("project", {})
                if "name" in project:
                    manifest["name"] = project["name"]
                if "version" in project:
                    manifest["version"] = project["version"]
                if "description" in project:
                    manifest["description"] = project["description"]
                if "authors" in project and project["authors"]:
                    author = project["authors"][0]
                    if "name" in author:
                        manifest["author"]["name"] = author["name"]
                    if "email" in author:
                        manifest["author"]["email"] = author["email"]
                if "license" in project:
                    if isinstance(project["license"], dict) and "text" in project["license"]:
                        manifest["license"] = project["license"]["text"]
                    else:
                        manifest["license"] = str(project["license"])
                if "keywords" in project:
                    manifest["keywords"] = project["keywords"]
                if "urls" in project:
                    urls = project["urls"]
                    if "homepage" in urls:
                        manifest["homepage"] = urls["homepage"]
                    if "repository" in urls:
                        manifest["repository"] = {"type": "git", "url": urls["repository"]}

            except (ImportError, Exception):
                pass

        return manifest

    def write_manifest(self, manifest: Dict[str, Any], output_path: str):
        """Write manifest to file"""
        with open(output_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f"Manifest written to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert MCP server configuration to DXT manifest.json"
    )
    parser.add_argument(
        "input",
        help="Path to MCP config file or Claude Desktop config file"
    )
    parser.add_argument(
        "-o", "--output",
        default="manifest.json",
        help="Output path for manifest.json (default: manifest.json)"
    )
    parser.add_argument(
        "-n", "--name",
        help="Server name (for Claude Desktop config with multiple servers)"
    )
    parser.add_argument(
        "-p", "--package-dir",
        help="Package directory to extract additional metadata from"
    )
    parser.add_argument(
        "--claude-desktop",
        action="store_true",
        help="Input is Claude Desktop configuration file"
    )

    args = parser.parse_args()

    converter = MCPToManifestConverter()

    try:
        if args.claude_desktop:
            # Convert from Claude Desktop config
            manifest = converter.convert_claude_desktop_config(args.input, args.name)
        else:
            # Convert from standalone MCP config
            with open(args.input, 'r') as f:
                mcp_config = json.load(f)
            manifest = converter.convert_mcp_config(mcp_config, args.name)

        # Enhance with package information if package directory is provided
        if args.package_dir:
            manifest = converter.enhance_manifest_with_package_info(manifest, args.package_dir)

        # Write manifest
        converter.write_manifest(manifest, args.output)

        print(f"Successfully converted MCP configuration to DXT manifest!")
        print(f"Remember to:")
        print(f"  - Update author information")
        print(f"  - Add appropriate description")
        print(f"  - Add tools and prompts arrays if needed")
        print(f"  - Add user_config if your server needs user configuration")
        print(f"  - Add icon and screenshots")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
