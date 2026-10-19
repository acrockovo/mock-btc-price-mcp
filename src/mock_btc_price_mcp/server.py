"""A deliberately static MCP server for integration demonstrations."""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("mock-btc-price")


@mcp.tool()
def get_btc_price() -> str:
    """Return a fixed simulated BTC price; no live market data is queried."""
    return "BTC今天的价格是 6万美元"


def main() -> None:
    """Start the MCP server over standard input/output."""
    mcp.run(transport="stdio")
