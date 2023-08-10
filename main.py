from cut_video import cut_video


def main():
    err = cut_video(
        url='https://www.youtube.com/watch?v=4JPviBRbcrQ',
        codec='copy',
        format='mp4',
        time_off='00:01:10',
        duration='00:00:20',
        path_prefix='media',
    )

    if err is not None:
        print(err)


if __name__ == '__main__':
    main()