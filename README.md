# Mock BTC Price MCP

A minimal, read-only demo MCP server. Its sole tool, `get_btc_price`, always
returns the fixed text below and never accesses a market-data API:

```text
BTC今天的价格是 6万美元
```

## Publish to GitHub

Create a new public GitHub repository named `mock-btc-price-mcp`, then commit
the contents of this directory to its default branch.

## ModelScope configuration

Replace `YOUR_GITHUB_USER` with the GitHub owner of that repository, select
`uvx` in ModelScope, and paste:

```json
{
  "mcpServers": {
    "mock-btc-price": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/YOUR_GITHUB_USER/mock-btc-price-mcp.git",
        "mock-btc-price-mcp"
      ]
    }
  }
}
```

The first launch downloads the public GitHub repository and its declared Python
dependency. No API key is needed.
