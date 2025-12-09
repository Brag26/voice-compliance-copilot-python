import asyncio
from apify import Actor

from actors.audio_transcriber.main import main as audio_main
from actors.prompt_response_loader.main import main as demo_main

async def main():
    async with Actor:
        input_data = await Actor.get_input() or {}
        mode = input_data.get("mode", "demo")

        print(f"Starting pipeline in {mode} mode...")

        if mode == "audio":
            await audio_main()   # ✅ SAME PROCESS → DATASET WILL WORK
        else:
            demo_main()

        print("Pipeline completed.")

if __name__ == "__main__":
    asyncio.run(main())
