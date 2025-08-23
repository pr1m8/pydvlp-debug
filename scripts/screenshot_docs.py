#!/usr/bin/env python3
"""Screenshot documentation pages using Playwright."""

import asyncio
import os
from pathlib import Path
from datetime import datetime
from playwright.async_api import async_playwright

async def screenshot_page(url: str, output_name: str):
    """Take a screenshot of a webpage."""
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        # Navigate to the page
        print(f"📸 Navigating to {url}")
        await page.goto(url, wait_until='networkidle')
        
        # Wait a bit for any animations to complete
        await page.wait_for_timeout(2000)
        
        # Create screenshots directory
        screenshots_dir = Path(__file__).parent.parent / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)
        
        # Take screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = screenshots_dir / f"{output_name}_{timestamp}.png"
        
        await page.screenshot(path=filepath, full_page=True)
        print(f"✅ Screenshot saved to: {filepath}")
        
        # Also take a viewport-only screenshot
        viewport_filepath = screenshots_dir / f"{output_name}_viewport_{timestamp}.png"
        await page.screenshot(path=viewport_filepath, full_page=False)
        print(f"✅ Viewport screenshot saved to: {viewport_filepath}")
        
        await browser.close()

async def main():
    """Screenshot the documentation pages."""
    pages_to_screenshot = [
        ("https://pydvlp-debug.readthedocs.io/en/latest/", "home"),
        ("https://pydvlp-debug.readthedocs.io/en/latest/guides/getting-started/", "getting_started"),
        ("https://pydvlp-debug.readthedocs.io/en/latest/api/", "api_reference"),
        ("https://pydvlp-debug.readthedocs.io/en/latest/CONTRIBUTING/", "contributing"),
    ]
    
    for url, name in pages_to_screenshot:
        try:
            await screenshot_page(url, name)
        except Exception as e:
            print(f"❌ Error screenshotting {url}: {e}")
    
    print("\n🎉 All screenshots completed!")

if __name__ == "__main__":
    # Install playwright browsers if needed
    os.system("playwright install chromium")
    
    # Run the screenshot script
    asyncio.run(main())