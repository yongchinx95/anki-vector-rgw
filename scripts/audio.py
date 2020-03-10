import anki_vector


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.audio.stream_wav_file("../resources/music/petitbiscuit.wav", 75)


if __name__ == "__main__":
    main()
