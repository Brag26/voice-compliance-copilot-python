import os
import asyncio
from apify import Actor

async def main():
    async with Actor:
        input_data = await Actor.get_input() or {}
        mode = input_data.get("mode", "demo")

        print(f"Starting pipeline in {mode} mode...")

        if mode == "audio":
            os.system("python actors/audio_transcriber/main.py")
        else:
            os.system("python actors/prompt_response_loader/main.py")

        os.system("python actors/quality_judge/main.py")
        os.system("python actors/report_generator/main.py")

        print("Pipeline completed.")

if __name__ == "__main__":
    asyncio.run(main())
