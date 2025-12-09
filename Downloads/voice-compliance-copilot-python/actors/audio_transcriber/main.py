import json
import speech_recognition as sr
from pydub import AudioSegment
from pathlib import Path
from apify import Actor

OUTPUT_PATH = Path("outputs/pairs_loaded.json")

async def main():
    async with Actor:
        input_data = await Actor.get_input() or {}
        audio_files = input_data.get('audio_files', [])
        store = await Actor.open_key_value_store()
        r = sr.Recognizer()
        results = []

        for idx, key in enumerate(audio_files, start=1):
            audio_bytes = await store.get_value(key)
            if not audio_bytes:
                continue

            temp = Path(f"/tmp/{key}")
            temp.write_bytes(audio_bytes)

            temp_wav = temp
            if temp.suffix.lower() != '.wav':
                temp_wav = temp.with_suffix('.wav')
                AudioSegment.from_file(temp).export(temp_wav, format='wav')

            with sr.AudioFile(str(temp_wav)) as src:
                audio = r.record(src)

            try:
                text = r.recognize_google(audio)
            except:
                text = ""

            rec = {
                "id": f"CALL-{idx}",
                "audio_key": key,
                "response": text
            }

            results.append(rec)
            await Actor.push_data(rec)

        OUTPUT_PATH.parent.mkdir(exist_ok=True)
        OUTPUT_PATH.write_text(json.dumps(results, indent=2))
        await Actor.set_value("transcripts.json", results)

        print("Cloud audio processing completed")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())