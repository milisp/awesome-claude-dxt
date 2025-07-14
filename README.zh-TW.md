# Awesome (not only Claude) Desktop Extensions (.dxt) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README.zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README.ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README.ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README.pt-BR.md)
[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README.th.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README.zh-TW.md)

[![Stars](https://img.shields.io/github/stars/milisp/awesome-claude-dxt?style=social)](https://github.com/milisp/awesome-claude-dxt/stargazers)
[![Forks](https://img.shields.io/github/forks/milisp/awesome-claude-dxt?style=social)](https://github.com/milisp/awesome-claude-dxt/network/members)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/dxt?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/dxt/)
[![Last Commit](https://img.shields.io/github/last-commit/milisp/awesome-claude-dxt)](https://github.com/milisp/awesome-claude-dxt/commits)
[![License](https://img.shields.io/github/license/milisp/awesome-claude-dxt)](LICENSE)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-yellow?logo=buymeacoffee)](https://www.buymeacoffee.com/milisp)

精選 Claude Desktop 擴充（.dxt 檔案）、工具與資源列表

## 什麼是 DXT?

[dxt](https://www.anthropic.com/engineering/desktop-extensions) 是 Desktop Extensions：為 Claude Desktop 一鍵安裝 MCP 伺服器

## 目錄
- [官方資源](#官方資源)
- [社群資源](#社群資源)
- [依類別分類的擴充](#依類別分類的擴充)
  - [開發工具](#開發工具)
  - [檔案管理](#檔案管理)
  - [系統工具](#系統工具)
  - [網路服務](#網路服務)
  - [訊息傳遞](#訊息傳遞)
  - [資料庫](#資料庫)
  - [分析工具](#分析工具)
  - [AI 系統](#ai-系統)
  - [MCP 工具](#mcp-工具)
  - [API 整合](#api-整合)
  - [資料分析](#資料分析)
  - [知識庫](#知識庫)
  - [媒體創作](#媒體創作)
  - [生產力](#生產力)
  - [專業應用](#專業應用)
  - [財務](#財務)
  - [範例](#範例)
- [開發工具](#開發工具-1)
- [打包與管理](#打包與管理)
- [文件與教學](#文件與教學)

## 官方資源
- [Desktop Extensions 公告](https://www.anthropic.com/engineering/desktop-extensions) - 官方部落格
- [DXT 規範](https://github.com/anthropics/dxt) - 開源工具鏈與規範
- [提交表單](https://forms.gle/tyiAZvch1kDADKoP9) - 提交到官方目錄
- [官方範例](https://github.com/anthropics/dxt/tree/main/examples) - 官方範例

## 社群

* [r/dxt Reddit](https://www.reddit.com/r/dxt)

## 貢獻
本列表由社群維護。請參閱 [CONTRIBUTING.md](CONTRIBUTING.md) 取得指引。

## 依類別分類的擴充

所有擴充都位於 servers 資料夾中，每個擴充依 owner/repo 組織，並包含 `manifest.json` 和 `user_config.json`。若 `manifest.json` 經社群驗證，還會包含 `verified.json` 檔案。

### 開發工具

<!-- 以下為英文原文，請根據需要翻譯描述 -->
- [chrome-applescript](https://github.com/anthropics/dxt/tree/main/examples/chrome-applescript) - 透過 AppleScript 進行瀏覽器自動化
- [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) - 連接 Kubernetes 叢集並管理 pods、deployments 和 services。
- [modelcontextprotocol/gitlab](https://github.com/modelcontextprotocol/servers/blob/main/src/gitlab) - GitLab API，專案管理
- [modelcontextprotocol/git](https://github.com/modelcontextprotocol/servers/blob/main/src/git) - 讀取、搜尋與操作 Git 儲存庫的工具
- [bazinga012/mcp_code_executor](https://github.com/bazinga012/mcp_code_executor) - 允許 LLM 在指定 Conda 環境中執行 Python 代碼的 MCP 伺服器
- [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) - 管理編碼偏好的 Model Context Protocol 伺服器
- [modelcontextprotocol/github](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) - 儲存庫管理、檔案操作與 GitHub API 整合
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) - 與 [OpenAPI](https://www.openapis.org/) API 互動
- [semgrep/mcp](https://github.com/semgrep/mcp) - 使用 Semgrep 掃描程式碼安全漏洞的 MCP 伺服器
- [manusa/kubernetes-mcp-server](https://github.com/manusa/kubernetes-mcp-server) - 強大的 Kubernetes MCP 伺服器，支援 OpenShift
- [pathintegral-institute/mcp.science](https://github.com/pathintegral-institute/mcp.science) - 安全的 Python 沙盒執行環境
- [MindscapeHQ/mcp-server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) - Raygun API V3 端點的 MCP 伺服器
- [baryhuang/mcp-server-any-openapi](https://github.com/baryhuang/mcp-server-any-openapi) - 內建語意搜尋的大型 [OpenAPI](https://www.openapis.org/) 文件互動
- [yanmxa/multicluster-mcp-server](https://github.com/yanmxa/multicluster-mcp-server) - 多 Kubernetes 叢集互動閘道
- [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) - 管理 n8n 工作流程與執行
- [hannesj/mcp-openapi-schema](https://github.com/hannesj/mcp-openapi-schema) - 探索大型 [OpenAPI](https://www.openapis.org/) schema
- [ShenghaiWang/xcodebuild](https://github.com/ShenghaiWang/xcodebuild) - 🍎 建置 iOS Xcode 專案並回饋錯誤
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) - 可設定檔案包含/排除規則的 repo 打包 MCP 工具
- [lingodotdev/lingo.dev](https://github.com/lingodotdev/lingo.dev) - 連接 Lingo.dev 的 MCP 標準指南
- [modelcontextprotocol/sentry](https://github.com/modelcontextprotocol/servers/blob/main/src/sentry) - 從 Sentry.io 擷取與分析問題
- [apimatic/apimatic-validator-mcp](https://github.com/apimatic/apimatic-validator-mcp) - 使用 APIMatic API 驗證 OpenAPI 規格
- [riza-io/riza-mcp](https://github.com/riza-io/riza-mcp) - [Riza](https://riza.io) 提供 LLM 隔離代碼解譯器
- [Boston343/starwind-ui-mcp](https://github.com/Boston343/starwind-ui-mcp) - Starwind UI 元件的 MCP 伺服器
- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) - Cloudflare API 的 MCP 伺服器
- [its-dart/dart-mcp-server](https://github.com/its-dart/dart-mcp-server) - Dart MCP 伺服器
- [agentrpc/agentrpc](https://github.com/agentrpc/agentrpc) - 跨網路與語言的 AI agent RPC 層
- [yangkyeongmo/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) - 連接 Apache Airflow 的 MCP 伺服器
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) - 存取 OpenTelemetry traces 的 MCP 伺服器
- [GongRzhe/JSON-MCP-Server](https://github.com/GongRzhe/JSON-MCP-Server) - 進階 JSONPath 查詢與處理
- [hannesj/mcp-graphql-schema](https://github.com/hannesj/mcp-graphql-schema) - 探索大型 GraphQL schema
- [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) - 透過自然語言描述快速生成 UI 元件
- [shannonlal/mcp-postman](https://github.com/shannonlal/mcp-postman) - 執行 Postman Collections 的 MCP 伺服器
- [bigcodegen/mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server) - Neovim session 的 MCP 伺服器
- [rishikavikondala/mcp-server-aws](https://github.com/rishikavikondala/mcp-server-aws) - 操作 AWS 資源
- [ko1ynnky/github-actions-mcp-server](https://github.com/ko1ynnky/github-actions-mcp-server) - 與 Github Actions 互動的 MCP 伺服器
- [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) - Docker 管理
- [shanejonas/openrpc-mpc-server](https://github.com/shanejonas/openrpc-mpc-server) - 與 JSON-RPC API 互動
- [chargebee/agentkit](https://github.com/chargebee/agentkit) - 連接 Chargebee 平台的 MCP 伺服器
- [ognis1205/mcp-server-unitycatalog](https://github.com/ognis1205/mcp-server-unitycatalog) - Unity Catalog AI 互動
- [JetBrains/mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains) - JetBrains IDE 請求代理

<!-- 其餘分類與內容請依照英文 README.md 逐一翻譯與補充，保留原有格式與連結，描述翻譯為繁體中文 -->

### 檔案管理

- [file-manager-python](https://github.com/anthropics/dxt/tree/main/examples/file-manager-python)

<!-- ... 其餘分類與內容請依照英文 README.md 逐一翻譯與補充 ... -->

<!-- 範例區塊與 JSON 範例 -->

### 範例

- [hello-world-node](https://github.com/anthropics/dxt/tree/main/examples/hello-world-node) - 基本 MCP 伺服器，提供簡單時間工具
- [Blender](./servers/blender-mcp) - Blender Model Context Protocol 整合

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

## 文件與教學

- [desktop-extensions](https://www.anthropic.com/engineering/desktop-extensions)

## 打包與管理工具
- [mcp-linker](https://github.com/milisp/mcp-linker) - 跨平台 MCP 管理工具，計畫支援 .dxt 🚀
- [@anthropic-ai/dxt](https://www.npmjs.com/package/@anthropic-ai/dxt) - 官方打包工具

## 關於
由 [@milisp](https://github.com/milisp) 整理 | [mcp-linker](https://github.com/milisp/mcp-linker) 作者

<!-- 你可以根據需要繼續翻譯與補充內容 -->
