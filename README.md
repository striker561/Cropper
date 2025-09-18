# Cropper 🎵

## Why does this exist?

Because cropping audio in Audacity made me want to throw my computer out the window. I'm a developer, so instead of learning to use a mouse, I wrote a Python script. Now you too can batch-crop teasers from your audio tracks with the power of code and zero rage-quits.

---

## Features

- Batch crop and fade audio tracks (MP3/WAV)
- Specify crop times per track in a simple JSON file
- High-quality output (MP3: 320kbps, WAV: 44.1kHz stereo)
- Handles missing files gracefully (no more mysterious crashes)
- Beautiful, readable logs (with timestamps!)
- Modular, class-based code for easy extension
- Because you deserve better than dragging sliders

---

## Usage

1. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

   **You must also install [ffmpeg](https://ffmpeg.org/download.html) and make sure it's in your PATH.**
   If you don't, pydub will complain and nothing will work. (Seriously, ffmpeg is required for audio processing!)

2. **Prepare your audio files:**

   - Put your source files in the `input_audio/` folder.
   - Specify crop instructions in a `crop.json` file (see below).

3. **Create `crop.json`:**

   Example:

   ```json
   [
     { "filename": "song1.mp3", "start": 30, "end": 60 },
     { "filename": "song2.wav", "start": 10, "end": 25 }
   ]
   ```

4. **Run the script:**

   ```sh
   python main.py
   ```

   Output teasers will appear in `output_teasers/`. Magic!

---

## Configuration

- Edit `main.py` to change input/output folders or fade duration.
- The script will check for `crop.json` in the project root and use it if present.

---

## Project Structure

- `main.py` — Entry point
- `cropper/logger.py` — Logger setup
- `cropper/audio_processor.py` — Audio cropping/fading logic
- `cropper/teaser_batcher.py` — Batch processing logic
- `requirements.txt` — Python dependencies

---

## Advanced

- Ignores input/output folders, cache, and venv in `.gitignore`.
- Modular and ready for extension.

---

## License

Open source. Use, modify, and share freely. If you improve it, send me a PR so I can stop using Audacity too and yes before you ask, it was made with the assistance of AI.
