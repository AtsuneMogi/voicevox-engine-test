import subprocess

def enter(text):
    subprocess.run(
        f'echo -n "{text}" >text.txt',
        shell=True
    )
    subprocess.run(
        'curl -s \
        -X POST \
        "localhost:50021/audio_query?speaker=1" \
        --get --data-urlencode text@text.txt \
        > query.json',
        shell=True
    )
    subprocess.run(
        'curl -s \
        -H "Content-Type: application/json" \
        -X POST \
        -d @query.json \
        "localhost:50021/synthesis?speaker=1" \
        > audio.wav',
        shell=True
    )


def main():
    while (1):
        text = input()
        enter(text)
        subprocess.run("paplay audio.wav", shell=True)


if __name__ == '__main__':
    main()

