"""from mcp.server.fastmcp import FastMCP
from app import fetch_news, generate_video_transcription

mcp = FastMCP("this is for real time news ")

@mcp.tool()
async def fetch_new_mcp(query):
    return fetch_news(query=query)


@mcp.tool()
async def gen_vid_trans_mcp(query):
    news = fetch_news(query=query)
    return generate_video_transcription(news)


if __name__ == "__main__":
    mcp.run(transport = "stdio")"""
    

from mcp.server.fastmcp import FastMCP
from app import get_realtime_info, generate_video_transcription

mcp= FastMCP("This is for video Script Generator")

@mcp.tool()
async def get_latest_info_mcp(query):
    return get_realtime_info(query)

@mcp.tool()
async def get_video_script_mcp(query):
    real_info = get_realtime_info(query)
    return generate_video_transcription(real_info)

if __name__=="__main__":
    mcp.run(transport="stdio")